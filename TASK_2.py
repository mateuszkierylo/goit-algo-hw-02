from collections import deque

def is_palindrome(input_string):
    # Normalize the string: remove spaces and convert to lower case
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Create a deque and add all characters from the normalized string
    char_deque = deque(normalized_string)
    
    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Example usage:
print(is_palindrome("Zaradny dynda raz"))
print(is_palindrome("Elf układał kufle"))                 
print(is_palindrome("Jurek"))                        
