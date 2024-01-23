# # содержание товаров в магазинах
# stores = {
#     'Магнит': {'молоко', 'соль', 'сахар'},
#     'Пятерочка': {'мясо', 'молоко', 'сыр'},
#     'Перекресток': {'молоко', 'творог', 'сыр'},
# }
#
# # переменные для ответов
# no_cheese = []
# milk_and_sugar = []
# salt_exist = []
#
# for key, value in stores.items():
#     if 'сыр' not in value:
#         no_cheese.append(key)
#     if {'молоко', 'сахар'}.issubset(value):
#         milk_and_sugar.append(key)
#     if 'соль' in value:
#         salt_exist.append(key)
#
# print('Нельзя приобрести сыр в:', ', '.join(no_cheese))
# print('Можно приобрести одновременно молоко и сахар в:', ', '.join(milk_and_sugar))
# print('Можно приобрести соль в:', ', '.join(salt_exist))


"""
В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
1. в каких магазинах нельзя приобрести сыр.
2. в каких магазинах можно приобрести одновременно молоко и сахар.
3. в каких магазинах можно приобрести соль.
"""


# товары
milk = {'молоко'}
meat = {'мясо'}
cheese = {'сыр'}
tvorog = {'творог'}
sugar = {'сахар'}
salt = {'соль'}

# содержание товаров в магазинах
stores = {
    'Магнит': milk | salt | sugar,
    'Пятерочка': meat | milk | cheese,
    'Перекресток': milk | tvorog | cheese,
}

for key, value in stores.items():
    if not cheese.issubset(value):
        print(f'Нельзя приобрести сыр в: {key}')
    if value.issuperset(milk.union(sugar)):
        print(f'Можно приобрести одновременно молоко и сахар в: {key}')
    if salt.intersection(value) == salt:
        print(f'Можно приобрести соль в: {key}')
