function nextInput(inputs, input, arrow = false){
    const currentInput = parseInt(input.id.split('-')[1]);
    let nextInput = currentInput + 1;
    if(currentInput === inputs.length && arrow) nextInput -= inputs.length;
    document.getElementById(`letter-${nextInput}`).focus();
}

function previousInput(inputs, input, arrow = false) {
    const currentInput = parseInt(input.id.split('-')[1]);
    let previousInput = currentInput - 1;
    if(currentInput === (inputs.length + 1 - inputs.length) && arrow) previousInput = inputs.length;
    document.getElementById(`letter-${previousInput}`).focus();
}

const wordForm = document.getElementById('game');
wordForm.addEventListener('submit', (e) => {
    e.preventDefault();
});

const letters = document.querySelectorAll('.letter');
letters.forEach((letter) => {
    letter.addEventListener('keydown', (e) => {
        if(e.altKey || e.key === 'AltGraph' || e.ctrlKey || e.metaKey || e.shiftKey || e.key === 'ArrowDown' || e.key === 'ArrowUp' || e.key === 'CapsLock') return;
        if(e.key !== 'ArrowLeft' && e.key !== 'ArrowRight' && e.code !== 'Space') e.target.value = '';
        setTimeout(() => {
            if (e.key === 'ArrowLeft' || e.key === 'Backspace') {
                previousInput(letters, letter, true);
            } else if (e.key === 'ArrowRight') {
                nextInput(letters, letter, true);
            } else if (e.code === 'Space') {
                nextInput(letters, letter, true);
            } else if (e.key === 'Enter') {

            } else {
                nextInput(letters, letter);
            } 
        }, 10);
    });
});