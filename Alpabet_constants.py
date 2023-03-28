EN_LETTERS = ''.join([chr(i) for i in range(ord('A'), ord('Z') + 1)]) + ''.join(
    [chr(i) for i in range(ord('a'), ord('z') + 1)])
RU_LETTERS = 'АБВГДЕЁ' + ''.join([chr(i) for i in range(ord('Ж'), ord('Я') + 1)]) + 'абвгдеё' + ''.join(
    [chr(i) for i in range(ord('ж'), ord('я') + 1)])
ru_alp_len = 66
en_alp_len = 52