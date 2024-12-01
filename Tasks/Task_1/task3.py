'''
Encoded Message: 
&&&**$gnirtS PLIO!!@1234 
Steps to Decode: 
1. Extract the core part of the message: "gnirtS PLIO". 
2. Reverse the first word: "gnirtS" becomes "String". 
3. Replace shifted vowels in the second word: 
o "PLIO": Replace I->E and O->U to get "PLEU". 
4. Final decoded message: "String PLEU".
'''


message = '&&&**$gnirtS PLIO!!@1234'

first_word = message[message.index('$') + 1:message.index(' ')]
first_word = first_word[::-1]  # عكس الكلمة مباشرة

second_word = message[message.index(' ') + 1:message.index('!')]
second_word = second_word.replace('I', 'E').replace('O', 'U')

decoded_message = first_word + ' ' + second_word
print(decoded_message)
