def encrypt(plainText, key):

    blocks = divideIntoBlocks(plainText)
    roundKeys = getRoundKeys(key)

    for block in blocks:
        addRoundKey(roundKeys[0], block) # First round

        for i in range(9): # Intermediate rounds
            subTypes(block)
            shiftRows(block)
            mixColumns(block)
            addRoundKey(roundKeys[i], block)

        subTypes(block)
        shiftRows(block)
        addRoundKey(roundKeys[9], block)

    cipherText = reAssemble(blocks)
    return cipherText


def divideIntoBlocks(text):
    return ""

def getRoundKeys(key):
    return ""

def addRoundKey(roundKey, block):
    return ""

def subTypes(block):
    return ""


def shiftRows(block):
    return ""

def mixColumns(block):
    return ""

def reAssemble(blocks):
    return