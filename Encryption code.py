print("Welcome to the Encryption Lab.")

user_name = input('Enter your Username :')
print(f'''Welcome {user_name}.
Now enter your text.''')
text = input('')

user_text = text.replace(' ','')
print(f'Your text is: {user_text}')

shift = 10
shifted_text = user_text[shift:] + user_text[:shift]

translation_table = str.maketrans(user_text, shifted_text)
encrypted_text = text.translate(translation_table)
print(f'Your encrypted text is {encrypted_text}')
print(f'Thank you for passing by {user_name}.')
 
