from cs50 import get_string

pizzas = {
    "cheese": 10,
    "peperoni": 12,
    "bufalo": 14,
    "sweet": 8,
    "american": 6,
    "hawaian": 18,
}

expensivePizzas = dict((k, v) for k, v in pizzas.items() if v >= 10) # cria uma nova dict com pizzas caras acima de v = 10;
print(expensivePizzas) # {'cheese': 10, 'peperoni': 12, 'bufalo': 14, 'hawaian': 18}
print(f"{expensivePizzas.keys()}") # dict_keys(['cheese', 'peperoni', 'bufalo', 'hawaian'])
