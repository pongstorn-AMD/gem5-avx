from ...macroop_gen import unop

microcode = '''
# AVX512 absolute value
'''

microcode += unop("EVEX_VPABSB", "gem5_avx_abs_epi8", 1)
microcode += unop("EVEX_VPABSW", "gem5_avx_abs_epi16", 2)
microcode += unop("EVEX_VPABSD", "gem5_avx_abs_epi32", 4)
microcode += unop("EVEX_VPABSQ", "gem5_avx_abs_epi64", 8)
