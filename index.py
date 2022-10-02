import numpy as np

Sbox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16,
]

Rcon = [
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
]

# Encrypt (): The main function that encrypts text with a key
def encrypt(plainText, key):

    blocks = divideIntoBlocks(plainText)
    roundKeys = getRoundKeys(key)
    cipherBlocks = []

    for block in blocks:
        _block = addRoundKey(roundKeys[0], block) # First round

        for i in range(9): # Intermediate rounds
            _block = subBytes(block)
            _block = shiftRows(block)
            _block = mixColumns(block)
            _block = addRoundKey(roundKeys[i], block)

        _block = subBytes(block)
        _block = shiftRows(block)
        _block = addRoundKey(roundKeys[9], block)

    # cipherText = reAssemble(blocks)
    return _block


"""
    divideIntoBlocks:  division of the input text into blocks of 128 bits (16 bytes). Each block is represented as a 4×4 matrix
"""
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


"""
    divideIntoBlocks() HELPER FUNCTIONS:
"""
def padText(text):
    for i in range(16):
        if (len(text)+i) % 16 == 0:
            return text+" "*i # add extra whitespace to make 16 bytes

def split_blocks(message):
        assert len(message) % 16 == 0
        return [message[i:i+16] for i in range(0, len(message), 16)]



"""
    getRoundKeys():  performs key deployment
"""
def getRoundKeys(key):

    key = divideIntoBlocks(key)
    key = key[0] # 128bit key
    
    assert len(key) * 8 in {128, 192, 256}

    Nk = {128: 4, 192: 6, 256: 8}[len(key) * 8] # length of the key words ( 4 bytes)
    
    Nr = {128: 11, 192: 13, 256: 15}[len(key) * 8] # number of rounds

    # the first 4 words of the expanded key
    W = [None for i in range(Nr * 4)]
    
    for i in range(Nk):
        W[i] = key[ i*4 : (i+1)*4] # string slicing 4 bytes each ( the bytes into words )

    
    for i in range(Nk, (4 * Nr)):
        temp = W[i-1] # previous word
    
        if i % Nk == 0:
            temp = list(subWord(rotWord(temp)))
            temp[0] = temp[0] ^ Rcon[i//Nk] # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
        elif Nk > 6 and i % Nk == 4:
            temp = subWord(temp)
        
        W[i] = xor_bytes(W[i-Nk], temp)

    theKeys = [W[i:i+4] for i in range(0, len(W), 4)]
    transposedKeys = []
    for key in theKeys:
        key = np.array(key).transpose()
        transposedKeys.append(key)


    return transposedKeys


"""
    getRoundKeys() HELPER FUNCTIONS:
"""
#takes from 1 to the end, adds on from the start to 1
def rotWord(word):
    return word[1:] + word[:1]


def xor_bytes(a, b):
    result = []
    for i in range(4):
        result.append(a[i] ^ b[i])
    return result

def subWord(word):
    #assert len(word) == 4
    return bytes(Sbox[b] for b in word)



def addRoundKey(roundKey, block):
    for i in range(4):
        for j in range(4):
            block[i][j] = xor_bytes(block[i][j], roundKey[i][j])
            
    return block


def addRoundKey(key, block):
    block = [block[i:i+4] for i in range(0, len(block), 4)]
    for i in range(4):
        for j in range(4):
            block[i][j] ^= key[i][j]
            
    return block
            


def subBytes(block):
    block = np.array(block)
    block = np.reshape(block, (4, 4)).transpose()
    #print(block)
    
    for i in range(4):
        for j in range(4):
            block[i][j] = Sbox[block[i][j]]
            
    return block



def shiftRows(s): # s for state
    
    s = np.array(s)
    s = np.reshape(s, (4, 4)).transpose()
    #print(s)
    
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
    
    return s




# learned from https://web.archive.org/web/20100626212235/http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # print(a)
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mixColumns(s):
    
    s = np.array(s)
    s = np.reshape(s, (4, 4)).transpose()
    
    for i in range(4):
        mix_single_column(s[i])
        
    return s

def reAssemble(blocks):
    return ""


cipherBlocks = encrypt("SampleTxtToCrypt", "SampleKeyToCrypt") # the final matrix after all transformations

cipher = np.array(cipherBlocks).transpose().reshape(-1)

cipherText = []
for k in cipher:
    cipherText.append(chr(k))

print("".join(cipherText)) # output the cipher text

