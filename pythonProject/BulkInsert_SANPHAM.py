import sqlite3
import re

def read_sql_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def parse_sql_line(line):
    pattern = r'VALUES\((.*?)\);'
    match = re.search(pattern, line)
    if match:
        values = match.group(1).split(', ')
        parsed_values = (
            values[0].strip("'"),
            values[1].strip("'"),
            values[2].strip("'"),
            int(values[3]),
            int(values[4]),
            values[5].strip("'"),
            values[6].strip("'")
        )
        return parsed_values
    return None

def bulk_insert_from_file(file_path, db_name='QuanLyPhongGym.db', table='SANPHAM'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = f'''INSERT INTO {table}(MASANPHAM, LOAISANPHAM, TENSANPHAM, GIATHANH, SOLUONG, DONVI, ANH) 
              VALUES (?, ?, ?, ?, ?, ?, ?)'''

    lines = read_sql_from_file(file_path)
    data = [parse_sql_line(line) for line in lines if parse_sql_line(line) is not None]

    chunk_size = 1000
    for i in range(0, len(data), chunk_size):
        cursor.executemany(sql, data[i:i + chunk_size])
        conn.commit()

    conn.close()
    print("Data inserted successfully.")

# Đường dẫn đến tệp chứa các câu lệnh SQL
file_path = 'sanpham_records.txt'
bulk_insert_from_file(file_path)
