class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
brackets = {
    ')': '(',
    '}': '{',
    ']': '['
}
opening_brackets = brackets.values()
closing_brackets = brackets.keys()

def is_symmetric(string: str):
    stack = Stack()

    characters = list(string)
    for char in characters:
        if char in opening_brackets:
            stack.push(char)
            continue
        
        if char in closing_brackets:
            if stack.is_empty():
                return "String is not symmetric" 
            
            opposite_bracket = brackets.get(char)
            if opposite_bracket == stack.peek():
                stack.pop()
            else:
                return "String is not symmetric" 
            
    if not stack.is_empty():
        return "String is not symmetric" 
            
    return "String is symmetric"