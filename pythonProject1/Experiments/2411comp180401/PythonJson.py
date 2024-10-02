import json

# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])
#
# print(json.dumps(y, indent=4))

#Biểu diễn dữ liệu ở dạng mảng

ho_ten = input("Nhập họ tên SV: ")
mssv = input("Mã số SV: ")
diem_gk = float(input("Diểm giữa kỳ: "))
diem_ck = float(input("Điểm cuối kỳ: "))
thong_tin_diem = {
    "ho_ten": ho_ten,
    "mssv": mssv,
    "diem": [
        {"ma_mon": "COMP1804", "giua_ky": diem_gk, "cuoi_ky": diem_ck}
    ]
}

print(json.dumps(thong_tin_diem))
with open('student.json', 'w', encoding="utf8") as outfile:
    json.dump(thong_tin_diem, outfile, indent=4)

with open('student.json', 'r', encoding="utf8") as infile:
    data = json.load(infile)
    print(data)