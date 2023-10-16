<form action="/edit/{{ task[0] }}" method="post">
    Task Name: <input type="text" name="task_name" value="{{ task[1] }}">
    <input type="submit" value="Update">
</form>
