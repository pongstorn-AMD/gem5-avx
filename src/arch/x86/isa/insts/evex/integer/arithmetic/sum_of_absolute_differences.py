from ...macroop_gen import binop

microcode = '''
# AVX512BW sum of absolute differences
'''

# VPSADBW reduces eight byte lanes to one quadword, so its element size is
# that of the destination.
microcode += binop("EVEX_VPSADBW", "gem5_avx_sad_epu8", 8)
