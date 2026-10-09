from ...macroop_gen import unop

microcode = unop("VEX_VRSQRTPS", "gem5_avx_rsqrt14_ps", 4)

# The scalar form keeps the upper lanes of its first source, so unlike the
# packed form it reads two registers.
microcode += '''
def macroop VEX_VRSQRTSS_XMM_XMM_XMM {
    gem5_avx_rsqrt14_ss xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VRSQRTSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_rsqrt14_ss xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VRSQRTSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_rsqrt14_ss xmm1, xmm2, uvec1, size=4, ext=Scalar
};

'''
