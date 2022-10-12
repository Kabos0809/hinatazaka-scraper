#挿入しようとするデータの存在確認を行います.

def is_data_exist(data_list, data):
    for exist_data in data_list:
        if data["month"] == exist_data["month"] and data["year"] == exist_data["year"] and data["count"] == exist_data["count"]:
            return True
        elif data["month"] == exist_data["month"] and data["year"] == exist_data["year"] and data["count"] != exist_data["count"]:
            return False
    return False
    
def change_data(data_list, data, index):
    data_list[index] = data