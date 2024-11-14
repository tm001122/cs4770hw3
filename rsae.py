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

def write_encrypted_to_file_as_hex(encrypted_bytes, filename):
    """Writes encrypted bytes to a file in hex format, ensuring ASCII compatibility."""
    with open(filename, 'w') as file:
        for encrypted_byte in encrypted_bytes:
            hex_value = format(encrypted_byte, 'x')  # Convert to hex
            file.write(f"{hex_value} ")

def main():
    # Read the input ASCII string from stdin
    input_string = input("Enter ASCII string to encrypt: ")
    # Read e and n from stdin
    e, n = map(int, input("Enter public key (e, n) separated by a space: ").split())

    # Encrypt the input string
    encrypted_bytes = rsa_encrypt_string(input_string, e, n)

    # Specify the output file name
    output_filename = "encrypted_output.txt"
    write_encrypted_to_file_as_hex(encrypted_bytes, output_filename)

    print(f"Encrypted bytes written to {output_filename} in hex format")

if __name__ == "__main__":
    main()
