# ฟังก์ชันแปลง Celsius เป็น Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# ฟังก์ชันแปลง Fahrenheit เป็น Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("\nเลือกโหมดการแปลง:")
    print("1: แปลง Celsius เป็น Fahrenheit")
    print("2: แปลง Fahrenheit เป็น Celsius")
    print("พิมพ์ 'exit' เพื่อปิดโปรแกรม")

    choice = input("กรุณาเลือก (1, 2 หรือ exit): ").strip().lower()

    if choice == "exit":
        print("ปิดโปรแกรม...")
        break
    elif choice == "1":
        celsius = input("ป้อนอุณหภูมิใน Celsius: ").strip()
        if celsius.lower() == "exit":
            print("ปิดโปรแกรม...")
            break
        try:
            celsius = float(celsius)
            print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
        except ValueError:
            print("กรุณาป้อนตัวเลขที่ถูกต้อง!")
    elif choice == "2":
        fahrenheit = input("ป้อนอุณหภูมิใน Fahrenheit: ").strip()
        if fahrenheit.lower() == "exit":
            print("ปิดโปรแกรม...")
            break
        try:
            fahrenheit = float(fahrenheit)
            print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
        except ValueError:
            print("กรุณาป้อนตัวเลขที่ถูกต้อง!")
    else:
        print("กรุณาเลือก 1, 2 หรือ exit เท่านั้น!")
