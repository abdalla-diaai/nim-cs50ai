state = [1, 2, 3, 4]
action = (0, 1)


q_values = {
    (tuple(state), action) : 5
}

for key in q_values.keys():
    print(key)