alphabet = "abcdefghijklmnopqrstuvwxyz"

def Encrypt(text, index):
    text = text.lower()
    newText = ""

    for letter in text:
        currentIndex = alphabet.index(letter)
        newIndex = currentIndex + index

        if newIndex < 0:
            newIndex += 26
        elif newIndex > 25:
            newIndex -= 26

        newText += alphabet[newIndex]
    return newText

text = input("Enter text to encrypt:\n")
index = int(input("How far should I shift the letters?\n"))
encryptedText = Encrypt(text, index)
print(encryptedText)
