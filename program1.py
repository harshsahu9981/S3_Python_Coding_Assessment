def isValid(s: str) -> bool:
    # Dictionary to hold the matching pairs
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in matching_brackets.values():
            # If it's an opening bracket, push to stack
            stack.append(char)
        elif char in matching_brackets.keys():
            # If it's a closing bracket, check the stack
            if stack == [] or stack.pop() != matching_brackets[char]:
                return False
        else:
            # Invalid character (not expected in this problem)
            return False
    
    # If the stack is empty, all brackets matched correctly
    return stack == []
