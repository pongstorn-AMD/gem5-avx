from ...macroop_gen import binop

microcode = '''
# AVX512BW rounded average
'''

microcode += binop("EVEX_VPAVGB", "gem5_avx_avg_epu8", 1)
microcode += binop("EVEX_VPAVGW", "gem5_avx_avg_epu16", 2)
