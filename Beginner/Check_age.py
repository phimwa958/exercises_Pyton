def check_age(age):
    if age >= 18:
        return "เป็นผู้ใหญ่"
    else:
        return "ยังเป็นเด็ก"

def main():
    while True:
        value = input("กรุณากรอกอายุ (พิมพ์ 'exit' เพื่อออกจากโปรแกรม): ")

        if value.lower() == 'exit':
            print("ขอบคุณที่ใช้โปรแกรม! ออกจากโปรแกรมแล้ว")
            break

        try:
            age = int(value)
            result = check_age(age)
            print(result)
        except ValueError:
            print("กรุณากรอกอายุเป็นตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    main()
