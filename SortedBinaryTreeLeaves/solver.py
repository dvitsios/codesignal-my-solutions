def find(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def treeBottom(tree):

    left_par_indexes = find(tree, '(')
    d = {}
    nums = {}
    sorted_nums = []

    cnt = 0
    for j in left_par_indexes:
        r = find(tree[j:], ' ')
        if r != []:
            r = r[0]
        else:
            continue

        num = tree[j: j+r]
        num = num[1:]
        if not num.isdigit():
            continue

        nums[j] = int(num)
        sorted_nums += [int(num)]
        cnt += 1

    par_cnt_arr = []
    left_par_cnt = 0
    for j in range(len(tree)):
        c = tree[j]
        if c == '(':
                left_par_cnt += 1
        if c == ')':
            left_par_cnt -= 1
        par_cnt_arr.append(left_par_cnt)

    cnt = 1
    for k in nums:
        if nums[k] not in d:
            d[nums[k]] = par_cnt_arr[k]
        else:
            d[str(nums[k])+'_'+str(cnt)] = par_cnt_arr[k]
            cnt += 1

    max_depth = max(d.values())
    out = []
    for (k,v) in d.items():
        if v == max_depth:
            k = int(str(k).split('_')[0])
            out += [k]

    mm = []
    for i in sorted_nums:
        for j in range(len(out)):
            if i == out[j]:
                mm += [out[j]]
                del out[j]
                break

    return mm
