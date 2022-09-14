import React from 'react'
import {Link} from 'react-router-dom'

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.note_header}
            </td>
            <td>
                <Link to={`/todos/${todo.note_text}`}>{todo.note_text}</Link>
            </td>
            <td>
                {todo.id}
            </td>
            <td><button type='button'>Delete</button></td>
        </tr>
    )
}


const TodoList = ({todos}) => {
    return (
        <table>
            <tr>
                <th>
                    Title
                </th>
                <th>
                    Text
                </th>
                <th>
                    User
                </th>
                <th></th>
            </tr>
            {todos.map((todo) => < TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList;
