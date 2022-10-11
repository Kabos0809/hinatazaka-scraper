#挿入しようとするデータの存在確認を行います.

def is_data_exist(data_list, data):
    for exist_data in data_list:
        if data == exist_data:
            return True
            
    return False