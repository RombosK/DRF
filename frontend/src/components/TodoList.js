import React from 'react'


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.note_header}
            </td>
            <td>
                {todo.note_text}
            </td>
            <td>
                {todo.id}
            </td>

        </tr>
    )
}


const TodoList = ({todos}) => {
    return (
        <table>
            <th>
                Title
            </th>
            <th>
                Text
            </th>
            <th>
                User
            </th>

            {todos.map((todo) => < TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList;
