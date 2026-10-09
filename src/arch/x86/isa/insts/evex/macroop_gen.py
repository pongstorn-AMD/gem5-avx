# Copyright (c) 2026 Advanced Micro Devices, Inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
#
# Macroop text generators for EVEX instructions.
#
# An EVEX instruction needs the same nine macroops -- three register widths
# times register, memory and rip-relative source -- and nine more for its
# masked form, all differing only in a width and an element size. Written out
# they come to several hundred near-identical lines per instruction, where a
# transposed digit is invisible on review and shows up as a wrong lane at run
# time. These build them from one description instead.
#
# This file is not listed in any __init__.py's categories: it supplies text to
# the category modules rather than contributing microcode of its own.

# (EVEX.LL name, register prefix, load microop, memory operand size)
WIDTHS = [
    ("XMM", "xmm", "ldvec128", 16),
    ("YMM", "ymm", "ldvec256", 32),
    ("ZMM", "zmm", "ldvec512", 64),
]


def _widths(only):
    """
    The width rows to generate. Some instructions already have part of their
    set written out by hand; passing only=["XMM", "ZMM"] fills in the rest
    without defining a macroop twice.
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


def binop(name, microop, size, mask_microop=None, only=None, plain=True):
    """
    A vector instruction reading a register and a register or memory operand
    and writing a register: VPSUBW, VPMULLW, VPAVGB and most of their
    neighbours. size is the element size in bytes.

    plain=False emits only the masked forms, for an instruction whose
    unmasked macroops are already written out by hand.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext)
        for form, src, riprel in (("%sMM" % ext[0], "%sm" % reg, False),
                                  ("M", "uvec1", False),
                                  ("P", "uvec1", True)):
            # EVEX_VPSUBW_YMM_YMM_YMM, _YMM_YMM_M, _YMM_YMM_P
            stem = "%s_%s_%s_%s" % (name, ext, ext, form)
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)

            if plain:
                out.append(_macroop(stem, pre + [
                    "    %s %s1, %s2, %s, %s"
                    % (microop, reg, reg, src, tail)]))
            if mask_microop:
                out.append(_macroop(stem + "_K", pre + [
                    "    %s %s1, %s2, %s, %s1, opmask=opmask, %s"
                    % (mask_microop, reg, reg, src, reg, tail)]))
    return "".join(out)


def unop(name, microop, size, only=None):
    """
    A vector instruction reading one register or memory operand: VPABSB and
    friends. The destination symbol has no digit in this form.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext)
        for form, src, riprel in (("%sMM" % ext[0], "%sm" % reg, False),
                                  ("M", "uvec1", False),
                                  ("P", "uvec1", True)):
            # EVEX_VPABSB_YMM_YMM, _YMM_M, _YMM_P
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)
            out.append(_macroop("%s_%s_%s" % (name, ext, form), pre + [
                "    %s %s, %s, %s" % (microop, reg, src, tail)]))
    return "".join(out)


def shift_imm(name, microop, size, only=None):
    """
    A shift by an immediate: the count comes from the immediate byte and the
    operand being shifted is the register or memory source, so there is no
    second register operand. The microop name takes the assembler's 'i'
    suffix, which selects the immediate form of an op2-using microop.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext)
        for form, src, riprel in (("%sMM_I" % ext[0], "%sm" % reg, False),
                                  ("M_I", "uvec1", False),
                                  ("P_I", "uvec1", True)):
            # EVEX_VPSLLW_YMM_YMM_I, _YMM_M_I, _YMM_P_I
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)
            out.append(_macroop("%s_%s_%s" % (name, ext, form), pre + [
                "    %si %s1, %s, imm, %s" % (microop, reg, src, tail)]))
    return "".join(out)


def cmp_to_mask(name, microop, size, mask_microop=None, only=None):
    """
    A comparison writing a mask register: VPCMPGTB and friends. The
    destination is a mask register, so the macroop name carries K in its
    place.
    """
    out = []
    for ext, reg, load, width in _widths(only):
        tail = "size=%d, ext=%s" % (size, ext)
        for form, src, riprel in (("%sMM" % ext[0], "%sm" % reg, False),
                                  ("M", "uvec1", False),
                                  ("P", "uvec1", True)):
            # EVEX_VPCMPGTB_K_YMM_YMM, _K_YMM_M, _K_YMM_P
            stem = "%s_K_%s_%s" % (name, ext, form)
            pre = [] if src == "%sm" % reg else _load(load, width, riprel)

            out.append(_macroop(stem, pre + [
                "    %s k, %s2, %s, %s" % (microop, reg, src, tail)]))
            if mask_microop:
                out.append(_macroop(stem + "_K", pre + [
                    "    %s k, %s2, %s, opmask=opmask, %s"
                    % (mask_microop, reg, src, tail)]))
    return "".join(out)
