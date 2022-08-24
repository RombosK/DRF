import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.project_name}
            </td>
            <td>
                <Link to={`/projects/${project.id}`}>{project.description}</Link>
            </td>
            <td>
                {project.project_url}
            </td>
        </tr>
    )
}


const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Header
            </th>
            <th>
                Description
            </th>
            <th>
                Url
            </th>
            {projects.map((project) => < ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;
