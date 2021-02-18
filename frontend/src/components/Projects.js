import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Projects = () => {

  const [projects, setProjects] = useState([]);

  useEffect(() => {
    axios.get('/api/projects/')
      .then(res => {
        console.log(res);
        setProjects(res.data.results);
      })
      .catch(err => {
        console.log(err);
      })
  }, []);

  return (
    <div className="Projects">
      <h1>Project List</h1>
      <ul>
        {projects.map(project => 
          <li key={project.project_id}>{project.title} : {project.description}</li>
        )}
      </ul>
    </div>
  )
};

export default Projects;