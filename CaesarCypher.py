def encrypt(shift, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encr_alph = []


    # Creating encrypted alphabet
    for i in range(shift, len(alphabet)):
        encr_alph.append(alphabet[i])
    for i in range(0,shift):
        encr_alph.append(alphabet[i])

    # Encrypting message:
    message = message.lower()
    encr_message = ""
    for i in message:
        if not i == " ":
            charIndex = alphabet.find(i)
            encr_message = encr_message + encr_alph[charIndex]
        else:
            encr_message = encr_message + " "
    return encr_message


def main():
    while True:
        shift = input("Input desired shift to encrypt your message (1 - 25): ")
        if 0 < int(shift) < 26:
            break
        else:
            print("Invalid input!")
    message = input("Enter message to encrypt: ")
    encrypted = encrypt(int(shift), message)
    print(f"Encrypted message: {encrypted}")


if __name__ == '__main__':
    main()

