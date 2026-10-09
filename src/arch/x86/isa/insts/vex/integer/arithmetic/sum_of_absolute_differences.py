from ...macroop_gen import binop, binop_imm

microcode = ""

# VPSADBW sums the absolute byte differences of each 64-bit half into the
# low word of that half, so its element size is a word.
microcode += binop("VEX_VPSADBW", "gem5_avx_sad_epu8", 2)

# VMPSADBW takes the immediate in ext, three bits per 128-bit lane.
microcode += binop_imm("VEX_VMPSADBW", "gem5_avx_mpsadbw_epu8", 2)
