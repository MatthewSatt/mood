import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import AddForm from './AddModal'

function AddFormModal({ userId }) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className='login-button' onClick={() => setShowModal(true)}>Add new mood</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <AddForm userId={userId}/>
        </Modal>
      )}
    </>
  );
}

export default AddFormModal;
