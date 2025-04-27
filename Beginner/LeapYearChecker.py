def is_leap_year(year):
    # ปีอธิกสุรทินจะต้องเป็นปีที่หารด้วย 4 ลงตัว แต่ไม่หารด้วย 100 ลงตัว
    # หรือหารด้วย 400 ลงตัว
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    while True:
        value = input("กรุณากรอกปี (พิมพ์ 'exit' เพื่อออกจากโปรแกรม): ")

        if value.lower() == 'exit':
            print("ขอบคุณที่ใช้โปรแกรม! ออกจากโปรแกรมแล้ว")
            break

        try:
            year = int(value)
            if is_leap_year(year):
                print(f"{year} เป็นปีอธิกสุรทิน")
            else:
                print(f"{year} ไม่เป็นปีอธิกสุรทิน")
        except ValueError:
            print("กรุณากรอกปีเป็นตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()
