import random
from datetime import datetime, timedelta

def generate_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date

def date_to_seconds(date):
    return round((date.year * 525948.766 + date.month * 43829.0639 + date.day * 1440) / 1000)

start_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2024-06-25', '%Y-%m-%d')

sql_statements = []
for i in range(1, 20001):
    mahoadon = f"HD{i:05d}"
    ngaythanhtoan = generate_date(start_date, end_date)
    i_ngaythanhtoan = date_to_seconds(ngaythanhtoan)
    tongtien = random.uniform(50000, 100000000)  # Giả định tổng tiền từ 10 đến 1000
    masanpham = f"SP{random.randint(1, 200):05d}"  # Giới hạn mã sản phẩm từ SP00001 đến SP00200
    makhachhang =  f"KH{str(i).zfill(5)}"

    sql = f"INSERT INTO HOADON (MAHOADON, NGAYTHANHTOAN, TONGTIEN, MASANPHAM, MAKHACHHANG, I_NGAYTHANHTOAN) VALUES ('{mahoadon}', '{ngaythanhtoan.strftime('%Y-%m-%d')}', {tongtien:.2f}, '{masanpham}', '{makhachhang}', {i_ngaythanhtoan});"
    sql_statements.append(sql)

# Lưu các câu lệnh SQL vào file
with open('hoadon_records.txt', 'w') as file:
    for statement in sql_statements:
        file.write(statement + '\n')

print("Hoàn thành việc tạo 20,000 câu lệnh SQL insert vào bảng HOADON.")
