document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('todo-form');
    const input = document.getElementById('todo-input');
    const list = document.getElementById('todo-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        addTask(input.value);
        input.value = '';
    });

    function addTask(task) {
        if (task.trim() === '') return;
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.textContent = task;
        list.appendChild(li);
    }
});