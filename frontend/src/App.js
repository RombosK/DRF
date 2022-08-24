import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'
import MenuList from './components/Menu.js'
import FooterList from './components/Footer.js'
import {BrowserRouter, Link, Navigate, Route, Routes, useLocation} from 'react-router-dom'
import ProjectList from './components/ProjectList'
import TodoList from './components/TodoList'
import UserProjectList from './components/UserProjectList'


const NotFound = () => {
    let {pathname} = useLocation()

    return (
        <div>
            Page '{pathname}'     NOT FOUND. PLEASE, TRY AGAIN
        </div>
    )
}

class App extends React.Component {
    menu = [
        {
            'name': 'Main',
            'url': '/'
        },
        {
            'name': 'Register',
            'url': '/register'
        },
        {
           'name': 'Log in' ,
            'url': '/login'
        },

         {
            'name': 'Log out',
            'url': '/logout'
        },
    ]
    footer = [

        {
            'name': 'Contacts',
            'url': '/contact'
        },
         {
            'name': 'Support',
            'url': '/support'
        },

    ]


    constructor(props) {
        super(props)
        this.state = {
            'menu': this.menu,
            'footer': this.footer,
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div className='App'>
                {<MenuList item_menu={this.state.menu} />}
            <div>
                <BrowserRouter>
                    <nav>
                        <li> <Link to='/'>Users</Link></li>
                        <li> <Link to='/projects'>Projects</Link></li>
                        <li> <Link to='/todos'>Todos</Link></li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users' />} />
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} users={this.state.users} />} />
                        <Route exact path='/todos' element={<TodoList todos={this.state.todos} users={this.state.users} />} />
                        <Route exact path='/todos/id' element={<TodoList todos={this.state.todos} users={this.state.users} />} />
                        <Route path='/users'>
                            <Route index element={<UserList users={this.state.users} />} />
                            <Route path=':userId' element={<UserProjectList projects={this.state.projects} />} />
                        </Route>
                        <Route exact path='*' element={<NotFound />} />
                    </Routes>
                </BrowserRouter>
            </div>
                 <div className='panel-footer'>
                     {<FooterList item_footer={this.state.footer} />}
               </div>
             </div>
        )
    }
}

export default App;

