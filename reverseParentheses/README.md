You have a string `s` that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in `s` form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.

**Example**

* For string `s = "a(bc)de"`, the output should be
    `reverseParentheses(s) = "acbde"`.

* For string `s = "a(bcdefghijkl(mno)p)q"`, the output should be
    `reverseParentheses(s) = "apmnolkjihgfedcbq"`.

* For string `s = "co(de(fight)s)"`, the output should be
    `reverseParentheses(s) = "cosfighted"`.

* For string `s = "Code(Cha(lle)nge)"`, the output should be
    `reverseParentheses(s) = "CodeegnlleahC"`.
