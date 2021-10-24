from string import ascii_lowercase, ascii_uppercase, printable
import random
import math


def encrypt_caesar(word, shift):
    # Create a function that accepts a string and integer
    # shift value as parameters and returns a new string
    # after a Caeser cipher has been applied.
    new_word = ""  # The new word generated
    word = word.lower()  # Make the word lower to make case insensitive
    listLetters = list(printable)

    for i in range(0, len(word)):  # Loop through each letter of the input
        letter = word[i]  # Get the index of the letter
        # Append the letter to the new word generated
        new_word += listLetters[(listLetters.index(letter) + shift) % 100]

    return new_word


def decrypt_caesar(word, shift):
    # Create a function that accepts a string and integer
    # shift value as parameters and returns a new string
    # after a Caeser cipher has been applied.
    new_word = ""  # The new word generated
    word = word.lower()  # Make the word lower to make case insensitive
    listLetters = list(printable.replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", ""))

    for i in range(0, len(word)):  # Loop through each letter of the input
        letter = word[i]  # Get the index of the letter
        # Append the letter to the new word generated
        new_word += listLetters[(listLetters.index(letter) - shift) % (len(listLetters) - 26)]

    return new_word


def encrypt_polybius(content, keyphrase):
    grid = []
    alpha = list(ascii_uppercase)
    output = ""
    keyword = keyphrase
    extra = ""
    index = 0
    word = content.split()

    if keyphrase == "":
        for i in range(5):
            grid.insert(len(grid), [alpha.pop(0) for j in range(5)])
        extra = alpha.pop(0)
    else:
        keyword = list(keyword)
        for l in keyword:  # Take out the common letter from the alphabet
            if l in alpha:
                alpha.remove(l)

        for i in range(5):  # Loop through the outer loop (the rows)
            grid.insert(len(grid), [])  # Insert a row in the table
            for j in range(5):  # # Loop through the inner loop (each element in a row)
                # If not all the letters in the keyword are used, then execute the following
                if len(keyword) != 0:
                    letter = keyword.pop(0)
                    grid[i].insert(len(grid[i]), letter)
                    for k in keyword:  # Delete the multiple occurrences in the keyword
                        if k == letter:
                            keyword.remove(k)

                else:  # If all the letters are used complete with the rest of alphabet list
                    grid[i].insert(len(grid[i]), alpha.pop(0))
        extra = alpha.pop(0)

    while index < len(content):  # Replace the letters of content by the coordinates
        if content[index] != extra:
            for i in range(5):
                for j in range(5):
                    if grid[i][j] == content[index]:
                        output += str(i + 1) + str(j + 1) + " "
            index += 1
        else:
            output += "99"
            index += 1

    return output.strip()


def decrypt_polybius(content, keyphrase):
    grid = []
    alpha = list(ascii_uppercase)
    output = ""
    keyword = keyphrase
    extra = ""
    index = 0
    word = content.split(" ")

    if keyphrase == "":
        for i in range(5):
            grid.insert(len(grid), [alpha.pop(0) for j in range(5)])
        extra = alpha.pop(0)
    else:
        keyword = list(keyword)
        for l in keyword:  # Take out the common letter from the alphabet
            if l in alpha:
                alpha.remove(l)

        for i in range(5):  # Loop through the outer loop (the rows)
            grid.insert(len(grid), [])  # Insert a row in the table
            for j in range(5):  # # Loop through the inner loop (each element in a row)
                # If not all the letters in the keyword are used, then execute the following
                if len(keyword) != 0:
                    letter = keyword.pop(0)
                    grid[i].insert(len(grid[i]), letter)
                    for k in keyword:  # Delete the multiple occurrences in the keyword
                        if k == letter:
                            keyword.remove(k)

                else:  # If all the letters are used complete with the rest of alphabet list
                    grid[i].insert(len(grid[i]), alpha.pop(0))
        extra = alpha.pop(0)

    for i in word:
        if i == "99":
            output += extra
        else:
            output += grid[int(i[0])][int(i[1])]
    return output


def encrypt_railfence(content, rails):
    fence = [[] for i in range(rails)]
    for rail in fence:
        for j in range(len(content)):
            rail.insert(len(rail), ".")
    row = 0
    col = 0
    index = 0
    factor = 1
    output = ""
    while col < len(content):
        fence[row][col] = content[col]
        if row == 0:
            factor = 1
        elif row == rails - 1:
            factor = -1
        row += 1 * factor
        col += 1
        index += 1

    for i in fence:
        for j in i:
            if j != ".":
                output += j

    return output


def decrypt_railfence(content, rails):
    fence = [[] for i in range(rails)]
    for rail in fence:
        for j in range(len(content)):
            rail.insert(len(rail), ".")
    content = list(content)
    row = 0
    col = 0
    index = 0
    factor = 1

    while col < len(content):
        fence[row][col] = "#"  # Placeholder
        if row == 0:  # Add the next letter up-right or down-right
            factor = 1
        elif row == rails - 1:
            factor = -1
        row += 1 * factor
        col += 1

    for i in range(rails):  # Replace the placeholders with the letters
        for j in range(len(fence[0])):
            if fence[i][j] == "#":
                fence[i][j] = content.pop(0)

    row = 0
    col = 0
    factor = 1

    output = ""
    while col < len(content):
        output += ""  # For some reason, this line doesn't work properly
        if row == 0:  # Add the next letter up-right or down-right
            factor = 1
        elif row == rails - 1:
            factor = -1
        row += 1 * factor
        col += 1

    return output


def encrypt_vigenere(content, keyphrase):
    content = list(content)
    substitute = []  # Change the letters into numbers (index)
    key = []
    for i in content:
        try:
            substitute.append(ascii_lowercase.index(i))
        # if it finds something that is not a letter (\n), it changes it to 99
        except ValueError:
            if i == " ":
                substitute.append(98)
            elif i == "\n":
                substitute.append(99)
    for j in keyphrase:
        key.append(ascii_lowercase.index(j))

    num = len(key)
    ctrl = 0

    while len(key) < len(substitute):  # If substitute is longer than key, add elements to key
        key.insert(len(key), key[ctrl])
        ctrl += 1
        if ctrl >= num:
            ctrl = 0

    temp = [(key[i] + substitute[i]) % 26 for i in range(len(substitute))]
    for i in range(len(substitute)):
        if substitute[i] == 98:
            temp.append(98)
        elif substitute[i] == 99:
            temp.append(99)
        else:
            temp.append((key[i] + substitute[i]) % 26)
    output = []
    for i in temp:
        if i == 98:
            output.append(" ")
        elif i == 99:
            output.append("\n")
        else:
            output.append(ascii_lowercase[i])

    return "".join(output)


def decrypt_vigenere(content, keyphrase):
    content = list(content)
    # Change the letters into numbers (index)
    substitute = [ascii_lowercase.index(i) for i in content]
    key = [ascii_lowercase.index(i) for i in keyphrase]
    num = len(key)
    ctrl = 0

    while len(key) < len(substitute):  # If substitute is longer than key, add elements to key
        key.insert(len(key), key[ctrl])
        ctrl += 1
        if ctrl >= num:
            ctrl = 0

    temp = [(substitute[i] - key[i]) for i in range(len(substitute))]
    output = [ascii_lowercase[i] for i in temp]

    return "".join(output)


def file_to_string(file):
    file = open(f"{file}", "r")  # Finds the file in the folder
    word = "".join(file.readlines())
    for line in word:
        line = line.lower()
    return word


def file_encrypt(word_encrypted):
    file = open("encrypted.txt", "w")
    file.write(word_encrypted)
    file.close()


def file_decrypt(word_decrypted):
    file = open("decrypted.txt", "w")
    file.write(word_decrypted)
    file.close()


def to_binary(file1, file2):
    f1 = open(f"{file1}", "r")
    text = f1.readlines()
    substitute = []
    binary_array = []
    for i in text:  # Transform each element into ASCII number
        for j in i:
            substitute.append(j)

    for char in range(len(substitute)):
        # Add the binary number corresponding to it
        binary_array.append(bin(ord(substitute[char]))[2:])

    f2 = open(f"{file2}", "w")
    f2.write(" ".join(binary_array))
    f1.close()
    f2.close()


def to_text(file1, file2):
    f1 = open(f"{file1}", "r")
    text = f1.readlines()
    substitute = []
    f1.close()

    for line in text:
        line = line.split()
        for chunk in line:
            if chunk != " ":
                substitute.append(chr(int(chunk, 2)))

    f2 = open(f"{file2}", "w")
    f2.write("".join(substitute))
    f2.close()


class RSA():
    def __init__(self, message):
        self.num1 = 5#self.extract()[0]  # Random prime number for generator
        self.num2 = 6#self.extract()[1]  # Random prime number for generator
        # The differents keys generated
        self.generated = self.generator(self.num1, self.num2)
        self.public = self.public_key(
            message, self.generated[0], self.generated[3])  # Encrypted
        self.private = self.private_key(
            self.public, self.generated[0], self.generated[2])  # Decrypted

    def lcm(self, num1, num2):
        for i in range(max(num1, num2), (num1*num2) - 1):  # Find the LCM
            if i % (num1 - 1) == 0 and i % (num2 - 1) == 0:
                return i
        return 0

    def extract(self):  # Extract 2 random prime numbers from a file
        f = open("numbers.txt", "r")
        lines = f.readlines()

        for i in lines:  # Remove new lines characters
            if i == "\n":
                lines.remove(i)

        for j in range(0, len(lines)):
            lines.insert(j, lines.pop(j).split())  # Eliminate the empty spaces

        # Cast from str to int
        num1 = int(random.choice(lines[random.randint(0, len(lines))]))
        # Cast from str to int
        num2 = int(random.choice(lines[random.randint(0, len(lines))]))
        return num1, num2

    # Generate the different numbers needed to encrypt and decrypt the message
    def generator(self, num1, num2):
        N = num1 * num2
        lcm = self.lcm(num1, num2)
        multInverse = 17  # Multiplicative inverse

        def coprime(multiple):  # Find the coprime of the LCM
            for num in range(2, multiple):
                if math.gcd(num, multiple) == 1:
                    return num
            return 0

        for something in range(2, lcm):  # Find modular inverse
            if (coprime(lcm) * something) % lcm == 1:
                multInverse = something

        return N, lcm, multInverse, coprime(lcm)

    def public_key(self, message, n, e):  # Encrypt the message
        return (message ** e) % n

    def private_key(self, content, n, d):  # Decrypt the message
        return (content ** d) % n


def text_to_binary(file1, file2):
    text = file_to_string(file1)  # A string
    text = text.split("\n")  # Turn into a list, separator "\n"

    for i in range(len(text)):
        # create a mini array of bytes of each character in the element at i
        temp = [bytes(a, encoding="utf8") for a in text[i]]
        text.pop(i)
        text.insert(i, temp)
    text.pop(len(text) - 1)
    print(text)


class DES():
    '''Implementation of the DES algorithm'''

    def __init__(self, to_encrypt):
        pass

message = list("hello wo")

chunks = []
shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
subkeys = []


def is_eight_bytes(byte) -> bool:
    '''Checks if the parameter is 8 bytes long'''
    if len(byte) == 8:
        return True
    return False


def complete_byte(byte) -> str:
    '''Complete the string representation of the parameter by adding 0s to the front'''
    binary = []
    if len(byte) < 8:
        binary = (8-len(byte)) * "0" + byte
    elif len(byte) > 8:
        binary = byte[:8]  # Cut the byte value to 8 elements
    return binary


def bin2D(binary):
    '''Return a 2D array made of the single bytes of the parameter'''
    if is_eight_bytes(binary):
        return [list(complete_byte(bin(ord(element)).replace("0b", ""))) for element in binary]  # Complete the binary value and return a 2D representation of it
    else:
        pass


message = bin2D(message)


def find(num, table=1, key=bin2D("fabrice ")):
    '''Find the bit at the numth index in the table'''
    if table == 1:  # Modify PC-1
        control = 0
        while True:
            for arr in range(len(key)):
                for ind in range(len(key[arr])):
                    if control == num:
                        return key[arr][ind]
                    control += 1


def shift_left(num, array):
    temp = array[0].pop(0)
    control = 0
    while control > num:
        for line in range(1, len(PC1)):
            array[control - 1].append(array[control].pop(0))
    array[len(array) - 1].append(temp)

    for ind in range(len(array) - 1):
        array[ind].append(array[ind + 1].pop(0))

    temp = [i for i in array]

    return temp  # Generator


PC1 = [
    # Left Half
    [find(57), find(49), find(41), find(33), find(25), find(17), find(9)],
    [find(1), find(58), find(50), find(42), find(34), find(26), find(18)],
    [find(10), find(2), find(59), find(51), find(43), find(35), find(27)],
    [find(19), find(11), find(3), find(60), find(52), find(44), find(36)],
    # Right Half
    [find(63), find(55), find(47), find(39), find(31), find(23), find(15)],
    [find(7), find(62), find(54), find(46), find(38), find(30), find(22)],
    [find(14), find(6), find(61), find(53), find(45), find(37), find(29)],
    [find(21), find(13), find(5), find(28), find(20), find(12), find(4)]
]

IP = [
    [find(58, key=message), find(50, key=message), find(42, key=message), find(34, key=message),
     find(26, key=message), find(18, key=message), find(10, key=message), find(2, key=message)],
    [find(60, key=message), find(52, key=message), find(44, key=message), find(36, key=message),
     find(28, key=message), find(20, key=message), find(12, key=message), find(4, key=message)],
    [find(62, key=message), find(54, key=message), find(46, key=message), find(38, key=message),
     find(30, key=message), find(22, key=message), find(14, key=message), find(6, key=message)],
    [find(64, key=message), find(56, key=message), find(48, key=message), find(40, key=message),
     find(32, key=message), find(24, key=message), find(16, key=message), find(8, key=message)],
    [find(57, key=message), find(49, key=message), find(41, key=message), find(33, key=message),
     find(25, key=message), find(17, key=message), find(9, key=message), find(1, key=message)],
    [find(59, key=message), find(51, key=message), find(43, key=message), find(35, key=message),
     find(27, key=message), find(19, key=message), find(11, key=message), find(3, key=message)],
    [find(61, key=message), find(53, key=message), find(45, key=message), find(37, key=message),
     find(29, key=message), find(21, key=message), find(13, key=message), find(5, key=message)],
    [find(63, key=message), find(55, key=message), find(47, key=message), find(39, key=message),
     find(31, key=message), find(23, key=message), find(15, key=message), find(7, key=message)]
]

keys = []


for i in range(16):  # Shift 16 times
    subkeys.append(shift_left(shifts[i], PC1[:4]))
    subkeys.append(shift_left(shifts[i], PC1[4:]))

for i in range(0, len(subkeys), 2):
    keys.append(subkeys[i] + subkeys[i + 1])


# for arr in subkeys:
#     print("Arr: ", arr)
# print("Subkeys: ", len(subkeys))

# print("Keys: ", len(keys))

PC2 = [
    [find(1, key=keys),    find(17, key=keys),   find(11, key=keys),    find(24, key=keys),     find(1, key=keys),    find(5, key=keys)],
    [find(3, key=keys),    find(28, key=keys),   find(15, key=keys),     find(6, key=keys),    find(21, key=keys),   find(10, key=keys)],
    [find(23, key=keys),    find(19, key=keys),   find(12, key=keys),     find(4, key=keys),    find(26, key=keys),    find(8, key=keys)],
    [find(16, key=keys),     find(7, key=keys),   find(27, key=keys),    find(20, key=keys),    find(13, key=keys),    find(2, key=keys)],
    [find(41, key=keys),    find(52, key=keys),   find(31, key=keys),    find(37, key=keys),    find(47, key=keys),   find(55, key=keys)],
    [find(30, key=keys),    find(40, key=keys),   find(51, key=keys),   find(45, key=keys),    find(33, key=keys),   find(48, key=keys)],
    [find(44, key=keys),    find(49, key=keys),   find(39, key=keys),    find(56, key=keys),    find(34, key=keys),   find(53, key=keys)],
    [find(46, key=keys),    find(42, key=keys),   find(50, key=keys),    find(36, key=keys),    find(29, key=keys),   find(32, key=keys)]
]



for i in range(len(keys)):
    keys.insert(i, PC2)

# print()
# print()

# print(IP)

message_left0 = IP[:4]  # First half of the message
message_right0 = IP[4:]  # Second Half of the message

# print(message_left0)
# print(message_right0)

sub_left = [message_left0]  # variations of the left half
sub_right = [message_right0]  # Variations of the right half

E = lambda x: [  # E-table used to expand the right half of
        [find(32, key=sub_right[x]),   find(1, key=sub_right[x]),    find(2, key=sub_right[x]),     find(3, key=sub_right[x]),     find(4, key=sub_right[x]),    find(5, key=sub_right[x])],
        [find(4, key=sub_right[x]),   find(5, key=sub_right[x]),    find(6, key=sub_right[x]),     find(7, key=sub_right[x]),     find(8, key=sub_right[x]),    find(9, key=sub_right[x])],
        [find(8, key=sub_right[x]),    find(9, key=sub_right[x]),   find(10, key=sub_right[x]),    find(11, key=sub_right[x]),    find(12, key=sub_right[x]),   find(13, key=sub_right[x])],
        [find(12, key=sub_right[x]),  find(13, key=sub_right[x]),   find(14, key=sub_right[x]),    find(15, key=sub_right[x]),    find(16, key=sub_right[x]),   find(17, key=sub_right[x])],
        [find(16, key=sub_right[x]),  find(17, key=sub_right[x]),   find(18, key=sub_right[x]),    find(19, key=sub_right[x]),    find(20, key=sub_right[x]),   find(21, key=sub_right[x])],
        [find(20, key=sub_right[x]),  find(21, key=sub_right[x]),   find(22, key=sub_right[x]),    find(23, key=sub_right[x]),    find(24, key=sub_right[x]),   find(25, key=sub_right[x])],
        [find(24, key=sub_right[x]),  find(25, key=sub_right[x]),   find(26, key=sub_right[x]),    find(27, key=sub_right[x]),    find(28, key=sub_right[x]),   find(29, key=sub_right[x])],
        [find(28, key=sub_right[x]),  find(29, key=sub_right[x]),   find(30, key=sub_right[x]),    find(31, key=sub_right[x]),    find(32, key=sub_right[x]),    find(1, key=sub_right[x])]
]


def xor_list(input1, input2, index):  # to XOR the left and right halves
    temp_array = []
    for item in range(len(input1)):
        # temp1 = int(input1[item][index])  # Element from the left
        # temp2 = int(input2[item][index])  # element from the right (modified in E-table)
        print(input1[item][index])
        print(input2[item][index][0])
        # temp_array.append(list(bin(temp1 ^ temp2).replace("0b", "")))
    # return temp_array


# for i in range(1, 5):
#     sub_left.append(sub_right[i - 1])
#     temp = xor_list(E(i - 1), keys[i], i)
#     sub_right.append(xor_list(sub_left[0][i-1], temp, i))  # Left + E(KEYn, Right)
#     # After feeding Right to E, XOR it with KEY ---

# print("Sub left: ", sub_left)
# print("Sub right: ", sub_right)

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
