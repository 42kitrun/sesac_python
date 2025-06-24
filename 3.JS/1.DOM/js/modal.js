const open = document.getElementById('open');
const close = document.getElementById('close');

const modal = document.querySelector('.modal-wrapper');
// const modal = document.getElementsByClassName('.modal-wrapper')[0];


// 함수 정의하는 3가지
// open.onclick = function openModal() {
// open.onclick = function() {
open.onclick = () => {
    modal.style.display = 'flex';
}

close.onclick = () => {
    modal.style.display = 'none';
}