#

def get_lowest_list_value(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    
    lowest = lst[0]
    for num in lst[1:]:
        if num < lowest:
            lowest = num
    return lowest

def get_highest_list_value(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    
    highest = lst[0]
    for num in lst[1:]:
        if num > highest:
            highest = num
    return highest