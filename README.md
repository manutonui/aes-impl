# aes-impl
## Imlpementation of the AES Encryption Algorithm
The AES algorithm is a symmetric encryption that encrypts plain text using a key. Varoius transformations are carried out to the plaintext using the key to produce cipher text, which can then be decrypted using the key only.

### The Encrypt function
Takes a block of text(*At the moment, I only use 128 bits for both plaintext and key. This will change in later revisions*) and takes it through a transformation with each roundKey. Round Keys are expanded so that each round transforms a block with a separate key.
Below is the list of transformations:
- addRoundKey() - computes XOR of block and roundKey 
- substituteBytes() - substitute bytes from the sbox table
- shiftRows()
- mixColumns()

### The Decrypt function
Takes a string of encrypted Text and the key that was used to encrypt it and performs inverse transformations to output the original plaintext
List of transformations:
- inverse substitute bytes() - substitutes bytes from the inverse sbox
- inverse shift rows()
- inverse mix columns()
- addRoundKey() is its own inverse


**[Official AES documentation]**(https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.197.pdf)