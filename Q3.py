# File name: decrypted_and_fixed_code.py

# Additional total calculation code for Key
def calculate_key():
    total = 0  # Initialize the variable total

    # First loop to calculate total
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += 1 + j
            else:
                total -= 1 - j

    # Initialize the counter
    counter = 0

    # Second loop to adjust total
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total = 1
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
    print("Enter 1 and press Enter for the encrypted key")
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
            cevag("5 abg sbhaq va gur qypgvbanel!”)

        cevag(tybony_inevnoyr)
        cevag(zl_qvpg)
        cevag(zl_frg)
        """

        decrypted_code = decrypt(encrypted_code, key)
        print("\nDecrypted Code:\n", decrypted_code)

    print("\nPress 3 to fix the decrypted code and show output")
    input3 = input()  # User inputs '3' to display fixed code

    if input3 == '3':
        # ---- Now the fixed code ----
        global_variable = 100  # Global variable to store inventory count
        my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}  # Dictionary

        def process_numbers():
            global global_inventory
            global_inventory = 5
            numbers = [1, 2, 3, 4, 5]
            
            while global_inventory > 0:
                if global_inventory % 2 == 0:
                    if global_inventory in numbers:
                        numbers.remove(global_inventory)
                global_inventory -= 1
            
            return numbers

        my_set = {1, 2, 3, 4, 5}
        result = process_numbers()

        def modify_dict():
            local_inventory = 10
            my_dict['key4'] = local_inventory

        modify_dict()

        def update_global():
            global global_inventory
            global_inventory += 10

        update_global()

        for i in range(5):
            print(i)

        if my_set is not None and my_dict['key4'] == 10:
            print("Condition met!")

        if 5 not in my_dict:
            print("5 not found in the dictionary!")
        
        print("Final output has been displayed.") 
        print(global_variable)
        print(my_dict)
        print(my_set)

        print("Final output has been displayed.")


# Run the main function
if __name__ == "__main__":
    main()
