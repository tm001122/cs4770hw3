import math
import sys

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

def find_private_key(e, n):
    """Finds the private key d given public key e and modulus n."""
    # Step 1: Factor n into p and q
    p, q = find_factors(n)
    
    # Step 2: Compute φ(n) = (p - 1)(q - 1)
    phi_n = (p - 1) * (q - 1)
    
    # Step 3: Compute the modular inverse of e mod φ(n) to get d
    d = mod_inverse(e, phi_n)
    
    return d

def find_factors(n):
    """Finds the factors of n."""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = i
            q = n // i
            return p, q
    return None, None

def mod_inverse(a, m):
    """Returns the modular inverse of a mod m using the Extended Euclidean Algorithm."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def main():
    # Prompt for the hex-encoded ciphertext
    sys.stderr.write("Enter hex-encoded ciphertext: ")
    hex_string = input().strip()
    
    # Prompt for the public key
    sys.stderr.write("Enter public key (e, n) separated by a space: ")
    e, n = map(int, input().strip().split())

    # Step 1: Find private key d using the public key (e, n)
    d = find_private_key(e, n)

    # Step 2: Decrypt the string from the input
    decrypted_string = rsa_decrypt_string_from_input(hex_string, d, n)

    # Output the decrypted string to stdout
    print(decrypted_string)

if __name__ == "__main__":
    main()
