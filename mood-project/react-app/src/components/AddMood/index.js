import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { Modal } from '../../context/Modal';
import AddForm from './AddModal'

function AddFormModal({setShowModal, showModal}) {
  // const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className='login-button' onClick={() => setShowModal(true)}>Add new mood</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <AddForm setShowModal={setShowModal}/>
        </Modal>
      )}
    </>
  );
}

export default AddFormModal;
