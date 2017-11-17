"""

Question            : 59
Start Time          : 17.11.17 13:23
End Time            : 17.11.17 13:56
Total Time Spent    : 00:33
Complexity          : O(n*m) n: number of keys m: length of message
Answer              : 107359

"""
import string

with open("p059_cipher.txt") as file:
    ciphertext_unformatted = file.read()
ciphertext = map(int, ciphertext_unformatted.split(","))

keys = list()
key_length = 3
alphabet = string.ascii_lowercase
number_of_characters = len(alphabet)

for i in range(number_of_characters ** key_length):
    chars = [ord('a')] * key_length
    num = i
    k = 0
    while num > 0:
        chars[k] = ord(alphabet[num % number_of_characters])
        num /= number_of_characters
        k += 1
    keys.append(chars)

for key in keys:
    while len(key) < len(ciphertext):
        key.extend(key)
    message_list = []
    for cipher_, key_ in zip(ciphertext, key):
        message_list.append(chr(cipher_ ^ key_))
    message =  ''.join(message_list)
    if 'the' in message and 'are' in message and 'of' in message and 'and' in message :
        print "Key:", list(map(chr, key[:key_length]))
        print "Message: ", message
        break
print sum(map(ord, message))
