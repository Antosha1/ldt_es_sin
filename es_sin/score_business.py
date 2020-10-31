import numpy as np


def softmax(profits):
    sum_ = sum(np.exp(profits))
    res = []

    for profit in profits:
        x = (np.exp(profit)) / sum_
        res.append(x)

    return res


def get_score(businesses):
    # d = {}
    # for business_name in businesses:
    #     profit = 0
    #     # select 'Общая итоговая сумма в чеках' as profit
    #     # from kkt_table
    #     # where 'Наименование' == business_name
    #     d[business_name] = profit
    #
    # profits = [profit for profit in d.values()]
    profits = businesses.Profit.values
    scores = softmax(profits)
    print(scores)
    # d_scores = {profits[i]: scores[i] for i in range(len(profits))}

    # business_scores = {business_name: d_scores[profit] for business_name, profit in d.items()}

    return scores
