import csv
f = open("adult.data", "r")
i = 0
# data_list = ['age', 'work class', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
data_list = []
for item in f:
    tmp_list = []
    for item1 in item.split(","):
        tmp_list.append(item1)
    data_list.append(tmp_list)

headers = ['age', 'work class', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
               'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

with open('adult.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in data_list:
        # print(row)
        print([item.strip() for item in row])
        writer.writerow([item.strip() for item in row])