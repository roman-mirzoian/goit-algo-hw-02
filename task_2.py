from collections import deque

def is_palindrome(string: str):
    prepared_chars = list(string.replace(" ", "").lower())
    chars_queue = deque(prepared_chars)

    while len(chars_queue) > 1:
        if chars_queue.popleft() != chars_queue.pop():
            return "String is not palindrome"
    
    return "String is palindrome"
