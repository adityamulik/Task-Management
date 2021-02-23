import React, { useState } from 'react';
import axios from 'axios';
import Modal from 'react-modal';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import moment from 'moment';

function NewProjectModal(props){
  const [modalIsOpen,setIsOpen] = useState(false);
  const [startDate, setStartDate] = useState(new Date());
  const [dueDate, setDueDate] = useState(new Date());
  const [sendData, setData] = useState(
    {
      "title": "",
      "description": "",
      "start_date": "",
      "due_date": "",
      "status": "A",
    }
  );

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
    setData({
      ...sendData, 
      [e.target.name]: e.target.value, 
      start_date: moment(startDate).format("yyyy-MM-DD"), 
      due_date: moment(dueDate).format("yyyy-MM-DD")
    })
  };

  const createProject = (e) => {
    e.preventDefault();
    axios.post('/api/projects/', sendData)
      .then(response => {
        if(response.status === 201) {
          alert('New Project Created!')
          closeModal(); 
        }
      })
      .catch(error => console.log(error, "why?"))
  }; 
 
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
            selected={startDate}
            onChange={date => setStartDate(date)}
          /><br/><br/>
          <DatePicker 
            name="due_date"
            dateFormat="yyyy-MM-dd"
            selected={dueDate}
            onChange={date => setDueDate(date)}
          /><br/><br/>
          <select name="status" onChange={handleChange}>
            <option name="Active" value="A">Active</option>
            <option name="Inactive" value="IA">Inactive</option>
          </select><br/><br/>
          <button onClick={closeModal}>Cancel</button>
          <button type="submit">Save</button>
        </form>
      </Modal>
    </div>
  );
}

export default NewProjectModal;