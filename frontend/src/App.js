import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'
// import MenuList from './components/Menu.js'
import FooterList from './components/Footer.js'
import {BrowserRouter, Link, Navigate, Route, Routes, useLocation} from 'react-router-dom'
import ProjectList from './components/ProjectList'
import TodoList from './components/TodoList'
import UserProjectList from './components/UserProjectList'
import LoginForm from './components/LoginForm';


const NotFound = () => {
    let {pathname} = useLocation()

    return (
        <div>
            Page '{pathname}'     NOT FOUND. PLEASE, TRY AGAIN
        </div>
    )
}

class App extends React.Component {
    // menu = [
    //     {
    //         'name': 'Main',
    //         'url': '/'
    //     },
    //     {
    //         'name': 'Register',
    //         'url': '/register'
    //     },
    //     {
    //        'name': 'Log in' ,
    //         'url': '/login'
    //     },

    //      {
    //         'name': 'Log out',
    //         'url': '/logout'
    //     },
    // ]
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
            // 'menu': this.menu,
            'footer': this.footer,
            'users': [],
            'projects': [],
            'todos': [],
            'token': '',
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {
                'username': login,
                'password': password
            })
            .then(response => {
                const token = response.data.token
                // console.log('token:', token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }
     isAuth() {
        return !!this.state.token
    }

    componentDidMount() {
          let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
        this.setState({ 'users': [] })

        axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))
        this.setState({ 'projects': [] })

        axios
            .get('http://127.0.0.1:8000/api/todos/', {headers})
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => console.log(error))
        this.setState({ 'todos': [] })

    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': '',
        }, this.getData)
    }

    render() {
        return (
            <div className='App'>
                {/*{<MenuList item_menu={this.state.menu} />}*/}
            <div>
                <BrowserRouter>
                    <nav>
                        <li> <Link to='/'>Users</Link></li>
                        <li> <Link to='/projects'>Projects</Link></li>
                        <li> <Link to='/todos'>Todos</Link></li>
                        <li>
                        {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<Navigate to='/users' />} />
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} users={this.state.users} />} />
                        <Route exact path='/todos' element={<TodoList todos={this.state.todos} users={this.state.users} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />
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

