def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

# Get user input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

# Validate mode and perform operation
if mode in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift, mode)
    print(f"\n{mode.title()}ed message: {output}")
else:
    print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
