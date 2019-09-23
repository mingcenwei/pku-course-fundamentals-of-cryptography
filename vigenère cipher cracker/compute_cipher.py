CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
PLAINTEXT = "cryptographyisanindispensabletoolusedtoprotec" + \
    "tinformationincomputingsystemsitisusedevery" + \
    "whereandbybillionsofpeopleworldwideonadailyba" + \
    "sisitisusedtoprotectdataatrestanddatainmotion"
CIPHER_LENGTH = 5

CIPHERTEXT = CIPHERTEXT.lower()
PLAINTEXT = PLAINTEXT.lower()

cipher = ""
for i in range(CIPHER_LENGTH):
    oc = ord(CIPHERTEXT[i])
    op = ord(PLAINTEXT[i])
    cipher += chr(ord("a") + (oc - op) % 26)

print(cipher)
