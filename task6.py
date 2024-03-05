def multiplying(my_dict):
    result = 1
    for key in my_dict:
        result = result * my_dict[key]
    return result


print(multiplying(my_dict={'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}))

