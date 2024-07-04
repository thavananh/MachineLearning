import math
import random
from datetime import datetime, timedelta

def calculate_i_ngay_phat_sinh(date):
    # Công thức tính giây có thể cần điều chỉnh
    seconds = round((date.year * 525948.766 + date.month * 43829.0639 + date.day * 1440) / 1000)
    return seconds

start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 7, 2)

records = []
current_date = start_date

while current_date <= end_date:
    i_ngay = calculate_i_ngay_phat_sinh(current_date)
    id_number = "CP" + current_date.strftime("%Y%m%d")
    tongchiphi = random.randint(100000000, 999999999)
    records.append((f"{str(id_number).zfill(3)}", current_date.strftime("%Y-%m-%d"), tongchiphi, i_ngay))
    current_date += timedelta(days=1)

# Ghi dữ liệu vào file
with open('chiphi_record.txt', 'w') as file:
    for record in records:
        file.write(f'INSERT INTO CHIPHI(MACHIPHI, NGAYPHATSINH, TONGCHIPHI, I_NGAYPHATSINH) VALUES("{record[0]}", "{record[1]}", {record[2]}, {record[3]});\n')
