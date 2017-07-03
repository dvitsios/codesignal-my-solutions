def ratingThreshold(threshold, ratings):

    manual_list = []

    for i in range(len(ratings)):
        s = sum(ratings[i]) / float(len(ratings[i]))
        
        if s < threshold:
            manual_list += [i]
            
    return manual_list