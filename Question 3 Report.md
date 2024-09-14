
# Question 3: Fixing the error-prone codes
The program consists of three major components:

Key Calculation: The first part of the program calculates a key based on a combination of two loops.
Decryption Function: This function decrypts a provided block of encrypted text using the key obtained from the first part.
Corrected Code Execution: The decrypted code is then further fixed for logical errors and executed to demonstrate the correct functionality.

The final program file has all the necessary fixes and comments
## 1. Fixing the Code to Reveal the Key
- Correct errors in the provided code to reveal the encryption key needed for decryption.

- **Original Code:**
The program calculates a numeric key used for decrypting an encrypted block of code. The process involves two loops:

First Loop: Adjusts the total using conditions based on the loop indices.
Second Loop: Further adjusts the total based on the value of the total calculated from the first loop.
Outcome
Final Key Value: The final total, which is the key, is printed and used for decryption

- **Errors:**
  - Incorrect variable names and types.
  - Logical errors in loops and conditionals.
  - Syntax errors, such as incorrect use of indentation and keywords.

- **Corrections:**
  - Fixed variable names and ensured they are consistently used.
  - Corrected loop conditions and syntax errors.
  - Made sure the calculation logic aligns with the expected key generation.

- **Key Revealed:**
  - The encryption key is successfully revealed as `13` through the fixed code

![Reveal_Key](Screenshots/Q3Reveal_Key.png) 


## 2. Writing the Decryption Function
- Implement a function to decrypt the encrypted code using the key obtained.

- **Original Code:**
Input: The encrypted block of text (code).
Logic: The function uses the calculated key to reverse the encryption by shifting characters backward in the alphabet.
Output: The decrypted code is printed.


- **Decryption Method:**
  The decryption function shifts each character in the encrypted text by the key value in the opposite direction of encryption. 
Processing Numbers: Modifies a list of numbers based on a certain condition.
Modifying Dictionary: Updates the dictionary by adding a new key-value pair.
Updating Global Variable: Increments the global variable based on a specific logic.
Condition Checking: Performs checks on the dictionary and set for certain conditions, printing results accordingly.

- **Function:**
  - The function reads each character in the encrypted text.
  - It adjusts the ASCII value of the character based on the key to reverse the encryption shift.
  - Special handling is done for uppercase and lowercase letters to ensure correct decryption.

- The `decrypt` function effectively reverses the encryption applied to the provided code snippet, producing readable decrypted code.
![Decrypted Code](Screenshots/Q3Decrypted_Code.png)


## 3. Correcting Errors and Providing Comments
- Fix errors in the decrypted code and add comments explaining the corrections.

- **Decrypted Code:**
  The decrypted code contained multiple logical errors and issues with variable usage and function definitions.
 **Identified Errors:** Function call mismatches, parameter issues, redundant set elements, unnecessary increments, incorrect key checks, and typographical errors.

## Error 1: Function Parameter Mismatch
- **Error:** The function `process_numbers` is called with a parameter (`numbers=my_set`), but it is defined without parameters.
- **Fix:** The function call should match the function definition. Remove the argument when calling the function, as it does not expect any parameters.

## Error 2: Incorrect Function Call

- **Error:**  The function `modify_dict` is called with an argument (`5`), but it does not accept any parameters.
- **Fix:**Call the function without arguments, as it is defined to operate without input parameters.

## Error 3: Redundant Elements in Set

- **Error:**  The set `my_set` contains duplicate values, which are not allowed in a set.
- **Fix:** Remove duplicate elements to ensure the set only contains unique values, which aligns with the set's intended use.

## Error 4: Unnecessary Increment in Loop

- **Error:** * The statement `i += 1` inside the `for` loop is unnecessary because the loop automatically increments the variable.
- **Fix:** Remove the `i += 1` statement, as the `for` loop already handles the iteration.

## Error 5: Incorrect Dictionary Key Check

- **Error:**  The check `if 5 not in my_dict` is incorrect because `5` is not a key in the dictionary `my_dict`.
- **Fix:** Modify the condition to check for actual keys in the dictionary or adjust the logic to match the intended check.

## Error 6: Typographical Error in Print Statement

- **Error:** The print statement `print("5 not found in the dlctionary!")` contains a typo (`dlctionary` instead of `dictionary`).
- **Fix:** Correct the spelling in the print statement to ensure clear and accurate messaging.

Program Structure: 
1. Global Variables
The program defines a global variable global_variable which is modified throughout the code.
It also uses a dictionary (my_dict) and a set (my_set) to store key-value pairs and a collection of unique numbers, respectively.
2. Functions
process_numbers(): Processes a list of numbers based on certain conditions.
modify_dict(): Adds a new key-value pair to the global dictionary.
update_global(): Increments the global variable by a specified amount.
3. Conditional Logic
The program includes conditional checks for:
The presence of specific keys in the dictionary.
Certain conditions for set membership.
4. Loops
A for loop iterates through a range of numbers, printing each one.
A while loop processes numbers based on specific conditions in the process_numbers() function.
![Corrected Decrypted Code](Screenshots/Q3CorrectedEncryptedCode.png)

## Comments:
  - Global and local variables
  - Function calls
  - Redundant code
  - Condition checks
  - Typos in print statements
  - Corrections made to fix errors and improve code readability
The comments directly address the errors and provide explanations for the corrections without cluttering the logic.

## 4. Program Output
Final Results:
The program successfully performs the following actions:

  - Prints the Calculated Key: The key used for decryption is printed after the first two loops complete their execution.
  - Prints Decrypted Code: After calculating the key, the encrypted code is decrypted and displayed.
  - Displays Corrected Program Output: The decrypted code is fixed for errors and executed, displaying the correct results:
  - Global Variable Value: Shows the updated value of the global variable.
  - Dictionary Contents: Prints the updated dictionary with the new key-value pair.
  - Set Contents: Displays the unique elements of the set.
  - The program has been successfully debugged, with all identified errors fixed. 
  - Each function operates as expected, and the final output shows the correct values of variables and structures after execution. 
  - The decryption process works as intended, and the corrected code is functioning smoothly without runtime issues.

![Program Output](Screenshots/Q3Output.png)
