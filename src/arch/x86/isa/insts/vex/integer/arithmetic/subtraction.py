microcode = '''
def macroop VEX_VPSUBB_XMM_XMM_XMM {
    gem5_avx_sub_epu8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop VEX_VPSUBB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPSUBB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPSUBB_YMM_YMM_YMM {
    gem5_avx_sub_epu8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop VEX_VPSUBB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPSUBB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPSUBD_XMM_XMM_XMM {
    gem5_avx_sub_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPSUBD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSUBD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSUBD_YMM_YMM_YMM {
    gem5_avx_sub_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPSUBD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSUBD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSUBQ_XMM_XMM_XMM {
    gem5_avx_sub_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VPSUBQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPSUBQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPSUBQ_YMM_YMM_YMM {
    gem5_avx_sub_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VPSUBQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPSUBQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};
'''

# The byte and word subtracts, plain and saturating. See macroop_gen.py.
from ...macroop_gen import binop

microcode += binop("VEX_VPSUBW", "gem5_avx_sub_epu16", 2)
microcode += binop("VEX_VPSUBSB", "gem5_avx_subs_epi8", 1)
microcode += binop("VEX_VPSUBSW", "gem5_avx_subs_epi16", 2)
microcode += binop("VEX_VPSUBUSB", "gem5_avx_subs_epu8", 1)
microcode += binop("VEX_VPSUBUSW", "gem5_avx_subs_epu16", 2)

# The horizontal subtracts.
microcode += binop("VEX_VPHSUBW", "gem5_avx_hsub_epi16", 2)
microcode += binop("VEX_VPHSUBSW", "gem5_avx_hsubs_epi16", 2)
microcode += binop("VEX_VPHSUBD", "gem5_avx_hsub_epi32", 4)
