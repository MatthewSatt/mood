
import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import EditForm from './EditModal';

function EditFormModal({ id }) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className='login-button' onClick={() => setShowModal(true)}>Edit</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditForm id={id} />
        </Modal>
      )}
    </>
  );
}

export default EditFormModal;
