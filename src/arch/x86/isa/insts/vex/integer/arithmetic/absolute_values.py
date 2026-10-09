from ...macroop_gen import unop

microcode = ""

microcode += unop("VEX_VPABSB", "gem5_avx_abs_epi8", 1)
microcode += unop("VEX_VPABSW", "gem5_avx_abs_epi16", 2)
microcode += unop("VEX_VPABSD", "gem5_avx_abs_epi32", 4)
