import encryption_methods
import decryption_methods

import checking_keys as ck

print()
key = ck.edit_key_for_Venigere('Hello 123ленин')
print(key)
enc_str = encryption_methods.encrypt_Vigenere('ПРИВЕТ мир hello world', key)
print(enc_str)

in_str = decryption_methods.decrypt_Vigenere(enc_str, key)
print(in_str)


print()
key = ck.edit_key_for_Decimatiy('sfg34')
print("Decimatyu key:", key)
if key:
    enc_str = encryption_methods.encrypt_Decimatiy('Cryptography', 21)
    print(enc_str)
    in_str = decryption_methods.encrypt_Decimatiy(enc_str, 21)
    print(in_str)

# key bcad - OK
# key cabac - OK
# key abbacdss -OK
# key i am is the greatest in the world men - OK
key = 'CRYPTOGRAPHY'

print()
in_str = ck.edit_instr_column_cipher('hello world is me3452')
print("New in str:          ", ck.edit_instr_column_cipher('hello world is me'))
new_key = ck.edit_key_column_cipher(key)
print(new_key)
enc_str = encryption_methods.encrypt_columns_cipher(in_str, key)
print(enc_str)

in_str = decryption_methods.decrypt_columns_cipher(enc_str, key)
print(in_str)