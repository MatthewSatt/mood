
import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import EditForm from './EditModal';

function EditFormModal({ mood, showEditModal, setShowEditModal }) {
  // const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className='login-button' onClick={() => setShowEditModal(true)}>Edit</button>
      {showEditModal && (
        <Modal onClose={() => setShowEditModal(false)}>
          <EditForm setShowEditModal={setShowEditModal} mood={mood} />
        </Modal>
      )}
    </>
  );
}

export default EditFormModal;
