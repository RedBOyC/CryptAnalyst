def char_num(letter):
    letter = letter.upper()  
    numerical_value_of_letter = str(ord(letter) - ord('A'))
    if int(numerical_value_of_letter) < 10:
        numerical_value_of_letter = '0' + numerical_value_of_letter
    return numerical_value_of_letter

def split_text(string):
    string_number = ''
    lst1 = []
    for char in string:
        if char.isalpha(): 
            char_value = char_num(char)
            string_number += char_value
            lst1.append(int(char_value))  
    return string_number, lst1

def caesar_cipher(k, lst):  
    lst2 = []
    for num in lst:
        shifted_num = (num + k) % 26  
        shifted_str = str(shifted_num)
        if shifted_num < 10:
            shifted_str = '0' + shifted_str
        lst2.append(shifted_str)
    return lst2

def encryption(words, key): 
    texts_list = words.split()
    encrypted_text_list = []
    
    for text in texts_list:
        encrypted_text = ''
        string_number, lst1 = split_text(text)       
        if lst1:
            lst2 = caesar_cipher(key, lst1)
            
            for num_str in lst2:
                num = int(num_str)
                encrypted_letter = chr(num + ord('A'))
                encrypted_text += encrypted_letter
            encrypted_text_list.append(encrypted_text)
    return ' '.join(encrypted_text_list)


##Main
original_msg = input('Enter message: ')
key = int(input('Enter the key: '))
encrypted_message = encryption(original_msg, key)
print(f"Encrypted message: {encrypted_message}")

