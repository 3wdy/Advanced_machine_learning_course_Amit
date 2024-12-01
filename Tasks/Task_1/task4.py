'''
Encoded Message: 
##$$$@!yalpstcejorp EPUVT****9887 
Steps to Decode: 
1. Extract the core part of the message: "yalpstcejorp EPUVT". 
2. Reverse the first word: "yalpstcejorp" becomes "projectplay". 
3. Replace shifted vowels in the second word: 
o "EPUVT": Replace E->A, U->O to get "APOVT". 
4. Final decoded message: "projectplay APTOV". 
'''


message = '##$$$@!yalpstcejorp EPUVT****9887'

first_word = message[message.index('!') + 1:message.index(' ')]
first_word = first_word[::-1]  # عكس الكلمة مباشرة

second_word = message[message.index(' ') + 1:message.index('*')]
second_word = second_word.replace('E', 'A').replace('U', 'O')

decoded_message = first_word + ' ' + second_word
print(decoded_message)
