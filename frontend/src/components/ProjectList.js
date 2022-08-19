import React from 'react'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.project_name}
            </td>
            <td>
                {project.description}
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
