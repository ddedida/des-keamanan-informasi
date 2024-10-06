from table import keyp, shift_table, key_comp
from util import hex_to_bin, bin_to_hex, left_shift, permutation, encrypt

pt = "123456789ABCDEF1"
key = "AABBCCDDEEFF1122"

# Key Process
key = hex_to_bin(key)
key = permutation(key, keyp, 56)
left = key[0:28]
right = key[28:56]
rk = [] # Round Key
rkb = [] # Round Key Binary

for i in range(0, 16):
	# Left Shift
	left = left_shift(left, shift_table[i])
	right = left_shift(right, shift_table[i])

	# Combine
	combine_str = left + right

	# Compress to 48-bit
	round_key = permutation(combine_str, key_comp, 48)

	rkb.append(round_key)
	rk.append(bin_to_hex(round_key))

# Encryption
print("===== ENCRYPTION =====")
cipher_text = bin_to_hex(encrypt(pt, rkb, rk))
print("Cipher Text: ", cipher_text)
print("\n")

# Decryption
print("===== DECRYPTION =====")
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]
text = bin_to_hex(encrypt(cipher_text, rkb_rev, rk_rev))
print("Plain Text: ", text)