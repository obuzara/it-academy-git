my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(**kwargs)


biggest_dict(login='HotTabH', password='123456789', username='Nagibator228', lvl=91)
biggest_dict(name='Мама', lvl=99, weight=61, answer_to_everything=42)
print(my_dict)