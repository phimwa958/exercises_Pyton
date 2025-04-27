def binary_to_other(value):
    decimal = int(value, 2)
    return {
        'binary': value,
        'octal': oct(decimal)[2:],
        'decimal': decimal,
        'hexadecimal': hex(decimal)[2:].upper()
    }

def octal_to_other(value):
    decimal = int(value, 8)
    return {
        'binary': bin(decimal)[2:],
        'octal': value,
        'decimal': decimal,
        'hexadecimal': hex(decimal)[2:].upper()
    }

def decimal_to_other(value):
    decimal = int(value)
    return {
        'binary': bin(decimal)[2:],
        'octal': oct(decimal)[2:],
        'decimal': value,
        'hexadecimal': hex(decimal)[2:].upper()
    }

def hexadecimal_to_other(value):
    decimal = int(value, 16)
    return {
        'binary': bin(decimal)[2:],
        'octal': oct(decimal)[2:],
        'decimal': decimal,
        'hexadecimal': value.upper()
    }

def main():
    while True:
        print("\nเลือกฐานที่ต้องการแปลง:")
        print("1. ฐานสอง (Binary)")
        print("2. ฐานแปด (Octal)")
        print("3. ฐานสิบ (Decimal)")
        print("4. ฐานสิบหก (Hexadecimal)")
        print("5. ออกจากโปรแกรม (Exit)")

        choice = input("กรุณาเลือก (1/2/3/4/5): ")

        if choice == '5':  # Exit
            print("ขอบคุณที่ใช้โปรแกรม! ออกจากโปรแกรมแล้ว")
            break

        value = input("กรุณากรอกค่าที่ต้องการแปลง: ")

        if choice == '1':  # Binary
            result = binary_to_other(value)
        elif choice == '2':  # Octal
            result = octal_to_other(value)
        elif choice == '3':  # Decimal
            result = decimal_to_other(value)
        elif choice == '4':  # Hexadecimal
            result = hexadecimal_to_other(value)
        else:
            print("ตัวเลือกไม่ถูกต้อง")
            continue

        print("\nผลลัพธ์การแปลง:")
        for base, val in result.items():
            print(f"{base.capitalize()}: {val}")

if __name__ == "__main__":
    main()