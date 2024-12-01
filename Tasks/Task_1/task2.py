'''
Encoded Message: 
###!!@mocleW EPGTQ!!!6789 
Steps to Decode: 
1. Extract the core part of the message: "mocleW EPGTQ". 
2. Reverse the first word: "mocleW" becomes "Welcome". 
3. Replace shifted vowels in the second word: 
o "EPGTQ": No vowels to change. 
4. Final decoded message: "Welcome PGTQ". 
'''


message = "##!!@mocleW EPGTQ!!!6789"

first_word = message[message.index('@') + 1 : message.index(' ')]
first_word = ''.join(reversed(first_word))

second_word = message[message.index(' ') + 1 : message.index('Q') + 1]
second_word = second_word.replace('E', '')

decoded_message = first_word + ' ' + second_word
print(decoded_message)
