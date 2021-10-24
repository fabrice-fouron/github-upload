

PC1 =[
    [57, 49, 41, 33, 25, 17, 9],
    [1, 58, 50, 42, 34, 26, 18],
    [10, 2, 59, 51, 43, 35, 27],
    [19, 11, 3, 60, 52, 44, 36],
    [63, 55, 47, 39, 31, 23, 15],
    [7, 62, 54, 46, 38, 30, 22],
    [14, 6, 61, 53, 45, 37, 29],
    [21, 13, 5, 28, 20, 12, 4]
]

PC2 = [
    [14, 17, 11, 24, 1, 5],
    [3, 28, 15, 6, 21, 10],
    [23, 19, 12, 4, 26, 8],
    [16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48],
    [44, 49, 39, 56, 34, 53],
    [46, 42, 50, 36, 29, 32]
]

IP = [
    [58, 50, 42, 34, 26, 18, 10, 2],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 4, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7]
]

E = [
    [32, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8, 9],
    [8, 9, 10, 11, 12, 13],
    [12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21],
    [20, 21, 22, 23, 24, 25],
    [24, 25, 26, 27, 28, 29],
    [28, 29, 30, 31, 32, 1]
]

S_BOX = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1,  14,  8,  13,  6,   2, 11,  15, 12,   9,  7,   3, 10,   5,  0],
        [15, 12,   8,  2,   4, 9,  1,  7,   5, 11,   3, 14,  10,  0,   6, 13]
    ],

    [
        [15,  1,   8, 14,   6, 11,   3,  4,   9,  7,   2, 13,  12,  0,   5, 10],
        [3, 13,  4,  7,  15,  2,   8, 14,  12, 0,  1, 10,   6,  9,  11,  5],
        [0, 14,  7, 11,  10,  4, 13,  1,  5,  8,  12,  6,   9,  3,   2, 15],
        [13,  8,  10,  1,   3, 15,   4,  2,  11,  6,  7, 12,   0,  5,  14,  9]
    ],

    [
        [10,  0,   9, 14,   6,  3,  15,  5,   1, 13,  12,  7,  11,  4,   2,  8],
        [13,  7,   0,  9,   3,  4,   6, 10,   2,  8,   5, 14,  12, 11,  15,  1],
        [13,  6,   4,  9,   8, 15,   3,  0,  11,  1,   2, 12,   5, 10,  14,  7],
        [1, 10,  13,  0,   6,  9,   8,  7,  4, 15,  14,  3,  11,  5,   2, 12]
    ],

    [
        [7, 13,  14,  3,   0,  6,   9, 10,   1,  2,   8,  5,  11, 12,   4, 15],
        [13,  8,  11,  5,   6, 15,   0,  3,  4,  7,  2, 12,   1, 10,  14,  9],
        [10,  6,   9,  0,  12, 11,   7, 13,  15,  1,   3, 14,   5,  2,   8,  4],
        [3, 15,   0,  6,  10,  1,  13,  8,   9,  4,   5, 11,  12,  7,   2, 14]
    ],

    [
        [2, 12,   4,  1,   7, 10,  11, 6,   8,  5,   3, 15,  13,  0,  14,  9],
        [14, 11,   2, 12,   4,  7,  13,  1,   5,  0,  15, 10,   3,  9,   8,  6],
        [4,  2,   1, 11,  10, 13,   7,  8,  15,  9,  12,  5,   6,  3,   0, 14],
        [11,  8, 12,  7,   1, 14,   2, 13,   6, 15,   0,  9,  10,  4,  5,  3]
    ],

    [
        [12,  1,  10, 15,   9,  2,   6,  8,   0, 13,   3,  4,  14,  7,   5, 11],
        [10, 15,   4,  2,   7, 12,   9,  5,   6, 1, 13, 14,   0, 11,   3,  8],
        [9, 14,  15,  5,   2,  8,  12,  3,   7,  0,   4, 10,   1, 13,  11, 6],
        [4,  3,  2, 12,   9,  5,  15, 10,  11, 14,   1,  7,   6,  0,   8, 13]
    ],

    [
        [4, 11,   2, 14,  15,  0,   8, 13,   3, 12,   9,  7,   5, 10,   6,  1],
        [13,  0,  11,  7,   4,  9,  1, 10,  14,  3,  5, 12,   2, 15,   8,  6],
        [1,  4, 11, 13,  12,  3,   7, 14,  10, 15,  6,  8,   0,  5,   9,  2],
        [6, 11,  13,  8,   1,  4,  10,  7,   9,  5,   0, 15,  14,  2,   3, 12],
    ],

    [
        [13,  2,  8,  4,   6, 15,  11,  1,  10,  9,   3, 14,   5,  0,  12,  7],
        [1, 15,  13,  8,  10,  3,   7,  4, 12,  5,   6, 11,   0, 14,   9,  2],
        [7, 11,   4,  1,   9, 12,  14,  2,   0, 6,  10, 13,  15,  3,   5,  8],
        [2,  1,  14, 7,   4, 10,   8, 13,  15, 12,   9,  0,   3,  5,   6, 11]
    ]
]

P = [
    [16,   7,  20,  21],
    [29,  12,  28,  17],
    [1,  15,  23,  26],
    [5,  18,  31,  10],
    [2,   8,  24,  14],
    [32,  27,   3,   9],
    [19,  13,  30,   6],
    [22,  11,   4,  25]
]

IP_1 = [
    [40,     8,   48,    16,    56,   24,    64,   32],
    [39,     7,   47,    15,    55,   23,    63,   31],
    [38,     6,   46,    14,    54,   22,    62,   30],
    [37,     5,   45,    13,    53,   21,    61,   29],
    [36,     4,   44,    12,    52,   20,    60,   28],
    [35,     3,   43,    11,    51,   19,    59,   27],
    [34,     2,   42,    10,    50,   18,    58,   26],
    [33,     1,   41,     9,    49,   17,    57,   25]
]


def to_bin(message) -> list:
    '''Creates a 2D array of binary representation of the parameter'''
    message = list(message)
    for i in range(len(message)):
        message.insert(i, make_eight_bits(list(bin(ord(message.pop(i))).replace("0b", ""))))
    return message


def make_eight_bits(byte) ->list:
    '''If the input is not 8 bytes long, complete with zeros in the front'''
    temp = byte
    while len(temp) < 8:
        temp.insert(0, '0')
    return temp


def shift_left(num, array) -> list:
    control = 0

    while control > num:
        temp = array[control].pop(0)
        for line in range(0, len(array)):
            array[control - 1].append(temp)
        control += 1

    temp = [i for i in array]
    
    return temp


def modify(list1, target_list) -> list:
    '''Modify the keys with different tables'''
    output_list = []
    for i in range(len(list)):
        temp = []
        for j in range(len(list1[i])):
            count = 0
            for a in len(target_list):
                for b in len(target_list[a]):
                    if count == list[i][j]:
                        temp.append(target_list[a][b])
                    count += 1
        output_list.append(temp)
    return output_list


def xor(list1, list2) -> list:
    '''XOR 2 lists and return a list as result'''
    output = []
    for i in range(len(list1)):
        output.append(int(list1[i]) ^ int(list2[i]))
    return output


# class DES:
#     '''DES Encryption  (Assuming the message and the key are 64 bits long)'''
#     def __init__(self, message, key) -> None:
#         self.message = modify(IP, to_bin(message))
#         self.leftM = [message[:4]]
#         self.rightM = [modify(E, message[4:])]
#         self.key = modify(to_bin(key), PC1)  # Array representation of the key
#         self.all_keys = [self.key]
#         self.leftK = [self.key[:4]]
#         self.rightK = [self.key[4:]]
#         self.SBOX = []




#     def key_generator(self) -> list:
#         '''Generates the different permutations of the key'''
#         for i in range(1, 17):
#             if i != 1 or i != 2 or i != 9 or i != 16:
#                 self.all_keys.append(shift_left(1, self.all_keys[i - 1]))
#             else:
#                 self.all_keys.append(shift_left(2, self.all_keys[i - 1]))

#     def leftK_generator(self) -> list:
#         '''Generates the different permutations of the left half of the key'''
#         for i in range(17):
#             self.leftK.append(self.all_keys[i][:4])


#     def rightK_generator(self) -> list:
#         '''Generates the different permutations of the left half of the key'''
#         for i in range(17):
#             self.rightK.append(self.all_keys[i][4:])
    

#     def subkeys_change(self) -> list:
#         for i in range(1, 17):
#             self.leftK.pop(i)
#             self.leftK.insert(i, modify(PC2, self.leftK[i]))
#             self.rightK.pop(i)
#             self.rightK.insert(i, modify(PC2, self.rightK[i]))
#             self.all_keys.pop(i)
#             self.all_keys.insert(i, self.leftK[i] + self.rightK[i])

#     def rightM_xor_key(self, key, message) -> list:
#         return xor(key, modify(E, message))


#     def add_leftM(self, index):
#         self.leftM.append(self.rightM[index - 1])

#     def add_rightM(self, index):
#         xor(self.leftM[index - 1], self.rightM_xor_key(self.all_keys[index], self.rightM[index]))


#     def s_box(self):
#         xored = []
#         for i in range(1, 9):
#             xored.append(self.rightM_xor_key(self.all_keys[i], self.rightM[i]))
        
#         for val in range(len(xored)):  
#             row = int("".join(xored[val][0] + xored[val][5]), 2)  # Row of the S number
#             col = int("".join(xored[val][1:4]), 2)  # Column for the S number
#             var = list(bin(S_BOX[val][row][col]).replace("0b", ""))  # Change it into binary
#             while len(var) < 4:  # Make sure that the number is 4 bits long
#                 var.insert(0, '0')
#             self.SBOX.append([i for i in var])  # Add to a list
    
#     def final_permut(self) -> list:
#         return modify(IP_1, self.rightM[15] + self.leftM[15])

    
#     def encrypt(self):
#         pass


#     def decrypt(self):
#         pass

# def to_text(list1) -> str:
#     for i in range(len(list1)):
#         list1.insert(i, chr(int("".join(list1.pop(i)), 2)))
