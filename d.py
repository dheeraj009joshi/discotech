def AddTwoNumbers(list1,list2):
    lists_of_lists = [list1, list2]
    aa=[sum(x) for x in zip(*lists_of_lists)]
    # -> [5, 7, 9]
    return str(aa).replace(","," ->").replace("[","").replace("]","")
result=AddTwoNumbers([1,9,2],[1,2,3])
print(result)