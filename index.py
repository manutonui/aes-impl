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

inv_Sbox = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
]

"""
=========================================================================================
=========================================================================================
=========================================================================================

Encrypt(string plaintext, string key)
Params: string plainText
        string key

"""


def encrypt(plainText, key):
    
    # Ensure Length is 16 bytes e.g 128 bits
    if  not len(plainText) == 16 and len(key) == 16:
        raise Exception("Ensure text and key length is 16")
    assert len(plainText) == 16 and len(key) == 16

    blocks = divideIntoBlocks(plainText)
    roundKeys = getRoundKeys(key)

    for block in blocks: # each block is 16bytes(128 bits)
        
        _block = np.reshape(np.array(block), (4,4)) # convert to 4x4 matrix
        _block = addRoundKey(roundKeys[0], _block) # First round

        for i in range(1, 10): # Intermediate rounds
            _block = subBytes(_block)
            _block = shiftRows(_block)
            _block = mixColumns(_block)
            _block = addRoundKey(roundKeys[i], _block)

        # last round
        _block = subBytes(_block)
        _block = shiftRows(_block)
        _block = addRoundKey(roundKeys[-1], _block)
        
    # ReAssemble the 128bit block
    cipher = np.array(_block).reshape(-1)
    encryptedText = "".join(format(x, '02x') for x in cipher)
    return encryptedText



"""
=========================================================================================
=========================================================================================
=========================================================================================

getRoundKeys(string key): 

KEY EXPANSION
- Takes the key string, and expands it to produce more keys that will be used in every round

params: string key
returns: array of expanded keys
    
"""
def getRoundKeys(key):
    
    assert len(key) * 8 in {128, 192, 256}

    
    Nk = {128: 4, 192: 6, 256: 8}[len(key) * 8] # length of the key in 4 byte words
    Nr = {128: 11, 192: 13, 256: 15}[len(key) * 8] # number of rounds
    Nb = 4 # no of bytes in a word - length of word
    
    key = toUnicode(key) # key to bytes

    # the expanded keys. E.g if Nr = 11, expanded keys should be same, etc
    W = [None for i in range(Nr * Nb)]
    
    # first round
    for i in range(Nk):
        W[i] = key[ i*Nb : (i+1)*Nb] # slicing
        
    
    # for other keys
    for i in range(Nk, (Nb * Nr)):
        temp = W[i-1] # previous word
    
        if i % Nk == 0: #
            temp = subWord(rotWord(temp))
            temp[0] ^= Rcon[i//Nk] # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
        elif Nk > 6 and i % Nk == 4:
            temp = subWord(temp)
        
        W[i] = xor_bytes(W[i-Nk], temp)
        
    # group into 4 - we have the expanded keys
    theKeys = [W[i:i+4] for i in range(0, len(W), 4)]
    return theKeys


"""
=========================================================================================
=========================================================================================

getRoundKeys()
    HELPER FUNCTIONS
"""

def rotWord(word):
    return word[1:] + word[:1]


def xor_bytes(a, b):
    result = []
    for i in range(4):
        result.append(a[i] ^ b[i])
    return result

def subWord(word):
    return [Sbox[w] for w in word]


"""
=========================================================================================
=========================================================================================
Encrypt()

    HELPER FUNCTIONS
"""
def addRoundKey(key, block):
    for i in range(4):
        for j in range(4):
            block[i][j] ^= key[i][j]
            
    return block            



def subBytes(block):
    for i in range(4):
        for j in range(4):
            block[i][j] = Sbox[block[i][j]]
            
    return block



def shiftRows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
    
    return s



# learned from https://web.archive.org/web/20100626212235/http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mixColumns(s):
    for i in range(4):
        mix_single_column(s[i])
        
    return s



"""
=========================================================================================
=========================================================================================
=========================================================================================

Decrypt(string cipherText, string key)
    - Takes a string of encrypted cipher text and the key that was used to encrypt it and performs the inverse transformations

"""

def decrypt(encryptedText, key):
    roundKeys = getRoundKeys(key)
    state = hex2ByteMatrix(encryptedText)
    
    state = addRoundKey(roundKeys[-1], state)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    
    for i in range(9,0,-1):
        state = addRoundKey(state, roundKeys[i])
        state = inv_mix_columns(state)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)

    state = addRoundKey(state, roundKeys[0])
    state = list(np.reshape(state, (-1)))
    text = [chr(b) for b in state]
    return "".join(text)
    
    
def inv_shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
    return s
    
    
def inv_sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = inv_Sbox[s[i][j]]
    return s
    
    
def inv_mix_columns(s):
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    return mixColumns(s)
    

# converts hex string back to unicode int representation
def hex2ByteMatrix(hexStr):
    hexArr = split_blocks(hexStr, 2)
    stateArr = []
    for hs in hexArr:
        stateArr.append(int(hs, 16)) # hex to int
        
    state = np.reshape(np.array(stateArr), (4,4))
    return state



"""
=========================================================================================
=========================================================================================
=========================================================================================
Helper Functions


=========================================================================================
divideIntoBlocks()
    division of the input text into blocks of 128 bits (16 bytes)
    
params: string text
returns: array of bytes in int representation (unicode)

"""

def divideIntoBlocks(text):

    blocks = split_blocks(text) # splits into 16-byte blocks
    
    byteBlocks = []
    for block in blocks:
        matrix = toUnicode(block)
        byteBlocks.append(matrix)
        
    return byteBlocks


"""
=========================================================================================
=========================================================================================
    divideIntoBlocks() HELPER FUNCTIONS:
"""

def split_blocks(message, size=16):
        assert len(message) % size == 0
        return [message[i:i+size] for i in range(0, len(message), size)]

# takes a string(block) of characters and return the array of unicode
def toUnicode(block):
    byteArr = []
    for b in block:
        byteArr.append(ord(b))
    return byteArr


# Test Functions
txt = "SampleTxtToCrypt"
key = "SampleKeyToKrypt"
encryptedTxt = encrypt(txt, key)
print("Encrypted Text = " + encryptedTxt)

decryptedTxt = decrypt(encryptedTxt, key)
print("Decrypted Text = " + decryptedTxt)