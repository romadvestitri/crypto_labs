from Alpabet_constants import *
import math
# there will be functions to check keys and delete unnecessary symbols

# editing key for Vinigere cipher, deleting unnecessary symbols
# (symbol that are not in the russian alphabet)
def edit_key_for_Venigere(key):
    new_key = ''
    for let in key:
        if let in RU_LETTERS:
            new_key += let

    return new_key

# editing key for Decinatiy cipher, deleting letter (only numbers are ok)
def edit_key_for_Decimatiy(key):
    nums = '0123456789'
    new_key = ''
    for let in key:
        if let in nums:
            new_key += let

    if new_key != '':
        int_new_key = int(new_key)
        if math.gcd(int_new_key, en_alp_len) != 1:
            return None
        return int_new_key
    else:
        return None

# editing key for upgraded column cipher, deleting unnecessary symbols
# (symbol that are not in the english alphabet)
def edit_key_column_cipher(key):
    new_key = ''
    for let in key:
        if let in EN_LETTERS:
            new_key += let

    return new_key

def edit_instr_column_cipher(in_str):
    new_instr = ''
    for let in in_str:
        if let in EN_LETTERS:
            new_instr += let

    return new_instr