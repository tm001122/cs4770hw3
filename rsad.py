def rsa_decrypt_byte(encrypted_byte, d, n):
    """Decrypts a single byte using RSA."""
    return pow(encrypted_byte, d, n)

def rsa_decrypt_string_from_input(hex_string, d, n):
    """Decrypts the space-separated hex values provided as input."""
    decrypted_chars = []

    # Split the hex string by spaces to get individual hex values
    hex_values = hex_string.split()

    # Process each hex value and decrypt
    for hex_value in hex_values:
        encrypted_byte = int(hex_value, 16)  # Convert the hex value to an integer
        decrypted_byte = rsa_decrypt_byte(encrypted_byte, d, n)  # Decrypt the byte
        decrypted_chars.append(chr(decrypted_byte))  # Convert to char and append to result list

    return ''.join(decrypted_chars)  # Join the decrypted characters into a string

def main():
    # Prompt for the hex-encoded ciphertext
    sys.stderr.write("Enter hex-encoded ciphertext: ")
    hex_string = input().strip()
    
    # Prompt for the private key
    sys.stderr.write("Enter private key (d, n) separated by a space: ")
    d, n = map(int, input().strip().split())

    # Decrypt the string from the input
    decrypted_string = rsa_decrypt_string_from_input(hex_string, d, n)

    # Output the decrypted string to stdout
    print(decrypted_string)

if __name__ == "__main__":
    import sys
    main()
