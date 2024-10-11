function playGame(playerChoice) {
    console.log("Button clicked! Player choice: " + playerChoice);

    // Computer's choice (random)
    const choices = ['s', 'w', 'g'];
    const compChoice = choices[Math.floor(Math.random() * 3)];

    // Determine the winner
    const result = getWinner(compChoice, playerChoice);

    // Display results in the DOM
    document.getElementById("computer-choice").innerHTML = `Computer chose: ${convertToWord(compChoice)}`;
    document.getElementById("your-choice").innerHTML = `You chose: ${convertToWord(playerChoice)}`;
    document.getElementById("game-result").innerHTML = result;
}

// Function to decide the game winner
function getWinner(comp, player) {
    if (comp === player) {
        return "It's a tie!";
    } else if ((comp === 's' && player === 'g') || 
               (comp === 'w' && player === 's') || 
               (comp === 'g' && player === 'w')) {
        return "You win!";
    } else {
        return "You lose!";
    }
}

// Function to convert shorthand to full word
function convertToWord(letter) {
    if (letter === 's') return 'Snake';
    if (letter === 'w') return 'Water';
    return 'Gun';
}
