#挿入しようとするデータの存在確認を行います.

def is_data_exist(data_list, data):
    for exist_data in data_list:
        if data["month"] == exist_data["month"] and data["year"] == exist_data["year"]:
            if data["count"] == exist_data["count"]:
                return True, data_list.index(exist_data)
            elif data["count"] != exist_data["count"]:
                return False, data_list.index(exist_data)
    return False, -1
    
def change_data(data_list, data, index):
    data_list[index] = data