import sqlite3
import re


def read_sql_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def parse_sql_line(line):
    # Sử dụng regex để trích xuất các giá trị từ câu lệnh SQL
    pattern = r'VALUES\((.*?)\);'
    match = re.search(pattern, line)
    if match:
        values = match.group(1).split(', ')
        # Chuyển đổi các giá trị phù hợp
        parsed_values = (
            values[0].strip('"'),
            int(values[1]),
            values[2].strip('"'),
            int(values[3])
        )
        return parsed_values
    return None


def bulk_insert_from_file(file_path, db_name='QuanLyPhongGym.db', table='DOANHTHU'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = f'''INSERT INTO {table}(MADOANHTHU, TIENTHU, NGAYTONGKETDOANHTHU, I_NGAYTONGKETDOANHTHU) 
              VALUES (?, ?, ?, ?)'''

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
file_path = 'doanhthu_record.txt'
bulk_insert_from_file(file_path)
