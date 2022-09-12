import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'header': '',
            'users': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleUsersSelect(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'users': []
                })
            return;
        }

        let users = []

        for(let option of event.target.selectedOptions) {
            users.push(option.value)
        }
        this.setState({
            'users': users
        })
    }

    handleSubmit(event) {
        this.props.createProject(this.state.header, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text" name="header" placeholder="header" value={this.state.header} onChange={(event) => this.handleChange(event)} />
                    <select multiple onChange={(event) => this.handleUsersSelect(event)} >
                        {this.props.users.map((user) => <option value={user.id}>{user.username}</option> )}
                    </select>
                    <input type="submit" className="btn btn-primary" value="Create"  />
                </form>
            </div>
        )
    }
}

export default ProjectForm;

