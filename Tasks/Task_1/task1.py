'''
Suppose you have this email address “Amit_ml@gmail.edu” - Input Validation: Check if the input string contains exactly one "@" symbol and 
at least one "." after the "@" symbol. If it's not a valid email, return "Invalid 
email". - Extract Username: Extract and return the part of the email before the "@" 
symbol. - Extract Domain: Extract and return the domain (the part between "@" and the 
last "."). - Check for Domain Ending: Check if the email ends with ".com". If it does, 
return "Commercial Domain". If it ends with ".edu", return "Educational Domain". 
Otherwise, return "Other Domain".
'''


email = 'Amit_ml@gmail.edu'
if email.count('@') != 1 or '.' not in email.split('@')[1]:
    print("Invalid email")
else:
    user = email.split('@')[0]
    domain = email[email.index('@') + 1 : email.rindex('.')]

    if email.endswith('.com'):
        print('Commercial Domain')
    elif email.endswith('.edu'):
        print('Educational Domain')
    else:
        print('Other Domain')
