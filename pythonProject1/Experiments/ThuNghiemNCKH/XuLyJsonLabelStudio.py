import json
import csv

filename = "hung-8-10-2024"
with open('MrDuy_Absa_Labeling/Json/Unprocess/' + filename + '.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


annotation_data = []

for item in data:
    annotations = item.get('annotations', [])
    for annotation in annotations:
        annotation_inner_id = item.get('inner_id')
        data_text = item.get('data').get('text')
        result = annotation.get('result', [])
        values = []
        for res in result:
            value = res.get('value')
            selected_value = {
                'start': value.get('start'),
                'end': value.get('end'),
                'text': value.get('text'),
                'labels': value.get('labels')
            }
            values.append(selected_value)
        annotation_data.append(
            {
                'annotation_id': annotation_inner_id,
                'full_text': data_text,
                'values': values
            }
        )

# Write the JSON data to a file
with open('MrDuy_Absa_Labeling/Json/Process/output' + filename + '.json', 'w', encoding='utf-8') as outfile:
    json.dump(annotation_data, outfile, ensure_ascii=False, indent=4)

print("JSON data has been written to outputDuy.json")

data_list = []

aspects = [
    'Teaching quality', 'Course information', 'Learning environment',
    'Support from lecturers', 'Organization and management', 'Workload', 'General review',  'Test and evaluation'
]

sentiments = [
    'Positive', 'Negative', 'Neutral'
]

headers = ['id', 'Review', 'Sentence Component', 'aspect_text', 'aspect', 'sentiment_text', 'sentiment']


for annotation in annotation_data:
    tmp_list = []
    count = 0
    tmp_list.append(annotation['annotation_id'])
    tmp_list.append(annotation['full_text'])
    for value in annotation['values']:
        # Check if the label is 'Sentence Component'
        if value.get('labels') == ['Sentence Component']:
            count += 1
            if count > 1:
                data_list.append(tmp_list.copy())
                print(tmp_list)
                tmp_list.clear()
                tmp_list.append(annotation['annotation_id'])
                tmp_list.append(annotation['full_text'])
                tmp_list.append(value.get('text'))
            else:
                tmp_list.append(value.get('text'))
        # Check if the label matches any aspect in the aspects list
        elif value.get('labels') and value['labels'][0] in aspects:
            if value.get('labels')[0] in tmp_list:
                tmp_list[tmp_list.index(value.get('labels')[0]) - 1] = tmp_list[tmp_list.index(value.get('labels')[0]) - 1] + ',' + value.get('text')
            else:
                tmp_list.append(value.get('text'))
                tmp_list.append(value.get('labels')[0])
        elif value.get('labels') and value['labels'][0] in sentiments:
            if value.get('labels')[0] in tmp_list:
                tmp_list[tmp_list.index(value.get('labels')[0]) - 1] = tmp_list[tmp_list.index(value.get('labels')[0]) - 1] + ',' + value.get('text')
            else:
                tmp_list.append(value.get('text'))
                tmp_list.append(value.get('labels')[0])

    print(tmp_list)
    print("-------------end--------------")
    data_list.append(tmp_list)

with open('MrDuy_Absa_Labeling/Csv/Convert' + filename + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in data_list:
        # print(row)
        writer.writerow([item.strip() if isinstance(item, str) else item for item in row])
