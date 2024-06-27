import random
from datetime import datetime, timedelta

# Danh sách tên
ho = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Phan", "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý",
      "Đinh", "Trương", "Hà", "Mai", "Tô", "Vương"]
ten_dem_nam = ["Anh", "Bảo", "Chí", "Công", "Đình", "Gia", "Hoàng", "Hữu", "Minh", "Quốc", "Thành", "Trường", "Văn",
               "Xuân", "Đức"]
ten_dem_nu = ["Ái", "Bảo", "Cẩm", "Diệu", "Hồng", "Khánh", "Kim", "Lan", "Minh", "Ngọc", "Phương", "Thanh", "Thu",
              "Thùy", "Yến"]
ten_nam = ["Anh Tuấn", "Bảo Long", "Chí Dũng", "Đăng Khoa", "Hùng Cường", "Minh Quân", "Nhật Minh", "Phúc Thịnh",
           "Quốc Huy", "Thành Đạt"]
ten_nu = ["Anh Thư", "Bảo Ngọc", "Diệu Linh", "Hồng Nhung", "Khánh Linh", "Minh Châu", "Ngọc Anh", "Phương Mai",
          "Thảo Vy", "Trúc Quỳnh"]

# Địa chỉ
duong = ["Đường Nguyễn Huệ", "Đường Lê Lợi", "Đường Trần Hưng Đạo", "Đường Lý Thái Tổ", "Đường Nguyễn Trãi",
         "Đường Phan Đình Phùng", "Đường Hai Bà Trưng", "Đường Võ Nguyên Giáp", "Đường Điện Biên Phủ",
         "Đường Cách Mạng Tháng Tám", "Đường An Dương Vương", "Đường Bạch Đằng"]

# Gói tập
goitap_dict = {
    'GOITAP0001': 1,
    'GOITAP0002': 1,
    'GOITAP0003': 1,
    'GOITAP0004': 1
}

goitappt_dict = {
    'GOITAPPT0001': 1,
    'GOITAPPT0002': 1,
    'GOITAPPT0003': 1,
    'GOITAPPT0004': 1
}

# Hàm tạo họ tên ngẫu nhiên
def tao_ho_ten():
    gioi_tinh = random.choice(["nam", "nữ"])
    ho_chon = random.choice(ho)
    ten_dem_chon = random.choice(ten_dem_nam if gioi_tinh == "nam" else ten_dem_nu)
    ten_chon = random.choice(ten_nam if gioi_tinh == "nam" else ten_nu)
    return f"{ho_chon} {ten_dem_chon} {ten_chon}", gioi_tinh

# Hàm tạo ngày sinh ngẫu nhiên
def tao_ngay_sinh():
    start_date = datetime(1960, 1, 1)
    end_date = datetime(2010, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

# Hàm tạo CMND ngẫu nhiên
def tao_cmnd():
    length = random.choice([9, 12])
    return ''.join([str(random.randint(1, 9)) for _ in range(length)])

# Hàm tạo ngày đăng ký ngẫu nhiên
def tao_ngay_dang_ky():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 6, 25)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d"), tinh_i_ngay_dang_ky(random_date)

# Hàm tính I_NGAYDANGKY theo công thức mới
def tinh_i_ngay_dang_ky(ngay_dang_ky):
    return int(round((ngay_dang_ky.year * 525948.766 + ngay_dang_ky.month * 43829.0639 + ngay_dang_ky.day * 1440) / 1000))

# Hàm tạo ngày hết hạn
def tao_ngay_het_han(ngay_dang_ky, ma_goi_tap):
    ngay_dk = datetime.strptime(ngay_dang_ky, "%Y-%m-%d")
    thoi_han = goitap_dict.get(ma_goi_tap, 1)
    ngay_hh = ngay_dk + timedelta(days=thoi_han * 30)
    return ngay_hh.strftime("%Y-%m-%d")

# Hàm tạo địa chỉ ngẫu nhiên
def tao_dia_chi():
    so_nha = random.randint(1, 1000)
    ten_duong = random.choice(duong)
    quan = random.randint(1, 10)
    return f"{so_nha} {ten_duong}, Quận {quan}"

# Tạo các trường khác
def tao_ma_goi_tap():
    return random.choice(list(goitap_dict.keys()))

def tao_goi_tap_pt(ma_goi_tap):
    return 1 if 'PT' in ma_goi_tap else 0

def tao_ten_pt():
    return tao_ho_ten()[0]

def tao_ma_nhan_vien():
    return tao_ho_ten()[0]

# Tạo một bản ghi
def tao_ban_ghi(i):
    ho_ten, gioi_tinh = tao_ho_ten()
    ngay_sinh = tao_ngay_sinh()
    cmnd = tao_cmnd()
    sdt = "0" + ''.join([str(random.randint(0, 9)) for _ in range(9)])
    email = ho_ten.lower().replace(" ", "") + "@example.com"
    ghi_chu = "Ghi chú mẫu"
    ngay_dang_ky, i_ngay_dang_ky = tao_ngay_dang_ky()
    ma_goi_tap = tao_ma_goi_tap()
    ngay_het_han = tao_ngay_het_han(ngay_dang_ky, ma_goi_tap)
    ten_pt = tao_ten_pt()
    ma_nhan_vien = tao_ma_nhan_vien()
    goi_tap_pt = tao_goi_tap_pt(ma_goi_tap)
    dia_chi = tao_dia_chi()

    ban_ghi = {
        "MATHE": f"KH{str(i).zfill(5)}",
        "HOTEN": ho_ten,
        "NGAYSINH": ngay_sinh,
        "CMND": cmnd,
        "SDT": sdt,
        "EMAIL": email,
        "GHICHU": ghi_chu,
        "NGAYDANGKI": ngay_dang_ky,
        "NGAYHETHAN": ngay_het_han,
        "TENPT": ten_pt,
        "THOIHAN": goitap_dict[ma_goi_tap],
        "ANH": "",
        "MAGOITAP": ma_goi_tap,
        "GOITAPPT": goi_tap_pt,
        "MANHANVIEN": ma_nhan_vien,
        "GIOITINH": gioi_tinh,
        "DIACHI": dia_chi,
        "I_NGAYDANGKI": i_ngay_dang_ky
    }

    return ban_ghi

# Tạo câu lệnh SQL từ bản ghi
def tao_sql_insert(ban_ghi):
    columns = ', '.join(ban_ghi.keys())
    values = ', '.join([f"'{str(v)}'" for v in ban_ghi.values()])
    return f"INSERT INTO KHACHHANG ({columns}) VALUES ({values});"

# Tạo 19834 bản ghi và ghi vào file
ban_ghi_list = [tao_ban_ghi(i + 1) for i in range(19834)]
sql_list = [tao_sql_insert(ban_ghi) for ban_ghi in ban_ghi_list]

# Ghi vào file với mã hóa UTF-8
with open('khachhang_records.txt', 'w', encoding='utf-8') as f:
    for sql in sql_list:
        f.write(sql + '\n')

