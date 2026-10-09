microcode = '''
def macroop EVEX_VCVTSS2SD_XMM_XMM_XMM {
    gem5_avx_cvtss_sd xmm1, xmm2, xmmm, destSize=8, srcSize=4, ext=0
};

def macroop EVEX_VCVTSS2SD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_cvtss_sd xmm1, xmm2, uvec1, destSize=8, srcSize=4, ext=0
};

def macroop EVEX_VCVTSS2SD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_cvtss_sd xmm1, xmm2, uvec1, destSize=8, srcSize=4, ext=0
};

def macroop EVEX_VCVTSD2SS_XMM_XMM_XMM {
    gem5_avx_cvtsd_ss xmm1, xmm2, xmmm, destSize=4, srcSize=8, ext=Scalar
};

def macroop EVEX_VCVTSD2SS_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_cvtsd_ss xmm1, xmm2, uvec1, destSize=4, srcSize=8, ext=Scalar
};

def macroop EVEX_VCVTSD2SS_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_cvtsd_ss xmm1, xmm2, uvec1, destSize=4, srcSize=8, ext=Scalar
};

def macroop EVEX_VGETMANTPD_XMM_XMM_I {
    gem5_avx_getmant_pdi xmm, xmmm, imm, size=8, ext=XMM
};

def macroop EVEX_VGETMANTPD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_getmant_pdi xmm, uvec1, imm, size=8, ext=XMM
};

def macroop EVEX_VGETMANTPD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_getmant_pdi xmm, uvec1, imm, size=8, ext=XMM
};

def macroop EVEX_VGETMANTPD_YMM_YMM_I {
    gem5_avx_getmant_pdi ymm, ymmm, imm, size=8, ext=YMM
};

def macroop EVEX_VGETMANTPD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_getmant_pdi ymm, uvec1, imm, size=8, ext=YMM
};

def macroop EVEX_VGETMANTPD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_getmant_pdi ymm, uvec1, imm, size=8, ext=YMM
};

def macroop EVEX_VGETMANTPD_ZMM_ZMM_I {
    gem5_avx_getmant_pdi zmm, zmmm, imm, size=8, ext=ZMM
};

def macroop EVEX_VGETMANTPD_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_getmant_pdi zmm, uvec1, imm, size=8, ext=ZMM
};

def macroop EVEX_VGETMANTPD_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_getmant_pdi zmm, uvec1, imm, size=8, ext=ZMM
};

def macroop EVEX_VGETEXPPD_XMM_XMM {
    gem5_avx_getexp_pd xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VGETEXPPD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_getexp_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VGETEXPPD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_getexp_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VGETEXPPD_YMM_YMM {
    gem5_avx_getexp_pd ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VGETEXPPD_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_getexp_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VGETEXPPD_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_getexp_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VGETEXPPD_ZMM_ZMM {
    gem5_avx_getexp_pd zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VGETEXPPD_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_getexp_pd zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VGETEXPPD_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_getexp_pd zmm, uvec1, size=8, ext=ZMM
};

# VCVTPS2PD widens, so its source is half the width of its destination and
# the memory forms load half as much.
def macroop EVEX_VCVTPS2PD_XMM_XMM {
    gem5_avx_cvt_ps2pd xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTPS2PD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvt_ps2pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTPS2PD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvt_ps2pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTPS2PD_YMM_XMM {
    gem5_avx_cvt_ps2pd ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTPS2PD_YMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvt_ps2pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTPS2PD_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvt_ps2pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTPS2PD_ZMM_YMM {
    gem5_avx_cvt_ps2pd zmm, ymmm, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VCVTPS2PD_ZMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvt_ps2pd zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VCVTPS2PD_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvt_ps2pd zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

'''
