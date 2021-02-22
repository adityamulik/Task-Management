import React, { useState } from 'react';
import axios from 'axios';
import Modal from 'react-modal';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

function NewProjectModal(props){
  const [modalIsOpen,setIsOpen] = useState(false);
  const [sendData, setData] = useState(
    {
      "title": "",
      "description": "",
      "start_date": "2013-02-12",
      "due_date": "2012-03-12",
      "status": "Active",
    }
  );

  console.log(sendData);

  const [startDate, setStartDate] = useState(new Date());
  const [dueDate, setDueDate] = useState(new Date());

  const styleModal = {
    content : {
      top                   : '50%',
      left                  : '50%',
      right                 : 'auto',
      bottom                : 'auto',
      marginRight           : '-50%',
      transform             : 'translate(-50%, -50%)',
      width: '800px',
      height: '500px',
    }
  };

  const openModal = () => {
    setIsOpen(!modalIsOpen);
  }

  const closeModal = () => {
    setIsOpen(false);
  }

  if(props.showModal) {
    setIsOpen(true);
  } 

  const handleChange = (e) => {
    setData({...sendData, [e.target.name]: e.target.value})
  }

  const createProject = (e) => {
    e.preventDefault();
    axios.post('/api/projects/', sendData)
      .then(response => {
        if(response.status == 201) {
          alert('New Project Created!')
          closeModal(); 
        }
      })
      .catch(error => console.log(error, "why?"))
  }; 

  console.log(sendData);
 
  return (
    <div className="projectModal">
      <button onClick={openModal}>Create Project</button>
      <Modal
        style={styleModal}        
        isOpen={modalIsOpen}
        ariaHideApp={false}
        onRequestClose={closeModal}
        contentLabel="Example Modal"
      >
        <p>Create New Project.</p>
        <form onSubmit={createProject}>
          <input 
            type="text" 
            name="title"
            placeholder="Title"
            value={sendData.title}
            onChange={handleChange}
          /><br/><br/>
          <textarea 
            name="description"
            placeholder="Description"
            value={sendData.description}
            onChange={handleChange}
          /><br/><br/>
          <DatePicker 
            name="start_date"
            dateFormat="yyyy-MM-dd"
            value={sendData.start_date}
            selected={startDate}
            onChange={date => setStartDate(date)}
          /><br/><br/>
          <DatePicker 
            name="due_date"
            dateFormat="yyyy-MM-dd"
            value={sendData.due_date}
            selected={dueDate}
            onChange={date => setDueDate(date)}
          /><br/><br/>
          <select name="status" onChange={handleChange}>
            <option name="Active" value="Active">Active</option>
            <option name="Inactive" value="Inactive">Inactive</option>
          </select><br/><br/>
          <button onClick={closeModal}>Cancel</button>
          <button type="submit">Save</button>
        </form>
      </Modal>
    </div>
  );
}

export default NewProjectModal;