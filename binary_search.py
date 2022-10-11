#binary search about date

def binary_search(list, event):
    i = len(list)/2
    while 1:
        if list[i]['date'] < event['date']:
            if i > len(list)/2:    
                i += (i - list(len(list)/2))/2
            else:
                i += ((len(list)/2)-i)/2
        elif list[i]['date'] > event['date']:
            if i > len(list)/2:
                i -= (i - len(list)/2)/2
            else:
                i /= 2
        elif list[i]['date'] == event['date']:
            break
    return i-1
            