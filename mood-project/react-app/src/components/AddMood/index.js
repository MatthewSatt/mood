
import { Modal } from '../../context/Modal';
import AddForm from './AddModal'

function AddFormModal({setShowModal, showModal}) {
  // const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className='addmoodbutton' onClick={() => setShowModal(true)}>Add new mood</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <AddForm setShowModal={setShowModal}/>
        </Modal>
      )}
    </>
  );
}

export default AddFormModal;
