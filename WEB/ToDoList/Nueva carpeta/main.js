const input = document.querySelector('input')
const addBtn = document.querySelector('.btn-add')
const ul = document.querySelector('ul')
const empty = document.querySelector('.empty')
const resetBtn = document.createElement('button');
resetBtn.textContent = "Reset";
resetBtn.className = "btn-reset";
resetBtn.style.display = "none";
document.querySelector('.container').appendChild(resetBtn);

addBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    const text = input.value;

    if (text !== ""){

    const li = document.createElement('li');
    const p = document.createElement('p');
    p.textContent = text;

    li.appendChild(p);
    li.appendChild(upTaskBtn());
    li.appendChild(downTaskBtn());
    li.appendChild(addDeleteBtn());
    li.appendChild(disableTaskBtn());
    ul.appendChild(li);


    input.value = "";
    empty.style.display = "none"
    resetBtn.style.display = "block";
    }
});

resetBtn.addEventListener('click', () => {
    ul.innerHTML = "";
    checkListState();
});

function addDeleteBtn() {
    const deleteBtn = document.createElement('button');

    deleteBtn.textContent = "X";
    deleteBtn.className = "btn-delete";

    deleteBtn.addEventListener('click', (e) => {
        const item = e.target.parentElement;
        ul.removeChild(item);

        const items = document.querySelectorAll('li');

        if (items.length === 0) {
            empty.style.display = 'block'
        }
    });
    return deleteBtn;
}

function disableTaskBtn() {
    const disableBtn = document.createElement('button');

    disableBtn.textContent = "OK";
    disableBtn.className = "btn-disable"

    disableBtn.addEventListener('click' , (e) => {
        const item = e.target.parentElement;
        const taskText = item.querySelector('p');
        const deleteBtn = item.querySelector('.btn-delete');
        const upBtn = item.querySelector('.up-btn')
        const downBtn = item.querySelector('.down-btn')
    

    if (taskText.style.textDecoration === 'line-through') {
        taskText.style.textDecoration = 'none';
    } else {
        taskText.style.textDecoration = 'line-through';
        disableBtn.classList.remove('btn-disable');
        disableBtn.classList.add('btn-disable-dis');
        disableBtn.disabled = true
        upBtn.classList.remove('up-btn');
        upBtn.classList.add('up-btn-ds');
        upBtn.disabled = true
        downBtn.classList.remove('down-btn');
        downBtn.classList.add('down-btn-ds');
        downBtn.disabled = true
    }
});

    return disableBtn;
}

function upTaskBtn(){
    const upBtn = document.createElement('button');

    upBtn.textContent = "↑";
    upBtn.className = "up-btn";

    upBtn.addEventListener('click' , (e) => {
        const item = e.target.parentElement;
        let prevItem = item.previousElementSibling

        while (prevItem && prevItem.querySelector('p').style.textDecoration === 'line-through') {
            prevItem = prevItem.previousElementSibling;

        }

        if (prevItem) {
            item.parentElement.insertBefore(item, prevItem);

        }
    })


    return upBtn;
}

function downTaskBtn(){
    const downBtn = document.createElement('button');

    downBtn.textContent = "↓";
    downBtn.className = "down-btn";

    downBtn.addEventListener('click' , (e) => {
        const item = e.target.parentElement;
        let prevItem = item.nextElementSibling;

        while (prevItem && prevItem.querySelector('p').style.textDecoration === 'line-through') {
            prevItem = prevItem.nextElementSibling;
        }

        if (prevItem) {
            item.parentElement.insertBefore(prevItem, item);

        }
    })


    return downBtn;
}

function checkListState() {
    const items = document.querySelectorAll('li');
    if (items.length === 0) {
        empty.style.display = "block";
        resetBtn.style.display = "none"; 
    } else {
        empty.style.display = "none";
        resetBtn.style.display = "block"; 
    }
}

