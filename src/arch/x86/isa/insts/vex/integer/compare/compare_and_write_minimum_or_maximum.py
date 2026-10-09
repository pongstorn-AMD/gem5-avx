microcode = '''
def macroop VEX_VPMINSD_XMM_XMM_XMM {
    gem5_avx_min_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPMINSD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPMINSD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPMINSD_YMM_YMM_YMM {
    gem5_avx_min_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPMINSD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPMINSD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPMINUB_XMM_XMM_XMM {
    gem5_avx_min_epu8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop VEX_VPMINUB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPMINUB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPMINUB_YMM_YMM_YMM {
    gem5_avx_min_epu8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop VEX_VPMINUB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPMINUB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPMAXSD_XMM_XMM_XMM {
    gem5_avx_max_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPMAXSD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_max_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPMAXSD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_max_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPMAXSD_YMM_YMM_YMM {
    gem5_avx_max_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPMAXSD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_max_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPMAXSD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_max_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};
'''

# The rest of the signedness and element size combinations. See macroop_gen.py.
from ...macroop_gen import binop, unop

microcode += binop("VEX_VPMINSB", "gem5_avx_min_epi8", 1)
microcode += binop("VEX_VPMAXSB", "gem5_avx_max_epi8", 1)
microcode += binop("VEX_VPMAXUB", "gem5_avx_max_epu8", 1)
microcode += binop("VEX_VPMINSW", "gem5_avx_min_epi16", 2)
microcode += binop("VEX_VPMAXSW", "gem5_avx_max_epi16", 2)
microcode += binop("VEX_VPMINUW", "gem5_avx_min_epu16", 2)
microcode += binop("VEX_VPMAXUW", "gem5_avx_max_epu16", 2)
microcode += binop("VEX_VPMINUD", "gem5_avx_min_epu32", 4)
microcode += binop("VEX_VPMAXUD", "gem5_avx_max_epu32", 4)

# VPHMINPOSUW is 128-bit only: it writes the smallest word of its source and
# that word's index into the low two words of the destination.
microcode += unop("VEX_VPHMINPOSUW", "gem5_avx_phminposuw", 2, only=["XMM"])
