import math
from Alpabet_constants import *
from pprint import pprint


# there will be encryption methods

# encryption with Vigenere method of in_str with key (string)
# return encrypted string
def encrypt_Vigenere(in_str, key):
    if key == '':
        return None
    key_ind = 0
    enc_str = ''
    for let in in_str:
        if key_ind == len(key):
            key_ind = 0

        if let in RU_LETTERS:
            enc_str += RU_LETTERS[(RU_LETTERS.index(let) + RU_LETTERS.index(key[key_ind])) % ru_alp_len]
            key_ind += 1
        else:
            enc_str += let

    return enc_str.upper()


# encryption with Decimatiy method of in_str with key (integer)
# return encrypted string
# TODO: check key to gcd(key, en_alp_len) != 1 and do not encrypting
def encrypt_Decimatiy(in_str, key):
    if math.gcd(key, en_alp_len) != 1:
        return None
    enc_str = ''
    for let in in_str:
        if let in EN_LETTERS:
            enc_str += EN_LETTERS[(EN_LETTERS.index(let) * key) % en_alp_len]
        else:
            enc_str += let

    return enc_str.upper()

# Start columns cipher
# finding index of element in the list depends on visited state
def find_index(sorted_key_arr, visited_arr, symbol):
    for i in range(len(sorted_key_arr)):
        if (sorted_key_arr[i] == symbol) and (not visited_arr[i]):
            visited_arr[i] = True
            return i, visited_arr

    return None, visited_arr

# Generating array of key
def gen_key_arr(key):
    key_arr = [list(key), [''] * len(key)]
    visited_arr = [False] * len(key)

    let_key_sorted_arr = list(key)
    let_key_sorted_arr.sort()

    let_ind = 0
    for let in key_arr[0]:
        #sort_ind = let_key_sorted_arr.index(let)
        sort_ind, visited_arr = find_index(let_key_sorted_arr, visited_arr, let)
        # filling list with position of symbol
        key_arr[1][let_ind] = str(sort_ind + 1)
        let_ind += 1

    pprint(key_arr)
    return key_arr


# generating array of in_str
def gen_instr_arr(in_str, key_arr):
    instr_arr = [[''] * len(key_arr[0])]

    ind_of_key_letter = 0 # index of letter in key letter with current letter
    instr_ind = 0
    instr_arr_ind = 0
    # iterating throw the in_str
    while instr_ind < len(in_str):
        # finding max index of filling in_str on the current row of matrix
        border_ind_of_key_letter = int(key_arr[1].index(str(ind_of_key_letter+1)))
        # filling in_str to this row
        for ind in range(border_ind_of_key_letter+1):
            instr_arr[instr_arr_ind][ind] = in_str[instr_ind]
            instr_ind += 1
            if instr_ind >= len(in_str):
                break
        # adding new row
        instr_arr.append([''] * len(key_arr[0]))
        instr_arr_ind += 1
        ind_of_key_letter += 1
        # refresh the value
        if ind_of_key_letter == len(key_arr[0]):
            ind_of_key_letter = 0

    pprint(instr_arr)
    return instr_arr


# encryption with upgraded columns method of in_str with key (string)
# return encrypted string
def encrypt_columns_cipher(in_str, key):
    key_arr = gen_key_arr(key)
    instr_arr = gen_instr_arr(in_str, key_arr)

    enc_str = ''
    for ind in range(len(key_arr[0])):
        col_ind = int(key_arr[1].index(str(ind+1)))
        for row_ind in range(len(instr_arr)):
            enc_str += instr_arr[row_ind][col_ind]

    #print(enc_str)
    return enc_str.upper()


#keyarr = gen_key_arr("bcad")
#gen_instr_arr('hello world is me', keyarr)