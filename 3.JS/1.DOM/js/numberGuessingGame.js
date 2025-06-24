
const Answer = Math.round(Math.random() * 99) + 1;
// 0 ~ 99에서 1을 더해 1 ~ 100까지의 범위임
console.log('Answer', Answer);

document.getElementById('inputNum').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        guessNumber();
    }
});

function guessNumber() {
    const inputNum = Number(document.getElementById('inputNum').value);
    const displayHistory = document.querySelector('ol');
    const feedBack = document.getElementById('feedBack');

    // 이상값 입력시 경고문 팝업 및 함수종료
    if (inputNum < 1 || inputNum > 100 || inputNum % 1 != 0) {
        alert('1이상 100이하 자연수를 입력하세요');
        document.getElementById('inputNum').value = ''; // 입력값을 지움
        return;
    }

    const newHistory = document.createElement('li');
    newHistory.textContent = `예측숫자: ${inputNum}`;
    displayHistory.appendChild(newHistory);

    if (inputNum > Answer) {
        const degree = (inputNum - Answer) >= 33 ? 'Too High' : 'High(less than 33)'
        feedBack.textContent = degree;
        newHistory.textContent += ` <---- ${degree}`;
    } else if (inputNum < Answer) {
        const degree = (Answer - inputNum) >= 33 ? 'Too Low' : 'Low(less than 33)'
        feedBack.textContent = degree;
        newHistory.textContent += ` <---- ${degree}`;
    } else {
        newHistory.textContent += ` <---- Correct!`;
        feedBack.textContent = 'Correct! 다시 시작하시려면 새로고침(F5)를 눌러주세요';
        document.getElementById('btnGuess').disabled = true;// 숫자를 맞추면 버튼을 비활성화
    }

    document.getElementById('inputNum').value = ''; // 입력값을 지움
}