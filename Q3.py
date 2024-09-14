# File name: decrypted_and_fixed_code.py

import time
import sys

def slow_print(text, delay=0.005):
    """Prints text one character at a time with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is printed immediately
        time.sleep(delay)   # Wait for a specified time before printing the next character
    print()

print("\n=====Key Reveal Code Start=====\n")
key_code  = """
total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

# Initialize the counter
counter = 0

# Second loop to adjust total
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2
"""
print(key_code)
print("\n=====Key Reveal Code End=====\n")
def calculate_key():
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    # Initialize the counter
    counter = 0

    # Second loop to adjust total
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2

    # Output the result as the key
    print("Key of Decryption:", total)
    return total


# Decryption function to decrypt the code using the key
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


# Main function to control the flow
def main():
    print("Enter 1 for the encrypted key")
    input1 = input()  # User inputs '1' to calculate the key

    if input1 == '1':
        key = calculate_key()  # Calculate and display the key

    print("\nPress 2 to decrypt the provided code with the found key")
    input2 = input()  # User inputs '2' to decrypt the code

    if input2 == '2':
        encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = { 'xrl1' : 'inyhr1' , 'xrl2' : 'inyhr2' , 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [ 1,2,3,4,5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = { 1,2,3,4,5,5,4,3,2,1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg ['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg[ 'xrl4'] == 10:
    cevag("pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qypgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
        """

        decrypted_code = decrypt(encrypted_code, key)
        print("\n=====Decrypted Code Start=====\n")
        slow_print(decrypted_code)
        print("\n=====Decrypted Code End=====\n")

    print("\nPress 3 to fix the decrypted code and show output")
    input3 = input()  # User inputs '3' to display fixed code

    if input3 == '3':
        # Comment on issues in decrypted code and provide fixed code output
        
        # Issues in Decrypted Code:
        # 1. Obfuscated variable names (e.g., 'tybony_inevnoyr' instead of 'total_inventory').
        # 2. Incorrect or unclear function logic.
        # 3. Syntax errors and invalid function names.

        # Fixed code:
        fixed_code = """

# Fixed global variable definition and corrected the function call error
global_variable = 100
my_dict = {'key1' : 'value1' , 'key2' : 'value2' , 'key3': 'value3'}

def process_numbers(numbers):  # Fix: Added 'numbers' parameter to match the function call
    global global_variable
    local_variable = 5
    # Fix: Ensure correct list handling
    while local_variable > 0:
        if local_variable in numbers:  # Fix: Check if 'local_variable' is in 'numbers' to avoid ValueError
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5}  # Fix: Removed duplicate elements, as sets automatically handle duplicates
result = process_numbers(numbers=my_set)  # Fix: Correctly pass the 'numbers' argument to 'process_numbers'

def modify_dict(value):  # Fix: Added 'value' parameter to match the function call
    local_variable = 10
    my_dict['key4'] = local_variable  # Fix: Correctly updated dictionary entry

modify_dict(5)  # Fix: Removed unnecessary argument as it’s not used in 'modify_dict'

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    # Fix: Removed redundant 'i += 1' as 'range()' already handles iteration

if my_set is not None and my_dict['key4'] == 10:  # Fix: Fixed key access to match 'modify_dict' changes
    print("condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
        """
        print("\n=====Corrected Encypted Code Start=====\n")
        slow_print(fixed_code)
        print("\n=====Corrected Encypted Code End=====\n")
        slow_print("\n=====Below Output of Corrected Code=====")
        # Fixed global variable definition and corrected the function call error
        global_variable = 100
        my_dict = {'key1' : 'value1' , 'key2' : 'value2' , 'key3': 'value3'}

        def process_numbers(numbers):  # Fix: Added 'numbers' parameter to match the function call
            global global_variable
            local_variable = 5
            # Fix: Ensure correct list handling
            while local_variable > 0:
                if local_variable in numbers:  # Fix: Check if 'local_variable' is in 'numbers' to avoid ValueError
                    numbers.remove(local_variable)
                local_variable -= 1

            return numbers

        my_set = {1, 2, 3, 4, 5}  # Fix: Removed duplicate elements, as sets automatically handle duplicates
        result = process_numbers(numbers=my_set)  # Fix: Correctly pass the 'numbers' argument to 'process_numbers'

        def modify_dict(value):  # Fix: Added 'value' parameter to match the function call
            local_variable = 10
            my_dict['key4'] = local_variable  # Fix: Correctly updated dictionary entry

        modify_dict(5)  # Fix: Removed unnecessary argument as it’s not used in 'modify_dict'

        def update_global():
            global global_variable
            global_variable += 10

        for i in range(5):
            print(i)
            # Fix: Removed redundant 'i += 1' as 'range()' already handles iteration

        if my_set is not None and my_dict['key4'] == 10:  # Fix: Fixed key access to match 'modify_dict' changes
            print("condition met!")

        if 5 not in my_dict:
            print("5 not found in the dictionary!")

        print(global_variable)
        print(my_dict)
        print(my_set)

# Run the main function
if __name__ == "__main__":
    main()
