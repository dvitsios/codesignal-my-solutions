def find_best_combination(stories, h):

    #print('*************')
    #print(h, stories)
    # find optimal combination of stories with score: max and sum(size) <= h

    vals = [0]
    weights = [0]
    keys = []

    # init values and weights
    for s in sorted(stories):
        l = stories[s]
        #print(l)
        vals += [l[1]]
        weights += [l[2]]
        keys += [s]

    n = len(stories)
    #print('n:', n)
    #print(stories)
    m = [ [0] * (h+1) for _ in range(n+1)]

    for j in range(h+1):
        m[0][j] = 0

    for i in range(1,n+1):
        for j in range(h+1):
            if weights[i] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j - weights[i]] + vals[i])

    path = []

    j = h
    for i in range(n, 0, -1):
        #print(i)
        if m[i][j] != m[i-1][j]:
            path.append(i-1)

            j -= weights[i]

    path.reverse()

    final_path = []
    for p in path:
        final_path += [keys[p]]

    final_path = [m[n][h]] + final_path
    #print(keys)
    return final_path



def feedOptimizer(span, h, events):

    result = []

    stories = {}
    story_timestamps = {}

    start_time = 0
    i = 0
    for e in events:

        # new story event
        if len(e) == 3:
            #print('\n----- Story -----')
            if i == 0: # 1st timestamp
                start_time = e[0]

            i += 1
            stories[i] = e
            story_timestamps[i] = e[0]
            #print('story_timestamps:', story_timestamps)

        else: # calc feed output
            cur_time = e[0]
            #print('\n----- reload -----')
            #print('cur_time:', cur_time)
            #elapsed_time = cur_time - start_time

            ids_to_del = [x for x in story_timestamps if story_timestamps[x] < cur_time - span]

            for k in ids_to_del:
                #print('delete dict elems')
                #print(k)
                del story_timestamps[k]
                del stories[k]
                #print(stories)

            if len(stories):
                cur_res = find_best_combination(stories, h)

                result += [cur_res]
            else:
                result += [[0]]

    return result


