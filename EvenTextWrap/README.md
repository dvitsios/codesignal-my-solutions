Given an array of words and a length `l`, format the text such that each line has exactly `l` characters and is fully justified on both the left and the right. Words should be packed in a greedy approach; that is, pack as many words as possible in each line. Add extra spaces when necessary so that each line has exactly `l` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text and lines with one word only, the words should be left justified with no extra space inserted between them.

** Example **

For

`words = ["This", "is", "an", "example", "of", "text", "justification."]` 
and `l = 16`, the output should be

```
textJustification(words, l) = ["This    is    an",
                               "example  of text",
                               "justification.  "]
```