const resultEl = document.getElementById('result');
const plusBtn = document.getElementById('plus');
const minusBtn = document.getElementById('minus');
const messageEl = document.getElementById('message');

let count = 0;

const BG_CLASSES = ['bg-yellow-400', 'bg-green-500', 'bg-red-500'];

function updateBackground() {
  resultEl.classList.remove(...BG_CLASSES);

  if (count > 0) {
    resultEl.classList.add('bg-yellow-400');
  } else if (count < 0) {
    resultEl.classList.add('bg-green-500');
  } else {
    resultEl.classList.add('bg-red-500');
  }
}

function updateButtons() {
  plusBtn.disabled = count === 10;
  minusBtn.disabled = count === -10;
}

function updateMessage() {
  if (count === 10 || count === -10) {
    messageEl.textContent = 'Вы достигли экстремального значения';
  } else {
    messageEl.textContent = '';
  }
}

function render() {
  resultEl.textContent = count;
  updateBackground();
  updateButtons();
  updateMessage();
}

plusBtn.addEventListener('click', () => {
  if (count < 10) {
    count++;
    render();
  }
});

minusBtn.addEventListener('click', () => {
  if (count > -10) {
    count--;
    render();
  }
});

render();
