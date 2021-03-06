from random import randint


# Константы. (tup_16, pi, r, a, c)
TUP_16 = ('0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

PI = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46, 153, 186,
      23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132,
      2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171, 242, 42, 104,
      162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 21, 161, 150, 41,
      16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128,
      195, 189, 13, 87, 223, 245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222,
      122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100,
      159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172,
      29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216,
      133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230, 244, 180,
      192, 209, 102, 175, 194, 57, 75, 99, 182)

R = (0, 8, 16, 24, 32, 40, 48, 56, 1, 9, 17, 25, 33, 41, 49, 57, 2, 10, 18, 26, 34, 42, 50, 58, 3, 11, 19, 27, 35, 43,
     51, 59, 4, 12, 20, 28, 36, 44, 52, 60, 5, 13, 21, 29, 37, 45, 53, 61, 6, 14, 22, 30, 38, 46, 54, 62, 7, 15, 23, 31,
     39, 47, 55, 63)

A = ('8e20faa72ba0b470', '47107ddd9b505a38', 'ad08b0e0c3282d1c', 'd8045870ef14980e', '6c022c38f90a4c07',
     '3601161cf205268d', '1b8e0b0e798c13c8', '83478b07b2468764', 'a011d380818e8f40', '5086e740ce47c920',
     '2843fd2067adea10', '14aff010bdd87508', '0ad97808d06cb404', '05e23c0468365a02', '8c711e02341b2d01',
     '46b60f011a83988e', '90dab52a387ae76f', '486dd4151c3dfdb9', '24b86a840e90f0d2', '125c354207487869',
     '092e94218d243cba', '8a174a9ec8121e5d', '4585254f64090fa0', 'accc9ca9328a8950', '9d4df05d5f661451',
     'c0a878a0a1330aa6', '60543c50de970553', '302a1e286fc58ca7', '18150f14b9ec46dd', '0c84890ad27623e0',
     '0642ca05693b9f70', '0321658cba93c138', '86275df09ce8aaa8', '439da0784e745554', 'afc0503c273aa42a',
     'd960281e9d1d5215', 'e230140fc0802984', '71180a8960409a42', 'b60c05ca30204d21', '5b068c651810a89e',
     '456c34887a3805b9', 'ac361a443d1c8cd2', '561b0d22900e4669', '2b838811480723ba', '9bcf4486248d9f5d',
     'c3e9224312c8c1a0', 'effa11af0964ee50', 'f97d86d98a327728', 'e4fa2054a80b329c', '727d102a548b194e',
     '39b008152acb8227', '9258048415eb419d', '492c024284fbaec0', 'aa16012142f35760', '550b8e9e21f7a530',
     'a48b474f9ef5dc18', '70a6a56e2440598e', '3853dc371220a247', '1ca76e95091051ad', '0edd37c48a08a6d8',
     '07e095624504536c', '8d70c431ac02a736', 'c83862965601dd1b', '641c314b2b8ee083')

C = ('b1085bda1ecadae9ebcb2f81c0657c1f2f6a76432e45d016714eb88d7585c4fc'
     '4b7ce09192676901a2422a08a460d31505767436cc744d23dd806559f2a64507',
     '6fa3b58aa99d2f1a4fe39d460f70b5d7f3feea720a232b9861d55e0f16b50131'
     '9ab5176b12d699585cb561c2db0aa7ca55dda21bd7cbcd56e679047021b19bb7',
     'f574dcac2bce2fc70a39fc286a3d843506f15e5f529c1f8bf2ea7514b1297b7b'
     'd3e20fe490359eb1c1c93a376062db09c2b6f443867adb31991e96f50aba0ab2',
     'ef1fdfb3e81566d2f948e1a05d71e4dd488e857e335c3c7d9d721cad685e353f'
     'a9d72c82ed03d675d8b71333935203be3453eaa193e837f1220cbebc84e3d12e',
     '4bea6bacad4747999a3f410c6ca923637f151c1f1686104a359e35d7800fffbd'
     'bfcd1747253af5a3dfff00b723271a167a56a27ea9ea63f5601758fd7c6cfe57',
     'ae4faeae1d3ad3d96fa4c33b7a3039c02d66c4f95142a46c187f9ab49af08ec6'
     'cffaa6b71c9ab7b40af21f66c2bec6b6bf71c57236904f35fa68407a46647d6e',
     'f4c70e16eeaac5ec51ac86febf240954399ec6c7e6bf87c9d3473e33197a93c9'
     '0992abc52d822c3706476983284a05043517454ca23c4af38886564d3a14d493',
     '9b1f5b424d93c9a703e7aa020c6e41414eb7f8719c36de1e89b4443b4ddbc49a'
     'f4892bcb929b069069d18d2bd1a5c42f36acc2355951a8d9a47f0dd4bf02e71e',
     '378f5a541631229b944c9ad8ec165fde3a7d3a1b258942243cd955b7e00d0984'
     '800a440bdbb2ceb17b2b8a9aa6079c540e38dc92cb1f2a607261445183235adb',
     'abbedea680056f52382ae548b2e4f3f38941e71cff8a78db1fffe18a1b336103'
     '9fe76702af69334b7a1e6c303b7652f43698fad1153bb6c374b4c7fb98459ced',
     '7bcd9ed0efc889fb3002c6cd635afe94d8fa6bbbebab07612001802114846679'
     '8a1d71efea48b9caefbacd1d7d476e98dea2594ac06fd85d6bcaa4cd81f32d1b',
     '378ee767f11631bad21380b00449b17acda43c32bcdf1d77f82012d430219f9b'
     '5d80ef9d1891cc86e71da4aa88e12852faf417d5d9b21b9948bc924af11bd720')


# Преобразования. (x, s, p, l)
def x(k: str, m: str) -> str:
    xk = [str(int(k[i]) ^ int(m[i])) for i in range(len(k))]
    return ''.join(xk)


def s(bits: str) -> str:
    s_string = ''
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        num = mod_f_b_in_decimal(byte)
        pi_num = PI[num]
        s_string += mod_f_d_in_bit(pi_num, 8)

    return s_string


def p(bits: str) -> str:
    p_list_string = ['' for _ in range(64)]
    index = 0
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        p_index = R[index]
        p_list_string[p_index] = byte
        index += 1

    p_string = ''.join(p_list_string)
    return p_string


def l(bits: str) -> str:
    bit_a = [mod_f_16_in_b(i) for i in A]
    vec_matrix = []
    for i in range(0, len(bits), 64):
        vec_matrix.append(bits[i:i+64])

    length = 64
    new_vec_matrix = [[0 for _ in range(length)] for _ in range(len(vec_matrix))]
    for i in range(len(vec_matrix)):
        for j in range(length):
            for k in range(length):
                new_vec_matrix[i][j] += int(vec_matrix[i][k]) * int(bit_a[k][j])
                if k == length - 1:
                    new_vec_matrix[i][j] = str(new_vec_matrix[i][j] % 2)

    for i in range(len(new_vec_matrix)):
        new_vec_matrix[i] = ''.join(new_vec_matrix[i])

    return ''.join(new_vec_matrix)


# Функции сжатия. (e (key_schedule in e), g)
def e(k, m):
    for i in range(len(C) + 1):
        if i == len(C):
            m = x(k, m)
        else:
            m = l(p(s(x(k, m))))
            k = l(p(s(x(k, mod_f_16_in_b(C[i])))))
    return m


def g(n, h, m):
    k = l(p(s(x(h, n))))
    res_g = x(x(e(k, m), h), m)
    return res_g


# Next Step
def mod_text_in_bit(text: str) -> str:
    bit_text = ''

    encode_text = text.encode('utf-8')

    for i in range(len(encode_text)):
        bit_text = bit_text + '0' * (8 - len(format(encode_text[i], 'b'))) + format(encode_text[i], 'b')

    return bit_text


def mod_f_d_in_bit(num: int, n) -> str:
    if num == 0 and n != 0:
        return '0' * n
    elif num == 0:
        return '0'

    rev_bit_num = []
    while num != 0:
        m = num % 2
        num //= 2
        rev_bit_num.append(str(m))

    zero_list = ['0' for _ in range(n - len(rev_bit_num))]
    rev_bit_num += zero_list

    if n != 0:
        rev_bit_num = rev_bit_num[:n]

    rev_bit_num.reverse()
    bit_num = ''.join(rev_bit_num)
    return bit_num


def mod_f_b_in_16(bit: str) -> str:
    str16 = ''
    for i in range(0, len(bit), 4):
        num = mod_f_b_in_decimal(bit[i:i + 4])
        str16 += TUP_16[num]
    return str16


def mod_f_16_in_b(str16: str) -> str:
    str_bit = ''
    for i in str16:
        str_bit += mod_f_d_in_bit(TUP_16.index(i), 4)
    return str_bit


def mod_f_b_in_decimal(bit: str) -> int:
    num = 0
    for i in range(len(bit)):
        num += int(bit[i]) * 2 ** (len(bit) - i - 1)
    return num


def stribog(m: str, key: str) -> str:
    if key == '1':
        IV = '0' * 512
    else:
        IV = '00000001' * 64

    h, n, z = IV, '0' * 512, '0' * 512

    while True:
        length_m = len(m)
        if length_m < 512:
            m = '0' * (511 - len(m)) + '1' + m
            break
        else:
            m1, m = m[:length_m - 512], m[-512:]
            h = g(n, h, m)
            n = mod_f_d_in_bit(mod_f_b_in_decimal(n) + 512, 512)
            z = mod_f_d_in_bit(mod_f_b_in_decimal(z) + mod_f_b_in_decimal(m), 512)
            m = m1

    h = g(n, h, m)
    n = mod_f_d_in_bit(mod_f_b_in_decimal(n) + length_m, 512)
    z = mod_f_d_in_bit(mod_f_b_in_decimal(z) + mod_f_b_in_decimal(m), 512)
    h = g('0' * 512, h, n)
    h = g('0' * 512, h, z)
    if key == '1':
        return h
    else:
        return h[:256]


def pmf(k, t):
    while True:
        p = ""
        for i in range(k - 2):
            p = str(randint(0, 1)) + p
        p = "1" + p + '1'
        p = int(p, 2)
        flag = 1
        if p == 2:
            return True
        if not p & 1:
            return False

        def check(a, s, d, p):
            x = pow(a, d, p)
            if x == 1:
                return True
            for i in range(s - 1):
                if x == p - 1:
                    return True
                x = pow(x, 2, p)
            return x == p - 1

        s = 0
        d = p - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        for i in range(t):
            a = randint(2, p - 2)
            if not check(a, s, d, p):
                flag = 0
        if flag == 1:
            return p


class BitString:
    def __init__(self, value: str):
        self.bits = value

    def __add__(self, other):
        if isinstance(other, BitString) and len(self.bits) == len(other.bits):
            new_bits = ''

            length = len(self.bits)
            for i in range(length):
                new_bits += str((int(self.bits[i]) + int(other.bits[i])) % 2)

            return BitString(new_bits)

    def __mul__(self, other):
        if isinstance(other, BitString) and len(self.bits) == len(other.bits):
            new_bits = ''

            length = len(self.bits)
            for i in range(length):
                new_bits += str(int(self.bits[i]) * int(other.bits[i]))

            return BitString(new_bits)

    def __floordiv__(self, other):
        if isinstance(other, BitString):
            return BitString(self.bits + other.bits)

    def __len__(self):
        return len(self.bits)

    def no(self):
        new_bits = ''

        length = len(self.bits)
        for i in range(length):
            new_bits += str(1 - int(self.bits[i]))

        return BitString(new_bits)

    def csr(self, steps: int):
        new_bits = self.bits[-steps:] + self.bits[:-steps]

        return BitString(new_bits)

    def sr(self, steps: int):
        new_bits = '0' * steps + self.bits[:-steps]

        return BitString(new_bits)

    def split(self, length):
        list_blocks = []

        for i in range(0, len(self.bits), length):
            list_blocks.append(BitString(self.bits[i:i + length]))

        return list_blocks

    def mod_f_b_in_decimal(self) -> int:
        num = 0
        for i in range(len(self.bits)):
            num += int(self.bits[i]) * 2 ** (len(self.bits) - i - 1)
        return num

    def mod_f_b_in_16(self):
        str16 = ''
        for i in range(0, len(self.bits), 4):
            num = BitString.mod_f_b_in_decimal(BitString(self.bits[i:i + 4]))
            str16 += TUP_16[num]
        return str16

    @staticmethod
    def join(list_bits):
        new_str_bits = ''
        for i in list_bits:
            new_str_bits += i.bits

        return BitString(new_str_bits)

    @staticmethod
    def mod_f_d_in_bit(num: int, length):
        if num == 0 and length != 0:
            return BitString('0' * length)
        elif num == 0:
            return BitString('0')

        rev_bit_num = []
        while num != 0:
            m = num % 2
            num //= 2
            rev_bit_num.append(str(m))

        zero_list = ['0' for _ in range(length - len(rev_bit_num))]
        rev_bit_num += zero_list

        if length != 0:
            rev_bit_num = rev_bit_num[:length]

        rev_bit_num.reverse()
        bit_num = ''.join(rev_bit_num)
        return BitString(bit_num)

    @staticmethod
    def mod_f_16_in_b(str16: str):
        str_bit = BitString.mod_f_d_in_bit(TUP_16.index(str16[0]), 4)
        for i in range(1, len(str16)):
            str_bit = str_bit // BitString.mod_f_d_in_bit(TUP_16.index(str16[i]), 4)
        return str_bit

    @staticmethod
    def mod_text_in_bit(text):
        bit_text = ''
        encode_text = text.encode('utf-8')

        for i in range(len(encode_text)):
            bit_text = bit_text + '0' * (8 - len(format(encode_text[i], 'b'))) + format(encode_text[i], 'b')

        return BitString(bit_text)


def hcam_stribog(key, message, func, func_key):

    ipad = '00110110' * (size_block_for_h[func] // 8)
    opad = '01011100' * (size_block_for_h[func] // 8)

    return func(x(key, opad) + func(x(key, ipad) + message, func_key), func_key)


def gen_key():
    key = BitString.mod_f_d_in_bit(pmf(randint(100, 300), 100), 0)

    return key


def format_key(key, func):
    zero_bit = BitString('0' * (size_block_for_h[func] - len(key)))
    key //= zero_bit

    return key


def save_key(key):
    name = input('\nВведите имя файла: ')
    with open(f'{name}.key', 'w') as file:
        file.write(key)


size_block_for_h = {
    stribog: 512
}


def main():
    print('Откуда будем кодировать?\n'
          '\t1) Сообщение из консоли\n'
          '\t2) Сообщение из файла')
    message_key = input()

    if message_key == '1':
        message = input('Введите соощение: ')
    else:
        path = input('Введите имя файла: ')
        with open(f'{path}.txt', 'r', encoding='utf-8') as file:
            message = file.read()

    key = gen_key()
    save_key(key.bits)

    message = BitString.mod_text_in_bit(message)

    key = format_key(key, stribog)
    message = message.bits
    print(BitString(hcam_stribog(key.bits, message, stribog, '1')).mod_f_b_in_16())


if __name__ == '__main__':
    main()
