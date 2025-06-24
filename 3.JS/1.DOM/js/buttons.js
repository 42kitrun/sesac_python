console.log('실행시 출력');

function number_inc() {
    console.log('증가버튼 클릭');
    let result = document.getElementById('result');
    let bf_number = result.textContent;

    // DIV 요소 안에 있는 글을 가져오는 3가지 방식
    // innerText - 글자만(디자인 속성을 적용받음)
    // innerHTML - 글자와 그 태그까지 함께 가져온다
    // textContent - 순수 글자만 가져온다
    console.log(bf_number);

    let af_number = Number(bf_number) + 1;
    console.log(af_number);
    result.textContent = af_number;

    // 나의 생각이나 의도가 중요한게 아니고
    // 내가 짠 코드 그 내용이 중요한 것
}
function number_dec() {
    // console.log('감소버튼 클릭');
    // let result = document.getElementById('result');
    // let bf_number = result.textContent;
    // console.log(bf_number);
    // let af_number = Number(bf_number) - 1;
    // console.log(af_number);
    // result.textContent = af_number;
    // document.getElementById('result').textContent -= 1; 선생님 코드
    document.getElementById('result').textContent--;
}