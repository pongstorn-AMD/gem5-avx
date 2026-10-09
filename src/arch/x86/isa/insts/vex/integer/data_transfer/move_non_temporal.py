microcode = '''
# gem5 has no notion of a non-temporal hint, so these are ordinary moves.
def macroop VEX_VMOVNTDQ_M_XMM {
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVNTDQ_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVNTDQ_M_YMM {
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVNTDQ_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop VEX_VMOVNTDQA_XMM_M {
    ldvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVNTDQA_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVNTDQA_YMM_M {
    ldvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVNTDQA_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, disp, dataSize=32
};

# VLDDQU is an unaligned load; gem5 does not model the split it is allowed
# to do, so it is VMOVDQU.
def macroop VEX_VLDDQU_XMM_M {
    ldvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VLDDQU_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VLDDQU_YMM_M {
    ldvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VLDDQU_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, disp, dataSize=32
};

# VMASKMOVDQU writes the bytes of its first source whose mask byte in the
# second has its top bit set, to DS:rDI. Reading the line first and writing
# it all back is how MASKMOVQ models the same thing.
def macroop VEX_VMASKMOVDQU_XMM_XMM {
    ldvec128 uvec1, ds, [1, t0, rdi], dataSize=16
    gem5_avx_maskmove_epi8 uvec1, xmmm, xmm, uvec1, size=1, ext=XMM + "| 1"
    stvec128 uvec1, ds, [1, t0, rdi], dataSize=16
};

'''
