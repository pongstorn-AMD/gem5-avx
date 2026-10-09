microcode = '''
def macroop VEX_VPMOVSXDQ_XMM_XMM {
    gem5_avx_cvtepi32_epi64 xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVSXDQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVSXDQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVSXDQ_YMM_XMM {
    gem5_avx_cvtepi32_epi64 ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVSXDQ_YMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVSXDQ_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVZXDQ_XMM_XMM {
    gem5_avx_cvtepu32_epi64 xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVZXDQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVZXDQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VPMOVZXDQ_YMM_XMM {
    gem5_avx_cvtepu32_epi64 ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVZXDQ_YMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VPMOVZXDQ_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_epi64 ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

'''

# The rest of the extending moves. See macroop_gen.py.
from ...macroop_gen import widen

microcode += widen("VEX_VPMOVSXBW", "gem5_avx_cvtepi8_epi16", 1, 2)
microcode += widen("VEX_VPMOVSXBD", "gem5_avx_cvtepi8_epi32", 1, 4)
microcode += widen("VEX_VPMOVSXBQ", "gem5_avx_cvtepi8_epi64", 1, 8)
microcode += widen("VEX_VPMOVSXWD", "gem5_avx_cvtepi16_epi32", 2, 4)
microcode += widen("VEX_VPMOVSXWQ", "gem5_avx_cvtepi16_epi64", 2, 8)
microcode += widen("VEX_VPMOVZXBW", "gem5_avx_cvtepu8_epi16", 1, 2)
microcode += widen("VEX_VPMOVZXBD", "gem5_avx_cvtepu8_epi32", 1, 4)
microcode += widen("VEX_VPMOVZXBQ", "gem5_avx_cvtepu8_epi64", 1, 8)
microcode += widen("VEX_VPMOVZXWD", "gem5_avx_cvtepu16_epi32", 2, 4)
microcode += widen("VEX_VPMOVZXWQ", "gem5_avx_cvtepu16_epi64", 2, 8)
