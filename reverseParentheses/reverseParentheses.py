def reverseParentheses(s):

    bracket_pairs = []
    left_brackets_stack = []

    for i in range(len(s)):
        char = s[i]
        if char == '(':
            left_brackets_stack += [i]
        elif char == ')':
            left_bracket = left_brackets_stack[-1]
            del left_brackets_stack[-1]

            bracket_pairs += [(left_bracket, i)]

    #print(bracket_pairs)

    for b in bracket_pairs:
        left, right = b

        subs = s[left:right]
        subs =  subs[::-1]
        s = s[:left]+subs+s[right:]
        #print(s)

    s = s.replace(')', '')
    s = s.replace('(', '')
    return(s)

