from ...macroop_gen import binop

microcode = ""

microcode += binop("VEX_VHSUBPS", "gem5_avx_hsub_ps", 4)
microcode += binop("VEX_VHSUBPD", "gem5_avx_hsub_pd", 8)
