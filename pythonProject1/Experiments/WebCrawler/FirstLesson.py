import pandas as pd

states = ['California', 'Texas', 'Florida', 'New York']
population = [3123123, 12321, 212351, 95123]
dict_state = {'State' : states, 'Population' : population}

df_states = pd.DataFrame.from_dict(dict_state)
print(df_states)

#handling exception errors: Try-except
new_list = [2, 4, 6, 'California']

for element in new_list:
    try:
        print(element/2)
    except:
        print('The element is not a numb')