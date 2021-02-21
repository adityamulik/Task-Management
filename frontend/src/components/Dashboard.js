import React, { useState } from 'react';
import Projects from './Projects';
import NewProjectModal from './Modal/NewProjectModal';

const Dashboard = () => {

  const [showModal] = useState(false);

  return (
    <div className="Dashboard">
      <NewProjectModal 
        showModal={showModal}
      />
      <Projects />
    </div>
  )
}

export default Dashboard;