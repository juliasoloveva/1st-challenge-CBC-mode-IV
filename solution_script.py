from Crypto.Cipher import AES

# Read the ciphertext and the key from the file
with open("ciphertext.bin", "rb") as f:
    ciphertext = f.read()
key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'

# Define the known IV
iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

# Decrypt the ciphertext
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# Check if the plaintext starts with "flag"
if plaintext.startswith(b"flag"):
    print("Flag:", plaintext.decode())
else:
    print("Plaintext:", plaintext.decode())
