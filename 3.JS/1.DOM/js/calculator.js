document.addEventListener('DOMContentLoaded', function () {
    // document.getElementById('display').focus(); // 페이지 로드 시 입력창에 포커스 설정
});

// 결과값 경우의 수
// number, error, +/-infinity, undefined, NaN

const input = document.getElementById('display');
input.addEventListener('keydown', function (event) {
    // 허용 키: 숫자, +, -, *, /
    const allowedKeys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/'];
    // 백스페이스, 딜리트, 화살표키 등은 허용
    const allowedSpecialKeys = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'];


    // 허용된 키가 아니면 입력 차단
    if (!allowedKeys.includes(event.key) && !allowedSpecialKeys.includes(event.key)) {
        event.preventDefault();
    }

    // 유한한 수가 아닐 경우, 입력창 초기화
    if (!isFinite(input.value)) {
        input.value = '';
    }

    switch (event.key) {
        // Enter 키와 Numpad Enter 키를 눌렀을 때 계산 실행}
        case 'Enter':
        case 'NumpadEnter':
            event.preventDefault(); // Enter 키의 기본 동작 방지
            calculate(); // 계산 함수 호출
            break;
        // Escape 키를 눌렀을 때 입력창 비우기
        case 'Escape':
            event.preventDefault(); // Escape 키의 기본 동작 방지
            clearInput(); // 입력창 비우기
            break;
        // Backspace 키를 눌렀을 때 입력창에서 마지막 문자 삭제
        case 'Backspace':
            event.preventDefault(); // Backspace 키의 기본 동작 방지
            // 입력창에서 마지막 문자 삭제
            const display = document.getElementById('display');
            display.value = display.value.slice(0, -1);
            break;
        // Delete 키를 눌렀을 때 입력창 비우기
        case 'Delete':
            // Delete 키의 기본 동작 방지
            event.preventDefault();
            clearInput(); // 입력창 비우기
            break;
        // 숫자 키를 눌렀을 때 입력창에 숫자 추가
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            event.preventDefault(); // 숫자 키의 기본 동작 방지
            appendNumber(event.key); // 입력창에 숫자 추가
            break;
        case '+':
        case '-':
        case '*':
        case '/':
            event.preventDefault(); // 연산자 키의 기본 동작 방지
            appendSymbol(event.key);
            break;
    }
});

// 입력창에 숫자를 추가합니다.
function appendNumber(number) {
    const display = document.getElementById('display');
    display.placeholder = ''; // 입력창의 placeholder를 초기화합니다.

    if (display.value === '0' && isFinite(number)) {
        // 입력창이 비어있고, 숫자가 0인 경우에는 아무 동작도 하지 않습니다.
        return;
    } else {
        document.getElementById('display').value += number;
    }
}

function appendSymbol(symbol) {
    const display = document.getElementById('display');
    display.placeholder = ''; // 입력창의 placeholder를 초기화합니다.

    // 입력창이 비어있고, 연산자가 '-'인 경우에만 추가
    if (!display.value && symbol === '-') {
        display.value += symbol;

    } // 마지막 문자가 숫자인 경우에 연산자를 추가
    else if (display.value) {
        if (isFinite(display.value.slice(-1))) {// 마지막 문자가 숫자인 경우
            // 연산자를 추가합니다.
            display.value += symbol;
        } else if (display.value.slice(-1) === '*' && symbol === '*') {
            // 연속된 '*' 연산자는 지수연산입니다.
            display.value += symbol;
        } else if (/[-+*/]/.test(display.value.slice(-1))) {
            // 마지막 문자가 기호인 경우에 연산자를 대체합니다.
            display.value = display.value.slice(0, -1) + symbol;
        } else {
            // 마지막 문자가 숫자가 아닌 경우에는 아무 동작도 하지 않습니다.
            return;
        }
    }
}

function clearInput() {
    const display = document.getElementById('display');

    display.value = '';// 입력창을 비웁니다.
    display.placeholder = ''; // 입력창의 placeholder를 초기화합니다.
}

function calculate() {
    const display = document.getElementById('display');
    display.placeholder = ''; // 입력창의 placeholder를 초기화합니다.

    // 입력창이 비어있으면 아무 동작도 하지 않습니다.
    if (!display.value) {
        display.value = '';
        return;
    }
    try {
        // 입력된 수식을 계산합니다.
        const result = eval(display.value);
        if (isFinite(result)) {// 결과가 유한한 수인 경우
            // 결과를 입력창에 표시합니다.
            display.value = result;
        } else { // 결과가 유한하지 않은 경우(예: Infinity, NaN 등)
            display.placeholder = result;
            display.value = '';
            return;
        }
    } catch (e) {
        display.placeholder = 'Error'; // 계산 중 오류가 발생한 경우
        display.value = '';
        console.error('계산 중 오류 발생:', e); // 오류 메시지를 콘솔에 출력
        return;
    }
}