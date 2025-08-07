const todos = document.getElementById('todo-list');

document.addEventListener('DOMContentLoaded', () => {
    displayTodos();
});

async function displayTodos() {
    const todosUl = document.getElementById('todo-list');
    let todoHtml = ``;

    const response = await fetch('/api/todo');
    if (!response.ok) {
        throw new Error('요청 오류');
    }
    const data = await response.json();
    let todos = data.data;
    console.log(todos);
    for (todo of todos)  {
        console.log(todo.todo,todo.status);

        todoHtml += `<li data-id="${todo.id}">
                <label class="new-todo">
                    <input type="checkbox" ${todo.status === 1 ? "checked" : ""}/>
                    <span>${todo.todo}</span>
                </label>
                    <i class="bi bi-trash"></i>
            </li>
            `
        
    }
    todosUl.innerHTML = todoHtml;
}

// 추가버튼 누르면 할일 추가
const todoForm = document.getElementById('todo-form');
todoForm.addEventListener('submit', (e) => {
  e.preventDefault(); // 폼 제출 막기
  postTodo();         // 함수를 호출해서 처리
});

async function postTodo() {
    // 할 일 추가 로직
    const input = document.getElementById('text-input');
    const todo = input.value;
    console.log(todo);
    const response = await fetch('/api/todo',{
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify( todo )
    });
    if (!response.ok) {
        throw new Error('요청 오류');
    }
    const data = await response.json();
    console.log(data);
    input.value = ''; // 입력값 초기화
    displayTodos();
}

// check box 상태변경시 post로 상태 변경반영
todos.addEventListener('change', async function (e) {
    if (e.target && e.target.type === 'checkbox') {
        const checkbox = e.target;
        const status = checkbox.checked ? 1:0;
        const todo = checkbox.parentElement.textContent.trim(); 
        const todoInfo = {
            'id' : checkbox.parentElement.dataset.id,
            'todo':todo,
            'status':status
        }
        const response = await fetch('/api/todo',{
            method: 'PATCH',
            headers: { // 옵셔널 한거지만, 나의 바디 포멧과 언어 등을 넣어 주는것이 좋음
                         'Content-Type': 'application/json; charset=UTF-8'
                     },
            body: JSON.stringify(todoInfo)
        });
        if (!response.ok) throw new Error('요청 오류');
        const data = await response.json();
        console.log(data);
        
    }
})

// 할일 삭제
todos.addEventListener('click', async (e) => {
    // 클릭된 요소가 이미지
    if (e.target.tagName === 'I') {
        const list = e.target.parentNode;
        const todoId = list.dataset.id;
        
        const response = await fetch('/api/todo',{
            method: 'DELETE',
            headers: { // 옵셔널 한거지만, 나의 바디 포멧과 언어 등을 넣어 주는것이 좋음
                         'Content-Type': 'application/json; charset=UTF-8'
                     },
            body: JSON.stringify(todoId)
        });
        if (!response.ok) throw new Error('요청 오류');
        const data = await response.json();
        console.log(data);
        list.remove(); // 해당 할일 삭제
    }
});