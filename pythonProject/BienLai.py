import math
import random
from datetime import datetime, timedelta

def calculate_i_ngay_thanh_toan(date):
    seconds = round((date.year * 525948.766 + date.month * 43829.0639 + date.day * 1440) / 1000)
    return seconds

# Từ điển mã gói tập và số tiền tương ứng
goitap_dict = {
    "GOITAP0001": 400000,
    "GOITAP0002": 500000,
    "GOITAP0003": 600000,
    "GOITAP0004": 800000,
    "GOITAP0005": 1000000
}

goitap_pt_dict = {
    "GOITAPT0001": 1100000,
    "GOITAPT0002": 1200000,
    "GOITAPT0003": 1300000,
    "GOITAPT0004": 1400000,
    "GOITAPT0005": 1500000
}

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

records = []
current_date = start_date
id_number = 1

while current_date <= end_date:
    i_ngay = calculate_i_ngay_thanh_toan(current_date)

    # Random số lượng khách hàng mới trong một ngày
    num_customers = random.randint(10, 100)

    for _ in range(num_customers):
        if id_number % 2 == 0:
            ma_goitap, tongtien = random.choice(list(goitap_pt_dict.items()))
            goitap_pt = 1
        else:
            ma_goitap, tongtien = random.choice(list(goitap_dict.items()))
            goitap_pt = 0

        ma_the = f"KH{str(id_number).zfill(5)}"
        ma_bien_lai = f"BLKH{str(id_number).zfill(5)}"

        records.append((ma_the, tongtien, current_date.strftime("%Y-%m-%d"), i_ngay, ma_bien_lai, ma_goitap, goitap_pt))
        id_number += 1

    current_date += timedelta(days=1)

# Ghi dữ liệu vào file txt
with open("bienlai_records.txt", "w") as file:
    for record in records:
        file.write(
            f'INSERT INTO BIENLAI(MATHE, TONGTIEN, NGAYTHANHTOAN, I_NGAYTHANHTOAN, MABIENLAI, MAGOITAP, GOITAPPT) VALUES("{record[0]}", {record[1]}, "{record[2]}", {record[3]}, "{record[4]}", "{record[5]}", {record[6]});\n'
        )
