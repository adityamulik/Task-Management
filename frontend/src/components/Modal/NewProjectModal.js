import React, { useState } from 'react';
import Modal from 'react-modal';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

function NewProjectModal(props){
  const [modalIsOpen,setIsOpen] = useState(false);
  const [startDate, setStartDate] = useState(new Date());
  const [dueDate, setDueDate] = useState(new Date());

  const openModal = () => {
    setIsOpen(!modalIsOpen);
  }

  const closeModal = () => {
    setIsOpen(false);
  }
 
  if(props.showModal) {
    setIsOpen(true);
  }
 
  return (
    <div className="projectModal">
      <button onClick={openModal}>Create Project</button>
      <Modal
        isOpen={modalIsOpen}
        ariaHideApp={false}
        onRequestClose={closeModal}
        contentLabel="Example Modal"
      >
        <p>Create New Project.</p>
        <form>
          <input 
            type="text" 
            placeholder="Title"
          /><br/><br/>
          <textarea 
            placeholder="Description"
          /><br/><br/>
          <DatePicker 
            selected={startDate} 
            onChange={date => setStartDate(date)} 
          /><br/><br/>
          <DatePicker 
            selected={dueDate} 
            onChange={date => setDueDate(date)} 
          /><br/><br/>
          <button onClick={closeModal}>Cancel</button>
          <button>Save</button>
        </form>
      </Modal>
    </div>
  );
}

export default NewProjectModal;