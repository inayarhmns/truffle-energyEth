encoded_hex = ("aa:3d:88:2e:93:8a:86:95:79:04:dc:ad:27:a4:6b:"
               "04:43:10:bd:67:2d:ba:57:41:d9:b6:1e:9f:54:2f:"
               "6c:6b")

# aa:3d:88:2e:93:8a:86:95:79:04:dc:ad:27:a4:6b:
#     04:43:10:bd:67:2d:ba:57:41:d9:b6:1e:9f:54:2f:
#     6c:6b
# Remove colons and concatenate
decoded_hex = ''.join(encoded_hex.split(':'))

# Convert to integer
private_num = int(decoded_hex, 16)

# Print in the form of 0x...
print(f"0x{private_num:x}")