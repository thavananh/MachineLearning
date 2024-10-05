import json
import csv

with open('formatted-duy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

annotation_data = []

for item in data:
    annotations = item.get('annotations', [])
    for annotation in annotations:
        annotation_inner_id = item.get('inner_id')
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
                'values': values
            }
        )

# Write the JSON data to a file
with open('output.json', 'w', encoding='utf-8') as outfile:
    json.dump(annotation_data, outfile, ensure_ascii=False, indent=4)

print("JSON data has been written to output.json")


