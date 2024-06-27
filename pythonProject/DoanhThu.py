import math
import random
from datetime import datetime, timedelta

def calculate_i_ngay_tong_ket(date):
    # Công thức tính giây có thể cần điều chỉnh
    seconds = round((date.year * 525948.766 + date.month * 43829.0639 + date.day * 1440) / 1000)
    return seconds

start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 6, 25)

records = []
current_date = start_date
id_number = 1

while current_date <= end_date:
    i_ngay = calculate_i_ngay_tong_ket(current_date)
    tienthu = random.randint(100000000, 999999999)
    records.append((f"MADOANHTHU{str(id_number).zfill(3)}", tienthu, current_date.strftime("%Y-%m-%d"), i_ngay))
    current_date += timedelta(days=1)
    id_number += 1

# Ghi dữ liệu vào file
with open('doanhthu_record.txt', 'w') as file:
    for record in records:
        file.write(f'INSERT INTO DOANHTHU(MADOANHTHU, TIENTHU, NGAYTONGKETDOANHTHU, I_NGAYTONGKETDOANHTHU) VALUES("{record[0]}", {record[1]}, "{record[2]}", {record[3]});\n')
