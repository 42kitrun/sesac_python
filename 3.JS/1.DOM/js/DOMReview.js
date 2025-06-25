//1. 나의 네이버 메일 들어가서, checkbox 전체 스크립트로 해보기
const checkboxes = document.querySelectorAll('.button_checkbox_wrap input[type="checkbox"]');

checkboxes.forEach(function (checkbox) {
    checkbox.checked = true;
});

//2. 보낸 사람 이메일 주소들 모두다 추출해보기
const senders = document.querySelectorAll('.button_sender');
let senderList = new Set();

Array.from(senders).forEach(function (sender) {
    let mailArr = sender.title.split('<');
    const mail = mailArr[mailArr.length - 1].slice(0, -1);
    console.log(mail);
    senderList.add(mail);
});
