from flask import Flask, jsonify, request, render_template 
import random

app = Flask(__name__)

# กำหนดตัวเลขที่ต้องเดา
target_number = random.randint(1, 199)
guess_count = 0

@app.route('/')
def home():
    return render_template('game.html')  # Render หน้า HTML

@app.route('/guess_number', methods=['POST'])
def guess_number():
    global target_number, guess_count
    user_guess = int(request.json['guess'])
    guess_count += 1

    if user_guess < 1 or user_guess > 199:
        return jsonify(result="กรุณาเดาตั้งแต่ 1-199")
    elif user_guess == target_number:
        response = f"ถูกต้อง! คุณเดาไปทั้งหมด {guess_count} ครั้ง"
        # รีเซ็ตค่าหลังจากจบเกม
        target_number = random.randint(1, 199)
        guess_count = 0
        return jsonify(result=response)
    else:
        if user_guess < target_number:
            return jsonify(result="มากกว่านี้")
        else:
            return jsonify(result="น้อยกว่านี้")

@app.route('/roll_dice', methods=['GET'])
def roll_dice():
    result = random.randint(1, 6)
    return jsonify(result=result)

@app.route('/rock_paper_scissors', methods=['POST'])
def rock_paper_scissors():
    user_choice = request.json['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "Draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"
    return jsonify(result=result)

@app.route('/flip_coin', methods=['POST'])
def flip_coin():
    user_guess = request.json['guess']
    result = random.choice(['heads', 'tails'])
    if user_guess == result:
        return jsonify(result="Correct!")
    else:
        return jsonify(result="Incorrect!")

if __name__ == '__main__':
    app.run(debug=True)
