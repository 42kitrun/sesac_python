
const Answer = Math.round(Math.random() * 100) + 1;
console.log('Answer', Answer);

function guessNumber() {
    const inputNum = Number(document.getElementById('inputNum').value);
    const displayHistory = document.querySelector('ul');
    const feedBack = document.getElementById('feedBack');

    // 이상값 입력시 경고문 팝업 및 함수종료
    if (inputNum < 1 || inputNum > 100 || inputNum % 1 != 0) {
        alert('1보다 크고 100보다 작은 자연수를 입력하세요');
        return;// 함수 종료
    }

    const newHistory = document.createElement('li');
    newHistory.textContent = `예측숫자: ${inputNum}`;
    displayHistory.appendChild(newHistory);

    if (inputNum > Answer) {
        feedBack.textContent = 'Too High';
        newHistory.textContent += ` <---- Too High`;
    } else if (inputNum < Answer) {
        feedBack.textContent = 'Too Low';
        newHistory.textContent += ` <---- Too Low`;
    } else {
        newHistory.textContent += ` <---- Correct!`;
        feedBack.textContent = 'Correct! 다시 시작하시려면 새로고침(F5)를 눌러주세요';
        document.getElementById('btnGuess').disabled = true;// 숫자를 맞추면 버튼을 비활성화
    }

    document.getElementById('inputNum').value = ''; // 입력값을 지움
}