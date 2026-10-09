microcode = '''
def macroop VEX_VPADDD_XMM_XMM_XMM {
    gem5_avx_add_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPADDD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_add_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPADDD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_add_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPADDD_YMM_YMM_YMM {
    gem5_avx_add_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPADDD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_add_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPADDD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_add_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPADDQ_XMM_XMM_XMM {
    gem5_avx_add_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VPADDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_add_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPADDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_add_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPADDQ_YMM_YMM_YMM {
    gem5_avx_add_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VPADDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_add_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPADDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_add_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};
'''

# The byte and word adds, plain and saturating. See macroop_gen.py.
from ...macroop_gen import binop

microcode += binop("VEX_VPADDB", "gem5_avx_add_epu8", 1)
microcode += binop("VEX_VPADDW", "gem5_avx_add_epu16", 2)
microcode += binop("VEX_VPADDSB", "gem5_avx_adds_epi8", 1)
microcode += binop("VEX_VPADDSW", "gem5_avx_adds_epi16", 2)
microcode += binop("VEX_VPADDUSB", "gem5_avx_adds_epu8", 1)
microcode += binop("VEX_VPADDUSW", "gem5_avx_adds_epu16", 2)

# The horizontal adds, which pair up neighbours within each 128-bit lane.
microcode += binop("VEX_VPHADDW", "gem5_avx_hadd_epi16", 2)
microcode += binop("VEX_VPHADDSW", "gem5_avx_hadds_epi16", 2)
microcode += binop("VEX_VPHADDD", "gem5_avx_hadd_epi32", 4)
