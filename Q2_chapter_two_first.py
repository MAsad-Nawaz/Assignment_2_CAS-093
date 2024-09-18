
def process_string(s):

    number_str = ''.join([ch for ch in s if ch.isdigit()])
    letter_str = ''.join([ch for ch in s if ch.isalpha()])
    
    
    even_numbers = [int(n) for n in number_str if int(n) % 2 == 0]
    even_numbers_ascii = [ord(str(n)) for n in even_numbers]
    
    
    uppercase_letters = [ch for ch in letter_str if ch.isupper()]
    uppercase_ascii = [ord(ch) for ch in uppercase_letters]
    
    return even_numbers, even_numbers_ascii, uppercase_letters, uppercase_ascii


s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

even_numbers, even_numbers_ascii, uppercase_letters, uppercase_ascii = process_string(s)


print("Even Numbers:", even_numbers)
print("Even Numbers ASCII:", even_numbers_ascii)
print("Uppercase Letters:", uppercase_letters)
print("Uppercase ASCII:", uppercase_ascii)
