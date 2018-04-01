import pandas as pd
from flask import jsonify


def similarity_score(history, similarities):
    return sum(history*similarities) / sum(similarities)


def getListItem(id_user):
    data_user_base_frame = pd.read_csv('data_user_base_frame.csv', index_col=[1])
    row = data_user_base_frame.loc[id_user].sort_values(ascending=False)[:11].index
    my_list = []
    for i in range(1,10):
        my_list.append(row[i])
    print my_list
    return jsonify(my_list)


def init():
    data = pd.read_csv('data_1.csv')
    data_item_base = data.drop('user', 1)
    data_item_base_frame = pd.read_csv('data_item_base_frame.csv', index_col = [0])
    data_neighbors = pd.DataFrame(index=data_item_base_frame.columns, columns = range(1, 11))
    # Order by similarity
    for i in range(0, len(data_item_base_frame.columns)):
        data_neighbors.ix[i,:10] = data_item_base_frame.ix[0:, i].sort_values(ascending=False)[:10].index
    data_sims = pd.DataFrame(index=data.index, columns=data.columns)
    data_sims.ix[:, 0] = data.ix[:, 0]
    for i in range(0, len(data_sims.index)):
        for j in range(1, len(data_sims.columns)):
            user = data_sims.index[i]
            product = data_sims.columns[j]
            if data.ix[i, j] == 1:
                data_sims.ix[i, j] = 0
            else:
                product_top_names = data_neighbors.ix[product][1:10]
                product_top_sims = data_item_base_frame.ix[product].sort_values(ascending=False)[1:10]
                user_purchases = data_item_base.ix[user, product_top_names]
                data_sims.ix[i, j] = similarity_score(user_purchases, product_top_sims)
    data_sims.to_csv('data_sims.csv', sep=',', encoding='utf-8')
    print data_sims
    data_recommend = pd.DataFrame(index=data_sims.ix[:, 0], columns=range(1, 11))
    data_recommend.ix[0:, 0] = data_sims.ix[:, 0]
    data_recommend.to_csv('data_recommend.csv', sep=',', encoding='utf-8')