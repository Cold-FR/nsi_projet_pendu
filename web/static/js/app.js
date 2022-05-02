function nextInput(inputs, input){
    const currentInput = parseInt(input.id.split('-')[1]);
    let nextInput = currentInput + 1;
    if(currentInput === inputs.length) nextInput -= inputs.length;
    document.getElementById(`letter-${nextInput}`).focus();
}

function previousInput(inputs, input) {
    const currentInput = parseInt(input.id.split('-')[1]);
    let previousInput = currentInput - 1;
    if(currentInput === (inputs.length + 1 - inputs.length)) previousInput = inputs.length;
    document.getElementById(`letter-${previousInput}`).focus();
}

const letters = document.querySelectorAll('.letter');
letters.forEach((letter) => {
    letter.addEventListener('keyup', (e) => {
            if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight' && e.key !== 'ArrowUp' && e.key !== 'ArrowDown' && e.key !== 'CapsLock' && e.key !== 'Backspace' && e.code !== 'Space') {
                nextInput(letters, letter);
            } else if (e.key === 'ArrowLeft' || e.key === 'Backspace') {
                previousInput(letters, letter);
            } else if (e.key === 'ArrowRight') {
                nextInput(letters, letter);
            } else if (e.code === 'Space') {
                e.target.value = '';
            }
    });
})