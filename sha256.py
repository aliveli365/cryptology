import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

while True:
	hash_string = input("Data to sha256:")
	sha_signature = encrypt_string(hash_string)
	print(sha_signature)

