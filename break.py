import time
import string
from ciphers import encrypt_caesar, decrypt_caesar, decrypt_polybius, decrypt_railfence, RSA
import csv

list_csv = []


def import_csv():
    file = open("sample.csv", "r")

    for line in file:
        list_csv.append(line.replace("\n", ""))


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


class Break:

    def __init__(self, method):
        self.method = method
        start_time = time.time()
        if method == "caesar":
            self.caesar_all("hi")
        elif method == "polybius":
            self.polybius()
        elif method == "rsa":
            print(self.rsa(70707))
        elif method == "des":
            self.DES()
        end = time.time()
        # import_csv()
        # print(list_csv)
        # print(self.caesar_all("Ymj%Tqn{jw%Frjx%Mnlm%Xhmttq%htrrzsny~%tk%kfhzqy~1%xyfkk1%xyzijsyx1%ufwjsyx1%fsi%wjxnijsyx%gjqnj{j%ymfy%ns%twijw%yt%kzqknqq%nyx%rnxxnts%tk%j}hjqqjshj%fsi%jvzny~%ns%jizhfynts1%|j%rzxy%jrgti~%ymj%nijfqx%tk%f%htruwjmjsxn{j%mnlm%xhmttq3"))
        print("\tIt took", end - start_time, "seconds")


    def caesar_all(self, ciphertext):
        '''Use a linear pattern to find what the shift key is'''
        index = 0
        shift = 0
        for i in list_csv:
            for j in range(len(string.printable.replace("ABCDEFGHIJKLMNOPQRSTUVWXZ", ""))):
                if i.lower() == decrypt_caesar(ciphertext, j):
                    return i
                print(decrypt_caesar(ciphertext, j).lower())  # FIX THE PROBLEM WITH THE ALPHABET AND THE LOWER/UPPER CONFLICT


    def polybius(self):
        pass

    def rsa(self, number):
        rsa = RSA(number)  # initialize the rsa object
        message = 65  # sample number
        sample = 0
        for num in range(1, number, 2):
            if is_prime(num):  # If a prime number is found, then...
                print("Num:", num)
                for num2 in range(1, num, 2):
                    if is_prime(num2):  # Find a prime number lower num
                        print("Num2:", num2)
                        tup1 = rsa.generator(num, num2)  # Generate

                        for m in range(number):
                            if rsa.public_key(m, tup1[0], tup1[3]) == number:  # If the public key creates a number similar to the input, then it is the public key
                                public = rsa.public_key(m, tup1[0], tup1[3])
                                message = m
                                outputStr = f"Encrypted: {public} - Decrypted: {message}"
                                return outputStr
        return "Nope, not it :)"


    def railfence(self):
        pass

    def DES(self):
        pass


Break("rsa")