import random

def get_user_choice():
    choices = ['ค้อน', 'กระดาษ', 'กรรไกร', 'ตะปู']
    print("เลือกอย่างใดอย่างหนึ่ง: ค้อน, กระดาษ, กรรไกร, ตะปู")
    user_input = input("คุณเลือก: ").strip()
    if user_input in choices:
        return user_input
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")
        return get_user_choice()

def get_computer_choice():
    choices = ['ค้อน', 'กระดาษ', 'กรรไกร', 'ตะปู']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "เสมอ!"
    
    # กรรไกร/กระดาษ: กรรไกรชนะ
    if (user_choice == 'กรรไกร' and computer_choice == 'กระดาษ') or (user_choice == 'กระดาษ' and computer_choice == 'กรรไกร'):
        return "กรรไกรชนะ!"

    # กรรไกร/ตะปู: ตะปูชนะ
    if (user_choice == 'กรรไกร' and computer_choice == 'ตะปู') or (user_choice == 'ตะปู' and computer_choice == 'กรรไกร'):
        return "ตะปูชนะ!"

    # กรรไกร/ค้อน: ค้อนชนะ
    if (user_choice == 'กรรไกร' and computer_choice == 'ค้อน') or (user_choice == 'ค้อน' and computer_choice == 'กรรไกร'):
        return "ค้อนชนะ!"

    # ค้อน/ตะปู: ค้อนชนะ
    if (user_choice == 'ค้อน' and computer_choice == 'ตะปู') or (user_choice == 'ตะปู' and computer_choice == 'ค้อน'):
        return "ค้อนชนะ!"
    
    # ค้อน/กระดาษ: กระดาษชนะ
    if (user_choice == 'ค้อน' and computer_choice == 'กระดาษ') or (user_choice == 'กระดาษ' and computer_choice == 'ค้อน'):
        return "กระดาษชนะ!"
    
    # กระดาษ/ตะปู: ตะปูชนะ
    if (user_choice == 'กระดาษ' and computer_choice == 'ตะปู') or (user_choice == 'ตะปู' and computer_choice == 'กระดาษ'):
        return "ตะปูชนะ!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"คุณเลือก: {user_choice}")
    print(f"คอมพิวเตอร์เลือก: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# เริ่มเกม
if __name__ == "__main__":
    play_game()
