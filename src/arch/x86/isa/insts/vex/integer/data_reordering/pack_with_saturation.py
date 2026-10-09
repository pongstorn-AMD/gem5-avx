from ...macroop_gen import binop

microcode = ""

# The size given is the destination's element size: packing halves the
# element width.
microcode += binop("VEX_VPACKSSWB", "gem5_avx_packs_epi16", 1)
microcode += binop("VEX_VPACKUSWB", "gem5_avx_packus_epi16", 1)
microcode += binop("VEX_VPACKSSDW", "gem5_avx_packs_epi32", 2)
microcode += binop("VEX_VPACKUSDW", "gem5_avx_packus_epi32", 2)
