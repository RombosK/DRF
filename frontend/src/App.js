import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'
import MenuList from './components/Menu.js'
import FooterList from "./components/Footer.js";


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
            'users': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                {<MenuList item_menu={this.state.menu} />}
                <div className='content'>
                    {<UserList users={this.state.users} />}
                </div>

                <div className='panel-footer'>
                    {<FooterList item_footer={this.state.footer} />}
                    <p>
                        <strong>Полезное</strong>
                    </p>
                    <p>
                        <ul className="list-unstyled">
                            <li><a href="#">Положения &amp; Условия</a></li>
                            <li><a href="#">Конфиденциальность &amp; Cookies</a></li>
                            <li><a href="#">Документация по API</a></li>
                        </ul>
                    </p>
                </div>

            </div>
        )
    }
}

export default App;
