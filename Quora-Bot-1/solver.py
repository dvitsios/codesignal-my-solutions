import operator

def mostViewedWriters(topicIds, answerIds, views):

    final_dict = {}

    uniq_topic_ids = set([topicIds[i][j] for i in range(len(topicIds)) for j in range(len(topicIds[i])) ])

    for u in uniq_topic_ids:

        u_indexes = [x for x in range(len(topicIds)) if u in topicIds[x] ]

        tmp = [answerIds[x] for x in u_indexes]
        cur_answer_ids = [tmp[i][j] for i in range(len(tmp)) for j in range(len(tmp[i])) ]

        cur_user_id = [views[x][1] for x in range(len(views)) if views[x][0] in cur_answer_ids]
        cur_views = [views[x][2] for x in range(len(views)) if views[x][0] in cur_answer_ids]


        for (user, view) in zip(cur_user_id, cur_views):
                if u not in final_dict:
                        final_dict[u] = [ [user, view] ]
                else:
                        id_to_add_views = [x for x in range(len(final_dict[u])) if final_dict[u][x][0] == user]
                        if not id_to_add_views:
                                final_dict[u].append([user, view])
                        else:
                                idx = id_to_add_views[0]
                                final_dict[u][idx][1] += view

    final_arr = []

    for k in sorted(uniq_topic_ids):
        if k not in final_dict:
                final_arr.append([])
        else:
                sublist = final_dict[k]
                sorted_sublist1 = sorted(sublist, key=operator.itemgetter(0))
                sorted_sublist = sorted(sorted_sublist1, key=operator.itemgetter(1), reverse=True)

                if len(sorted_sublist) > 10:
                        sorted_sublist = sorted_sublist[:10]
                final_arr.append(sorted_sublist)

    return(final_arr)

