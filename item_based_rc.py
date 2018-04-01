from flask import jsonify
import pandas as pd
from scipy.spatial.distance import cosine


def getListItem(id_item):
    data_item_base_frame = pd.read_csv('data_item_base_frame.csv', index_col = [0])
    row = data_item_base_frame.loc[id_item].sort_values(ascending=False)[:11].index
    my_list = []
    for i in range(1,10):
        my_list.append(row[i])
    print my_list
    return jsonify(my_list)

#TODO
def add_row_and_training(row):
    return

def training():
    data = pd.read_csv('data.csv')
    # --- Start Item Based Recommendations --- #
    # Drop any column named "user"
    data_item_base = data.drop('user', 1)
    # store DataFrame
    data_item_base_frame = pd.DataFrame(index=data_item_base.colums, columns=data_item_base.columns)
    # Calculate similarily
    for i in range(0, len(data_item_base_frame.columns)):
        # Loop through the columns for each column
        for j in range(0, len(data_item_base_frame.columns)):
            # Calculate similarity
            data_item_base_frame.ix[i, j] = 1 - cosine(data.ix[:, i], data.ix[:, j])

    data_item_base_frame.to_csv('data_item_base_frame.csv', sep=',', encoding='utf-8')
