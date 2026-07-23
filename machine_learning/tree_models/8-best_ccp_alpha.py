#!/usr/bin/env python3
"""
--- TASK 8 ---
function that selects the best pruning value ccp_alpha for a set
of trees
"""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """
    selects best pruning value ccp_alpha for a set of trees
    - highest test accuracy
    - if same test accuracy --> smallest difference btw 
    training and test accuracy
    - if another tie: largest ccp_alpha

    args:
    - clfs: trained with diff ccp_alpha
    - train_scores
    - test_scores
    - ccp_alphas: list of arrays

    return:
    - best alpha
    - best clf    
    """

    acc = 0
    it = 0
    for i in test_scores:
        if acc < i:
            acc = i
            it = i
    count = test_scores.count(acc)

    # print(f"acc: {acc}")
    # print(f"count: {count}")

    if count > 1:
        # print("in if count")
        subset = [(index, score) for (index, score) in enumerate(test_scores) if score == acc]
        # print(f"subset {subset}")
        # print(f"subset[0][0] {subset[0][0]}")
        dif = []
        for j in subset:
            dif.append(train_scores[j[0]] - j[1])
        min_dif = min(dif)
        min_dif_i = dif.index(min(dif))
        count = dif.count(min_dif)
        if count == 1:
            it = int(subset[min_dif_i][0])
            acc = test_scores[it]
        else:
            alpha = 0
            for k in subset:
                if alpha < ccp_alphas[k[0]]:
                    it = k[0]
                    alpha = ccp_alphas[k[0]]
                    acc = k[1]
        
    return ccp_alphas[it], clfs[it]
