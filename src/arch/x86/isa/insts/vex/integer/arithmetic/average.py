from ...macroop_gen import binop

microcode = ""

microcode += binop("VEX_VPAVGB", "gem5_avx_avg_epu8", 1)
microcode += binop("VEX_VPAVGW", "gem5_avx_avg_epu16", 2)
