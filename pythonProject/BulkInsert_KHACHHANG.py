import sqlite3
import re


def read_sql_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def parse_sql_line(line):
    # Sử dụng regex để trích xuất các giá trị từ câu lệnh SQL
    pattern = r'VALUES\((.*?)\);'
    match = re.search(pattern, line)
    if match:
        values = match.group(1).split(", ")
        # Chuyển đổi các giá trị phù hợp
        parsed_values = (
            values[0].strip("'"),
            values[1].strip("'"),
            values[2].strip("'"),
            values[3].strip("'"),
            values[4].strip("'"),
            values[5].strip("'"),
            values[6].strip("'"),
            values[7].strip("'"),
            values[8].strip("'"),
            values[9].strip("'"),
            int(values[10].strip("'")),
            values[11].strip("'"),
            values[12].strip("'"),
            values[13].strip("'"),
            values[14].strip("'"),
            values[15].strip("'"),
            values[16].strip("'"),
            int(values[17].strip("'"))
        )
        return parsed_values
    return None


def bulk_insert_from_file(file_path, db_name='QuanLyPhongGym.db', table='KHACHHANG'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = f'''INSERT INTO {table}(MATHE, HOTEN, NGAYSINH, CMND, SDT, EMAIL, GHICHU, NGAYDANGKY, NGAYHETHAN, TENPT, THOIHAN, ANH, MAGOITAP, GOITAPPT, MANHANVIEN, GIOITINH, DIACHI, I_NGAYDANGKY) 
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

    lines = read_sql_from_file(file_path)
    data = [parse_sql_line(line) for line in lines if parse_sql_line(line) is not None]

    # Chia dữ liệu thành các phần nhỏ hơn (ví dụ: 1000 bản ghi mỗi phần)
    chunk_size = 1000
    for i in range(0, len(data), chunk_size):
        cursor.executemany(sql, data[i:i + chunk_size])
        conn.commit()

    conn.close()
    print("Data inserted successfully.")


# Đường dẫn đến tệp chứa các câu lệnh SQL
file_path = 'khachhang_records.txt'
bulk_insert_from_file(file_path)
