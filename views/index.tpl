<h2>Task List</h2>
<ul>
    % for task in tasks:
        <li>{{ task[1] }} - <a href="/edit/{{ task[0] }}">Edit</a> | <a href="/delete/{{ task[0] }}">Delete</a></li>
    % end
</ul>

<a href="/create">Create New Task</a>
