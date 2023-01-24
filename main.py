from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Define the plaintext message
message = b'flag{ISEP 2023 easy challenge}'

# Define the key and IV
key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'
iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

# Pad the plaintext message
block_size = 16
padded_message = pad(message, block_size)

# Create the AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the padded plaintext
ciphertext = cipher.encrypt(padded_message)

# Write the ciphertext to a file
with open("ciphertext.bin", "wb") as f:
    f.write(ciphertext)

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