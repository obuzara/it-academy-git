def pythonist_dict(str1='pythonist'):
    my_dict = {i: str1.count(i) for i in str1}
    return my_dict


print(pythonist_dict())
