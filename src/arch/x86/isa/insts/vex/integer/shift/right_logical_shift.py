microcode = '''
def macroop VEX_SARX_R_R_R {
    sarx reg1, regm, reg2, size=dsz, ext="VEX_W"
};

def macroop VEX_SARX_R_M_R {
    ld t1, seg, sib, disp, dataSize="4 << VEX_W"
    sarx reg1, t1, reg2, size=dsz, ext="VEX_W"
};

def macroop VEX_SARX_R_P_R {
    rdip t7
    ld t1, seg, riprel, disp, dataSize="4 << VEX_W"
    sarx reg1, t1, reg2, size=dsz, ext="VEX_W"
};

def macroop VEX_SHRX_R_R_R {
    shrx reg1, regm, reg2, size=dsz, ext="VEX_W"
};

def macroop VEX_SHRX_R_M_R {
    ld t1, seg, sib, disp, dataSize="4 << VEX_W"
    shrx reg1, t1, reg2, size=dsz, ext="VEX_W"
};

def macroop VEX_SHRX_R_P_R {
    rdip t7
    ld t1, seg, riprel, disp, dataSize="4 << VEX_W"
    shrx reg1, t1, reg2, size=dsz, ext="VEX_W"
};

def macroop VEX_VPSRLD_XMM_XMM_XMM {
    gem5_avx_srl_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPSRLD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_srl_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSRLD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_srl_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSRLD_XMM_XMM_I {
    gem5_avx_srl_epu32_immi xmm, xmmm, imm, size=4, ext=XMM
};

def macroop VEX_VPSRLD_YMM_YMM_XMM {
    gem5_avx_srl_epu32 ymm1, ymm2, xmmm, size=4, ext=YMM
};

def macroop VEX_VPSRLD_YMM_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_srl_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSRLD_YMM_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_srl_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSRLD_YMM_YMM_I {
    gem5_avx_srl_epu32_immi ymm, ymmm, imm, size=4, ext=YMM
};

def macroop VEX_VPSRLQ_XMM_XMM_XMM {
    gem5_avx_srl_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VPSRLQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_srl_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPSRLQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_srl_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPSRLQ_XMM_XMM_I {
    gem5_avx_srl_epu64_immi xmm, xmmm, imm, size=8, ext=XMM
};

def macroop VEX_VPSRLQ_YMM_YMM_XMM {
    gem5_avx_srl_epu64 ymm1, ymm2, xmmm, size=8, ext=YMM
};

def macroop VEX_VPSRLQ_YMM_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_srl_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPSRLQ_YMM_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_srl_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPSRLQ_YMM_YMM_I {
    gem5_avx_srl_epu64_immi ymm, ymmm, imm, size=8, ext=YMM
};

def macroop VEX_VPSRLDQ_XMM_XMM_I {
    gem5_avx_bsrli_epu128i xmm, xmmm, imm, size=16, ext=XMM
};

def macroop VEX_VPSRLDQ_YMM_YMM_I {
    gem5_avx_bsrli_epu128i ymm, ymmm, imm, size=16, ext=YMM
};

def macroop VEX_VPALIGNR_XMM_XMM_XMM_I {
    gem5_avx_palignr_epi8 xmm1, xmm2, xmmm, size=1, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPALIGNR_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_palignr_epi8 xmm1, xmm2, uvec1, size=1, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPALIGNR_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_palignr_epi8 xmm1, xmm2, uvec1, size=1, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPALIGNR_YMM_YMM_YMM_I {
    gem5_avx_palignr_epi8 ymm1, ymm2, ymmm, size=1, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPALIGNR_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_palignr_epi8 ymm1, ymm2, uvec1, size=1, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPALIGNR_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_palignr_epi8 ymm1, ymm2, uvec1, size=1, ext="(IMMEDIATE & mask(8)) |" + YMM
};

'''

# The word shifts and the variable shifts. See macroop_gen.py.
from ...macroop_gen import binop, shift_imm, shift_imm_invalid_memory, \
        shift_count

microcode += shift_imm("VEX_VPSRLW", "gem5_avx_srl_epu16_imm", 2)
microcode += shift_count("VEX_VPSRLW", "gem5_avx_srl_epu16", 2)

# A memory source for a shift by an immediate is #UD; see
# shift_imm_invalid_memory. These three have their register forms written out
# above.
microcode += shift_imm_invalid_memory("VEX_VPSRLD")
microcode += shift_imm_invalid_memory("VEX_VPSRLQ")
microcode += shift_imm_invalid_memory("VEX_VPSRLDQ")

microcode += binop("VEX_VPSRLVD", "gem5_avx_srlv_epu32", 4)
microcode += binop("VEX_VPSRLVQ", "gem5_avx_srlv_epu64", 8)
