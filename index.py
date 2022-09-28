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


# TASK 1: divide input text into blocks of 16 bytes
def divideIntoBlocks(text):

    if len(text) % 16 != 0:
        text = padText(text) # Text padded

    # Division of text to 16 bytes blocks
    blocks = split_blocks(text)

    byteBlocks = [] # Array of blocks of 16 bytes each
    for block in blocks:
        matrix = [] # one block of 16 bytes
        for i in block:
            matrix.append(ord(i)) # convert characters to byte values
        byteBlocks.append(matrix)

    return byteBlocks

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


# Helper functions
def padText(text):
    for i in range(16):
        if (len(text)+i) % 16 == 0:
            return text+" "*i # add extra whitespace to make 16 bytes

def split_blocks(message):
        assert len(message) % 16 == 0
        return [message[i:i+16] for i in range(0, len(message), 16)]