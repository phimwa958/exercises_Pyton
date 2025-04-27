def print_multiplication_table():
    for i in range(2, 26):  # สำหรับแม่ 2 ถึง 25
        print(f"ตารางสูตรคูณของ {i}:")
        for j in range(1, 13):  # คูณ 1 ถึง 12
            print(f"{i} x {j} = {i * j}")
        print()  # พิมพ์เว้นบรรทัดหลังแต่ละตาราง

if __name__ == "__main__":
    print_multiplication_table()
