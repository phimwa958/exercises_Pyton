// ฟังก์ชันสำหรับเริ่มเกมเดาตัวเลข
function showNumberGuess() {
    document.getElementById('game-selection').innerHTML = `
        <h2>Number Guessing Game</h2>
        <input type="number" id="guess-input" placeholder="Enter a number (1-199)">
        <button onclick="submitGuess()">Submit Guess</button>
        <div id="guess-result"></div>
    `;
}

// ฟังก์ชันสำหรับส่งการเดา
function submitGuess() {
    const userGuess = parseInt(document.getElementById('guess-input').value);
    if (isNaN(userGuess)) {
        document.getElementById('guess-result').innerText = 'Please enter a valid number.';
        return;
    }
    fetch('/guess_number', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ guess: userGuess })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('guess-result').innerText = `Result: ${data.result}`;
    });
}

// ฟังก์ชันสำหรับเริ่มเกมทอยลูกเต๋า
function startDiceGame() {
    document.getElementById('game-selection').innerHTML = `
        <h2>Roll the Dice</h2>
        <button onclick="rollDice()">Roll Dice</button>
        <div id="dice-result"></div>
    `;
}

// ฟังก์ชันทอยลูกเต๋าและแสดงผล
function rollDice() {
    fetch('/roll_dice')
        .then(response => response.json())
        .then(data => {
            document.getElementById('dice-result').innerText = `You rolled: ${data.result}`;
        });
}

// ฟังก์ชันแสดงตัวเลือกเกมเป่ายิ้งฉุบ
function showRPS() {
    document.getElementById('game-selection').innerHTML = `
        <h2>Rock, Paper, Scissors</h2>
        <button onclick="playRPS('rock')">Rock</button>
        <button onclick="playRPS('paper')">Paper</button>
        <button onclick="playRPS('scissors')">Scissors</button>
        <div id="rps-result"></div>
    `;
}

// ฟังก์ชันเล่นเป่ายิ้งฉุบ
function playRPS(userChoice) {
    fetch('/rock_paper_scissors', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ choice: userChoice })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('rps-result').innerText = `Result: ${data.result}`;
    });
}

// ฟังก์ชันแสดงตัวเลือกการโยนเหรียญ
function showCoinFlip() {
    document.getElementById('game-selection').innerHTML = `
        <h2>Flip Coin</h2>
        <button onclick="flipCoin('heads')">Heads</button>
        <button onclick="flipCoin('tails')">Tails</button>
        <div id="coin-flip-result"></div>
    `;
}

// ฟังก์ชันการโยนเหรียญ
function flipCoin(userGuess) {
    fetch('/flip_coin', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ guess: userGuess })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('coin-flip-result').innerText = `Result: ${data.result}`;
    });
}
