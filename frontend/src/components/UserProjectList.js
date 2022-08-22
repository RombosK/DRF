import {useParams} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.project_name}
            </td>
            <td>
                {project.description}
            </td>
        </tr>
    )
}

const UserProjectList = ({projects}) => {
    let {userId} = useParams()
    let filteredProjects = projects.filter((project) => project.users.includes(parseInt(userId)))

    return (
        <table>
            <th>
                Header
            </th>
            <th>
                Users
            </th>
            {filteredProjects.map((project) => <ProjectItem project={project} /> )}
        </table>
    )
}

export default UserProjectList;

