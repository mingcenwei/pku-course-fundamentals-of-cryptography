CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
TARGET_WORD = "the"
ENCRYPTED_STRING = "olh"
CIPHER_LENGTH = 5

CIPHERTEXT = CIPHERTEXT.lower()
TAEGET_WORD = TARGET_WORD.lower()
ENCRYPTED_STRING = ENCRYPTED_STRING.lower()

forwardShifts = [(ord(ENCRYPTED_STRING[i]) - ord(TAEGET_WORD[i])) % 26 for i in range(len(TAEGET_WORD))]
encyptedStringIndex = CIPHERTEXT.find(ENCRYPTED_STRING)
partiallyDecryptedString = ""
for i in range(len(CIPHERTEXT)):
    offset = (i - encyptedStringIndex) % CIPHER_LENGTH
    if offset < len(TARGET_WORD):
        o1 = ord(CIPHERTEXT[i]) - forwardShifts[offset]
        decryptedChar = chr(o1) if o1 >= ord("a") else chr(o1 + 26)
        partiallyDecryptedString += decryptedChar
    else:
        partiallyDecryptedString += chr(ord(CIPHERTEXT[i]) + ord("A") - ord("a"))
print(partiallyDecryptedString)