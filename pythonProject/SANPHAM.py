import random

def generate_sql_insert():
    products = [
        "Thịt gà nướng", "Cá hồi", "Ức gà luộc", "Thịt bò nạc", "Thịt heo nạc", "Trứng gà", "Sữa chua không đường",
        "Sữa tươi không đường", "Hạt chia", "Hạt lanh", "Hạt bí ngô", "Hạt hướng dương", "Hạt hạnh nhân", "Hạt điều",
        "Hạt óc chó", "Yến mạch", "Gạo lứt", "Quinoa", "Lúa mạch", "Khoai lang", "Khoai tây", "Bông cải xanh",
        "Cải bó xôi", "Rau cải xanh", "Rau dền", "Cải thìa", "Cà rốt", "Dưa chuột", "Cà chua", "Ớt chuông", "Bơ",
        "Chuối", "Táo", "Dâu tây", "Việt quất", "Mâm xôi", "Đào", "Xoài", "Đậu phộng", "Đậu nành", "Đậu lăng",
        "Đậu hà lan", "Đậu đen", "Đậu trắng", "Đậu xanh", "Đậu đỏ", "Tôm", "Cua", "Sò điệp", "Hàu", "Mực",
        "Bạch tuộc", "Cá ngừ", "Cá trích", "Cá thu", "Cá mòi", "Sữa đậu nành", "Sữa hạnh nhân", "Sữa yến mạch",
        "Phô mai Cottage", "Phô mai Mozzarella", "Bánh mì ngũ cốc nguyên hạt", "Bánh mì lúa mạch", "Bánh mì đen",
        "Mì ống nguyên hạt", "Mì soba", "Mì gạo lứt", "Hạt diêm mạch", "Trà xanh", "Trà đen", "Nước lọc", "Nước dừa",
        "Nước ép cà rốt", "Nước ép cần tây", "Nước ép cam", "Nước ép táo", "Nước ép dứa", "Nước ép củ dền",
        "Sinh tố xanh", "Sinh tố dâu", "Sinh tố chuối", "Sinh tố xoài", "Sinh tố bơ", "Sinh tố việt quất",
        "Bột protein", "Bột casein", "Bột whey", "Bột đậu nành", "Bột gạo lứt", "Bột yến mạch", "Bột hạnh nhân",
        "Bột diêm mạch", "Hạt kê", "Hạt óc chó", "Hạt mắc ca", "Hạt đậu phộng", "Hạt đậu nành", "Hạt đậu xanh",
        "Hạt đậu lăng", "Hạt đậu hà lan", "Tạ đơn", "Tạ đòn", "Ghế tập ngực", "Máy chạy bộ", "Xe đạp tập",
        "Máy ép ngực", "Máy ép chân", "Máy kéo xô", "Máy tập bụng", "Băng quấn cổ tay", "Dây kéo đàn hồi",
        "Quả bóng tập yoga", "Thảm tập yoga", "Tạ chuông", "Thanh kéo xà", "Máy tập cơ bụng", "Máy tập đùi",
        "Máy tập bắp chân", "Máy tập lưng", "Ghế nghiêng tập bụng", "Ghế tập đùi sau", "Thảm tập sàn",
        "Găng tay tập gym", "Dây nhảy", "Dây kháng lực", "Bộ tạ mini", "Thanh đẩy", "Thanh tập xà đơn", "Tạ miếng",
        "Máy rung giảm mỡ", "Máy ép mông", "Máy tập cơ vai", "Máy tập cơ lưng", "Ghế tập cơ lưng", "Máy tập cơ tay",
        "Máy tập chân", "Máy tập eo", "Tạ đĩa", "Bộ tạ đa năng", "Máy tập toàn thân", "Máy tập eo", "Máy tập cơ ngực",
        "Máy tập cơ đùi", "Máy tập cơ bụng", "Máy tập bắp tay", "Máy tập cơ mông", "Bộ ghế đa năng", "Máy tập eo",
        "Máy tập cơ tay trước", "Máy tập cơ tay sau", "Máy tập cơ vai", "Máy tập chân", "Máy tập ngực", "Máy tập lưng",
        "Máy tập bụng", "Máy tập cơ liên sườn", "Ghế tập tạ", "Bộ dây nhảy", "Dây đàn hồi", "Tạ nhựa", "Tạ xi măng",
        "Bộ khung tập xà", "Bộ khung tập xà đơn", "Bộ khung tập xà kép", "Bộ khung tập xà 3 trong 1",
        "Bộ ghế ngồi tập tạ", "Bộ ghế nằm tập tạ", "Bộ ghế điều chỉnh được độ nghiêng", "Tạ bánh xe", "Tạ đĩa cao su",
        "Tạ đĩa thép", "Máy đạp đùi", "Máy kéo dây", "Máy tập cơ tay trước", "Máy tập cơ tay sau", "Máy tập chân",
        "Máy tập ngực", "Máy tập bụng", "Máy tập eo", "Ghế tập cơ bụng", "Ghế tập cơ tay", "Ghế tập cơ ngực",
        "Ghế tập cơ chân", "Ghế tập cơ lưng", "Ghế tập cơ vai", "Ghế tập cơ eo", "Bộ ghế tập đa năng", "Máy tập cơ bụng",
        "Máy tập cơ tay", "Máy tập cơ ngực", "Máy tập cơ chân", "Máy tập cơ lưng", "Máy tập cơ vai", "Máy tập cơ eo",
        "Máy tập bụng", "Máy tập tay", "Máy tập ngực", "Máy tập lưng", "Máy tập chân", "Máy tập vai"
    ]

    sql_statements = []
    product_id = 1

    for product in products:
        masanpham = f"SP{str(product_id).zfill(4)}"
        loaisanpham = "thực phẩm" if product in products[:101] else "dụng cụ thể dục"
        tensanpham = product
        giathanh = random.randint(50000, 10000000) if loaisanpham == "thực phẩm" else random.randint(100000, 10000000)
        soluong = random.randint(50, 100)
        donvi = "cái"
        anh = ""

        sql_statement = f"INSERT INTO SANPHAM (MASANPHAM, LOAISANPHAM, TENSANPHAM, GIATHANH, SOLUONG, DONVI, ANH) VALUES ('{masanpham}', '{loaisanpham}', '{tensanpham}', {giathanh}, {soluong}, '{donvi}', '{anh}');"
        sql_statements.append(sql_statement)

        product_id += 1

    return sql_statements

# Generate the SQL statements
sql_statements = generate_sql_insert()

# Save SQL statements to file with utf-8 encoding
with open("sanpham_records.txt", "w", encoding="utf-8") as file:
    for statement in sql_statements:
        file.write(statement + "\n")

print("SQL statements have been written to sanpham.sql")
