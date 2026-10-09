from ...macroop_gen import binop

microcode = '''
# AVX512BW pack with saturation
'''

microcode += binop("EVEX_VPACKUSWB", "gem5_avx_packus_epi16", 1)
