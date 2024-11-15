import sys

def rsa_encrypt_byte(byte, e, n):
    """Encrypts a single byte using RSA."""
    return pow(byte, e, n)

def rsa_encrypt_string(input_string, e, n):
    """Encrypts an ASCII string one byte at a time using RSA encryption."""
    encrypted_bytes = []
    for char in input_string:
        byte_value = ord(char)
        encrypted_byte = rsa_encrypt_byte(byte_value, e, n)
        encrypted_bytes.append(encrypted_byte)
    return encrypted_bytes

def main():
    # Read the input ASCII string from stdin
    sys.stderr.write("Enter ASCII string to encrypt: ")
    input_string = input().strip()
    
    # Read e and n from stdin
    sys.stderr.write("Enter public key (e, n) separated by a space: ")
    e, n = map(int, input().strip().split())

    # Encrypt the input string
    encrypted_bytes = rsa_encrypt_string(input_string, e, n)

    # Write the encrypted bytes as hex to standard output
    encrypted_hex = ' '.join(format(byte, 'x') for byte in encrypted_bytes)
    print(encrypted_hex)

if __name__ == "__main__":
    main()
