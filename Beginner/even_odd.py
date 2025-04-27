def check_even_odd(number):
    if number % 2 == 0:
        return "เลขคู่"
    else:
        return "เลขคี่"

def main():
    while True:
        value = input("กรุณากรอกตัวเลข (พิมพ์ 'exit' เพื่อออกจากโปรแกรม): ")

        if value.lower() == 'exit':
            print("ขอบคุณที่ใช้โปรแกรม! ออกจากโปรแกรมแล้ว.")
            break

        try:
            number = int(value)
            result = check_even_odd(number)
            print(f"{number} เป็น {result}")
        except ValueError:
            print("กรุณากรอกตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()
