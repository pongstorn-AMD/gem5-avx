from ...macroop_gen import binop

microcode = ""

# VPSIGN negates, zeroes or keeps each element of the first source according
# to the sign of the matching element of the second.
microcode += binop("VEX_VPSIGNB", "gem5_avx_sign_epi8", 1)
microcode += binop("VEX_VPSIGNW", "gem5_avx_sign_epi16", 2)
microcode += binop("VEX_VPSIGND", "gem5_avx_sign_epi32", 4)
