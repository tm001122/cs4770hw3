def rsa_decrypt_byte(encrypted_byte, d, n):
    """Decrypts a single byte using RSA."""
    return pow(encrypted_byte, d, n)

def rsa_decrypt_string_from_file(filename, d, n):
    """Reads the encrypted hex values from a file, decrypts them, and returns the decrypted string."""
    decrypted_chars = []

    with open(filename, 'r') as file:
        # Read the single line containing space-separated hex values
        line = file.readline().strip()

        # Split the line by space to get individual hex values
        hex_values = line.split()

        # Process each hex value and decrypt
        for hex_value in hex_values:
            encrypted_byte = int(hex_value, 16)  # Convert the hex value to an integer
            decrypted_byte = rsa_decrypt_byte(encrypted_byte, d, n)  # Decrypt the byte
            decrypted_chars.append(chr(decrypted_byte))  # Convert to char and append to result list

    return ''.join(decrypted_chars)  # Join the decrypted characters into a string

def main():
    # Specify the input file name
    input_filename = "encrypted_output.txt"
    
    # Read d and n from stdin
    d, n = map(int, input("Enter private key (d, n) separated by a space: ").split())

    # Decrypt the string from the file
    decrypted_string = rsa_decrypt_string_from_file(input_filename, d, n)

    print("Decrypted string:", decrypted_string)

if __name__ == "__main__":
    main()
