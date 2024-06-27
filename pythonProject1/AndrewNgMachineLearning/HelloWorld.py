tienLuong = 5000000
hsl = 1.475
hoTen = 'Lê Anh Thư'

strTT1 = f'Họ tên: {hoTen}\nTiền lương: {tienLuong}\nHệ số lương: {hsl}'
print(strTT1)

strTT2 = f'Họ tên: {hoTen}\nTiền lương: {tienLuong:,}\nHệ số lương: {hsl}'
print(strTT2)

strTT3 = f'Họ tên: {hoTen}\nTiền lương: {tienLuong:,.2f}\nHệ số lương: {hsl}'
print(strTT3)

k1 = eval('2+3+5')
k2 = eval('25')
k3 = eval('1.75')
k4 = eval('20,30,45')
k5 = eval('[12,13,14,15]')
k6 = eval('"abc"')

k = eval('abc') # báo lỗi vì nó nghĩ đây làm biến

print()