import React from 'react'
import {Link} from 'react-router-dom'

const ProjectItem = ({project, deleteProject}) => {
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
            <td>
                <button onClick={() => deleteProject(project.id) }>Delete</button>
            </td>
        </tr>
    )
}


const ProjectList = ({projects, deleteProject}) => {
    return (
        <div>
        <table>
            <tr>
                <th>
                    Header
                </th>
                <th>
                    Description
                </th>
                <th>
                    Url
                </th>
                <th></th>
            </tr>
            {projects.map((project) => < ProjectItem project={project} deleteProject={deleteProject} />)}
        </table>
        </div>
    )
}

export default ProjectList;

