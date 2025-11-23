def sum_nested(list):
    return sum(list[1]+sum(list[2]))
my_list= [[1,2],[3,4]]
print(sum_nested(my_list))