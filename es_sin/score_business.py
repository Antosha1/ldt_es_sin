import math


def softmax(profits):
    sum_ = sum(math.exp(profits))
    res = []

    for profit in profits:
        x = (math.exp(profit)) / sum_
        res.append(x)

    return res


def get_score(business_names):
    d = {}
    for business_name in business_names:
        # select 'Общая итоговая сумма в чеках' as profit
        # from kkt_table
        # where 'Наименование' == business_name
        d[business_name] = profit

    profits = [profit for profit in d.values()]
    scores = softmax(profits)
    d_scores = {profits[i]: scores[i] for i in range(len(profits))}

    business_scores = {business_name: d_scores[profit] for business_name, profit in d.items()}

    return business_scores    
