CIPHERTEXT = "GEHDRSTAONLLRGYRVWRGWCNBQEOUSRSBUIQIQCCNVBCSA" + \
    "XVWTMVZJHGSARBASZYIRMAPGWWGNAQMGRGSWRMSTIEH" + \
    "KFIENOLHOHPGPYRCLWBODCSCUSUSEURUMQNCLEQJWJCOJ" + \
    "GGWVCWQYFNRRSCACRIPCRYXNJHPIFCOLHQJHYMAVCRMBW"
TARGET_WORD = "the"

CIPHERTEXT = CIPHERTEXT.lower()
TAEGET_WORD = TARGET_WORD.lower()

stringFrequencies = dict()

for i1 in range(len(CIPHERTEXT) - len(TAEGET_WORD) + 1):
    word = CIPHERTEXT[i1: i1 + len(TAEGET_WORD)]
    if word in stringFrequencies.keys():
        continue
    else:
        count = 1
        for i2 in range(i1 + 1, len(CIPHERTEXT) - len(TAEGET_WORD) + 1):
            if word == CIPHERTEXT[i2: i2 + len(TAEGET_WORD)]:
                count += 1
            else:
                continue
        if count == 1:
            continue
        else:
            stringFrequencies[word] = count

sortedList = sorted(stringFrequencies.items(), key=(lambda kv: kv[1]), reverse=True)
print(sortedList)

