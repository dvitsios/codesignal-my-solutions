def minSubstringWithAllChars(s, t):

    if len(t) == 0 or len(s) == 0:
        return ''

    if len(t) == 1 and t in s:
        return t

    all_substrings = []
    start_idx = 0

    while True:
        cur_substr = ''
        char_cnt=0
        visited_chars = dict([(k, 0) for k in t])

        for i in range(len(s)):
            if s[i] in t:
                visited_chars[s[i]] = 1
                char_cnt += 1

            if char_cnt >= 1:
                cur_substr += s[i]

            if char_cnt == 2:
                char_cnt += 1
                start_idx = i

            if all([v==1 for k,v in visited_chars.items()]):
                s = s[start_idx:]
                all_substrings.append(cur_substr)
                break

        if not all([v==1 for k,v in visited_chars.items()]):
            break

    min_substr = min(all_substrings, key=len)
    return min_substr
