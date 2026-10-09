microcode = '''
# gem5 has no notion of a non-temporal hint, so these are ordinary stores.
def macroop VEX_VMOVNTPS_M_XMM {
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVNTPS_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVNTPS_M_YMM {
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVNTPS_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop VEX_VMOVNTPD_M_XMM {
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVNTPD_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVNTPD_M_YMM {
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVNTPD_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

'''
