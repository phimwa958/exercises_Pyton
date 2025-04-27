name = input("กรุณากรอกข้อความ: ")  
num = int(input("กรุณากรอกตัวเลข: "))  
ft = float(input("กรุณากรอกทศนิยม: "))  

print(f"\nข้อมูลที่ได้รับ:")
print(f"ข้อความ: {name}")
print(f"ตัวเลข: {num}")
print(f"ทศนิยม: {ft}")

# แปลงชนิดข้อมูล
num_to_float = float(num)
str_to_int = int(name) if name.isdigit() else "ไม่สามารถแปลงเป็น int ได้"
float_to_int = int(ft)
num_to_str = str(num)
ft_to_str = str(ft)

print("\nผลลัพธ์การแปลงชนิดข้อมูล:")
print(f"int เป็น float: {num_to_float}")
print(f"str เป็น int: {str_to_int}")
print(f"float เป็น int: {float_to_int}")
print(f"int เป็น str: {num_to_str}")
print(f"float เป็น str: {ft_to_str}")
