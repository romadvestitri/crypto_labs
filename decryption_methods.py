import math
from Alpabet_constants import *
from pprint import pprint


# there will be decryption methods

# decryption with Vigenere method of enc_str with key (string)
# return initial string
def decrypt_Vigenere(enc_str, key):
    if key == '':
        return None
    key_ind = 0
    in_str = ''

    for let in enc_str:
        if key_ind == len(key):
            key_ind = 0

        if let in RU_LETTERS:
            in_str += RU_LETTERS[(RU_LETTERS.index(let) - RU_LETTERS.index(key[key_ind])) % ru_alp_len]
            key_ind += 1
        else:
            in_str += let

    return in_str.upper()


# Extended Euclid algo to find mod inverse number
def findModInverse(a, n):
    if math.gcd(a, n) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, n

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % n


# decryption with Decimatiy method of enc_str with key (integer)
# return initial string
def encrypt_Decimatiy(enc_str, key):
    if math.gcd(key, en_alp_len) != 1:
        return None
    in_str = ''
    for let in enc_str:
        if let in EN_LETTERS:
            in_str += EN_LETTERS[(EN_LETTERS.index(let) * findModInverse(key, en_alp_len)) % en_alp_len]
        else:
            in_str += let

    return in_str.upper()


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
        sort_ind, visited_arr = find_index(let_key_sorted_arr, visited_arr, let)
        # filling list with position of symbol
        key_arr[1][let_ind] = str(sort_ind + 1)
        let_ind += 1

    # pprint(key_arr)
    return key_arr


# finding sum of numbers form 1 to n
def find_sum_of_nums(n):
    res = 0
    for i in range(1, n + 1):
        res += i

    return res

# finding size of array to enc_str
# return array
def find_size_of_arr(enc_str, key_arr):
    key_size = len(key_arr[0])
    max_capacity_of_part_arr = find_sum_of_nums(key_size)
    arr_col_size = math.ceil(len(enc_str) / max_capacity_of_part_arr) * key_size
    max_capacity_of_arr = arr_col_size // key_size * max_capacity_of_part_arr
    while max_capacity_of_arr >= len(enc_str):
        if arr_col_size % key_size == 0:
            mod_num = key_size
        else:
            mod_num = arr_col_size % key_size
        max_capacity_of_arr -= (key_arr[1].index(str(mod_num)) + 1)
        arr_col_size -= 1

    arr_col_size += 1
    encstr_arr = [[''] * key_size]
    for _ in range(arr_col_size - 1):
        encstr_arr.append([''] * key_size)

    return encstr_arr

# generating array of in_str
def gen_encstr_arr(enc_str, key_arr):
    encstr_arr = find_size_of_arr(enc_str, key_arr)

    # iterating throw columns in array
    str_ind = 0
    col_count = len(encstr_arr[0])
    row_count = len(encstr_arr)
    for col_num in range(1, col_count + 1):
        # index of current col_ind in the column
        current_col_index = key_arr[1].index(str(col_num))
        col_ind = 1
        num_fill_let = 0
        for row_num in range(row_count):
            # index of col_ind on the current row
            tmp_col_ind = key_arr[1].index(str(col_ind))
            # num of fill letters from string
            num_fill_let += tmp_col_ind + 1
            if current_col_index <= tmp_col_ind and str_ind < len(enc_str):
                if not (row_num == row_count - 1 and (
                        num_fill_let - (tmp_col_ind - current_col_index) > len(enc_str))):
                    encstr_arr[row_num][current_col_index] = enc_str[str_ind]
                    str_ind += 1

            col_ind += 1
            if col_ind >= len(encstr_arr[0]) + 1:
                col_ind = 1

    #pprint(encstr_arr)
    return encstr_arr


# decryption with upgraded columns method of in_str with key (string)
# return encrypted string
def decrypt_columns_cipher(enc_str, key):
    key_arr = gen_key_arr(key)
    encstr_arr = gen_encstr_arr(enc_str, key_arr)

    col_count = len(encstr_arr[0])
    row_count = len(encstr_arr)
    in_str = ''
    for row in range(row_count):
        for col in range(col_count):
            in_str += encstr_arr[row][col]

    # print(dec_str)
    return in_str.upper()
