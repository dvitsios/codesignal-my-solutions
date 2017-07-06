edges_dict = {}
visited_nodes = {}

def expected_time(j, t):

    global visited_nodes
    connected_edges = edges_dict[j]

    visited_nodes[j] = 1
    connected_edges = [x for x in connected_edges if x not in visited_nodes]

    q = len(connected_edges)
    if q == 0:
        return t[j]
    else:
        time = 0
        for k in connected_edges:
            time += expected_time(k, t)

        time = t[j] + time/float(q)

    return time


def relatedQuestions(n, t, edges):

    if n == 1:
        return 0
    
    global visited_nodes

    for pair in edges:

        left, right = pair[0], pair[1]
        left1, right1 = pair[1], pair[0]

        for l,r in zip([left, right], [left1, right1]):
            if l in edges_dict:
                edges_dict[l] += [r]
            else:
                edges_dict[l] = [r]

    total_t = {}

    for j in range(n):
        visited_nodes = {}
        total_t_j = expected_time(j, t)
        total_t[j] = total_t_j

    ret_key = min(total_t, key=total_t.get)
    
    return ret_key

