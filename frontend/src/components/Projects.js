import React, { useState, useEffect, useMemo } from 'react';
import axios from 'axios';
import ProjectTable from './ProjectTable';

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

  const columns = useMemo(
    () => 
      [{
        Header: 'ID',
        accessor: 'project_id'
      },
      {
        Header: 'Title',
        accessor: 'title'
      },
      {
        Header: 'Description',
        accessor: 'description'
      },
      {
        Header: 'Start Date',
        accessor: 'start_date'
      },
      {
        Header: 'Due Date',
        accessor: 'due_date'
      },
      {
        Header: 'Status',
        accessor: 'status_display'
      },
      {
        Header: 'Owner',
        accessor: 'owner'
      }]
  )

  return (
    <div className="Projects">
      <h1>Project List</h1>
      <ProjectTable columns={columns} data={projects} />
    </div>
  )
};

export default Projects;