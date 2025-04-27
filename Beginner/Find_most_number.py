def find_max_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    while True:
        value = input("กรุณากรอก 3 ตัวเลขคั่นด้วยช่องว่าง (พิมพ์ 'exit' เพื่อออกจากโปรแกรม): ")

        if value.lower() == 'exit':
            print("ขอบคุณที่ใช้โปรแกรม! ออกจากโปรแกรมแล้ว")
            break

        try:
            num1, num2, num3 = map(int, value.split())
            if len([num1, num2, num3]) == 3:
                max_num = find_max_number(num1, num2, num3)
                print(f"เลขที่มากที่สุดคือ: {max_num}")
            else:
                print("กรุณากรอกตัวเลข 3 ตัว")
        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()