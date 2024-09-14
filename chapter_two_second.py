def caesar_decrypt(ciphertext, shift):
    decrypted_message = []
    
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Adjust the base value for uppercase and lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            
            # Shift the character within its alphabet range
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)  # Leave non-alphabetic characters as they are
    
    return ''.join(decrypted_message)

# Example cryptogram
ciphertext = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNK..."

# Test decryption with different shift values
for shift in range(1, 26):
    decrypted_message = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_message}")