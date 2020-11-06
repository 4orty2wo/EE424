# -*- coding: utf-8 -*-
# Shift Cipher Implementation
# First, the alphabet used by plaintext and ciphertext
abet = 'abcdefghijklmnopqrstuvwxyz'
def enc_shift(k, plaintext):
    outciph = ''
    for ctr in plaintext.lower():
        try:
            i = (abet.index(ctr) + k) % 26
            outciph += abet[i]
        except ValueError:
            outciph += ctr
    return outciph.lower()
plaintext = 'Alice was beginning to get very tired of sitting by her sister'
ciphertext = enc_shift(3,plaintext)
print(ciphertext)

def dec_shift(k, ciphertext):
    plaintext = ''
    for ctr in ciphertext.lower():
        try:
            i = (abet.index(ctr) - k) % 26
            plaintext += abet[i]
        except ValueError:
            plaintext += ctr
    return plaintext.lower()
newText = dec_shift(3,ciphertext)
print(newText)