# Copyright (c) 2026 Advanced Micro Devices, Inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
#
# Macroop text generators for VEX instructions.
#
# The EVEX side has the same problem and the same answer in
# insts/evex/macroop_gen.py; see the comment there. VEX needs six macroops
# per instruction rather than eighteen -- two register widths times register,
# memory and rip-relative source, with no masked forms -- but the arithmetic
# of getting every width and element size right by hand is the same.
#
# This file is not listed in any __init__.py's categories: it supplies text to
# the category modules rather than contributing microcode of its own.

# (VEX.L name, register prefix, load microop, memory operand size)
WIDTHS = [
    ("XMM", "xmm", "ldvec128", 16),
    ("YMM", "ymm", "ldvec256", 32),
]


def _widths(only):
    """
    The width rows to generate. Passing only=["YMM"] fills in the half of a
    set whose other half is already written out by hand.
    """
    if only is None:
        return WIDTHS
    return [w for w in WIDTHS if w[0] in only]


def _load(load, width, riprel):
    """The lines that bring a memory source into uvec1."""
    if riprel:
        return ["    rdip t7",
                '    %s uvec1, seg, riprel, "DISPLACEMENT", dataSize=%d'
                % (load, width)]
    return ['    %s uvec1, seg, sib, "DISPLACEMENT", dataSize=%d'
            % (load, width)]


def _macroop(name, lines):
    return "def macroop %s {\n%s\n};\n" % (name, "\n".join(lines))


def _forms(ext, reg):
    """
    The three source forms of one width: a register, a memory operand and a
    rip-relative memory operand. Returns (name suffix, source symbol, riprel).
    """
    return (("%sMM" % ext[0], "%sm" % reg, False),
            ("M", "uvec1", False),
            ("P", "uvec1", True))


def binop(name, microop, size, only=None, ext_prefix=""):
    """
    A vector instruction reading a register and a register or memory operand
    and writing a register, which is most of them. size is the element size
    in bytes; ext_prefix prepends flags to the width, as in "Signed |".
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext_prefix + ext)
        for form, src, riprel in _forms(ext, reg):
            # VEX_VPADDB_XMM_XMM_XMM, _XMM_XMM_M, _XMM_XMM_P
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)
            out.append(_macroop("%s_%s_%s_%s" % (name, ext, ext, form), pre + [
                "    %s %s1, %s2, %s, %s" % (microop, reg, reg, src, tail)]))
    return "".join(out)


def binop_imm(name, microop, size, only=None,
              ext_prefix="(IMMEDIATE & mask(8)) |"):
    """
    A two-source instruction with an immediate, such as VMPSADBW. The
    immediate reaches the microop through ext rather than as an operand.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = 'size=%d, ext="%s" + %s' % (size, ext_prefix, ext)
        for form, src, riprel in _forms(ext, reg):
            # VEX_VMPSADBW_XMM_XMM_XMM_I, _XMM_XMM_M_I, _XMM_XMM_P_I
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)
            out.append(_macroop("%s_%s_%s_%s_I" % (name, ext, ext, form),
                                pre + [
                "    %s %s1, %s2, %s, %s" % (microop, reg, reg, src, tail)]))
    return "".join(out)


def unop(name, microop, size, only=None):
    """
    A vector instruction reading one register or memory operand: VPABSB and
    friends. The destination symbol has no digit in this form.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext)
        for form, src, riprel in _forms(ext, reg):
            # VEX_VPABSB_XMM_XMM, _XMM_M, _XMM_P
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)
            out.append(_macroop("%s_%s_%s" % (name, ext, form), pre + [
                "    %s %s, %s, %s" % (microop, reg, src, tail)]))
    return "".join(out)


def shift_imm(name, microop, size, only=None):
    """
    A shift by an immediate: the count comes from the immediate byte and the
    value shifted is the register or memory source, so there is no second
    register operand. The microop name takes the assembler's 'i' suffix,
    which selects the immediate form of an op2-using microop.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext)
        for form, src, riprel in (("%sMM_I" % ext[0], "%sm" % reg, False),
                                  ("M_I", "uvec1", False),
                                  ("P_I", "uvec1", True)):
            # VEX_VPSLLW_XMM_XMM_I, _XMM_M_I, _XMM_P_I
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)
            out.append(_macroop("%s_%s_%s" % (name, ext, form), pre + [
                "    %si %s1, %s, imm, %s" % (microop, reg, src, tail)]))
    return "".join(out)


def shift_count(name, microop, size, only=None):
    """
    A shift whose count is the low 64 bits of an XMM operand, so the third
    operand is 128 bits wide whatever the width of the other two.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext)
        for form, src, riprel in (("XMM", "xmmm", False),
                                  ("M", "uvec1", False),
                                  ("P", "uvec1", True)):
            # VEX_VPSLLW_YMM_YMM_XMM, _YMM_YMM_M, _YMM_YMM_P
            pre = [] if src == "xmmm" else _load("ldvec128", 16, riprel)
            out.append(_macroop("%s_%s_%s_%s" % (name, ext, ext, form), pre + [
                "    %s %s1, %s2, %s, %s" % (microop, reg, reg, src, tail)]))
    return "".join(out)


def widen(name, microop, srcSize, destSize, only=None):
    """
    An extending move such as VPMOVSXBW, whose source holds as many elements
    as the destination but each of them narrower. The source is an XMM
    register or a 128-bit memory operand whatever the destination width, and
    the microop reads only the low elements it needs; this follows the
    VPMOVSXDQ macroops that were already written out by hand.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "srcSize=%d, destSize=%d, ext=%s" % (srcSize, destSize, ext)
        for form, src, riprel in (("XMM", "xmmm", False),
                                  ("M", "uvec1", False),
                                  ("P", "uvec1", True)):
            # VEX_VPMOVSXBW_YMM_XMM, _YMM_M, _YMM_P
            pre = [] if src == "xmmm" else _load("ldvec128", 16, riprel)
            out.append(_macroop("%s_%s_%s" % (name, ext, form), pre + [
                "    %s %s, %s, %s" % (microop, reg, src, tail)]))
    return "".join(out)
