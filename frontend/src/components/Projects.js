import React, { useEffect } from 'react';

const Projects = () => {

  useEffect(() => {
    const projects = async () => {
      const response = await fetch('/api/projects/')
      const projectList = await response.json();
      console.log(projectList); 
    }
    projects();
  })  

  return (
    <div className="Projects">
      
    </div>
  )
};

export default Projects;