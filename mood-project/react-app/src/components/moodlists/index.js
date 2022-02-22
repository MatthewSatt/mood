import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Modal } from "../../context/Modal";
import { Link } from "react-router-dom";
import { editMoodlist } from "../../store/moodlist";

import { loadUserMoods, deleteMoodlist } from "../../store/moodlist";
import AddFormModal from "../AddMood";
import "./moodlists.css";

const Moodlists = () => {
  const dispatch = useDispatch();
  const moodlists = useSelector((state) => Object.values(state.moodlists));
  const userId = useSelector((state) => state.session.user.id);
  const [showModal, setShowModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const user = useSelector((state) => state.session.user);
  const [name, setName] = useState("");
  const [color, setColor] = useState("");
  const [x, setX] = useState("");


  useEffect(() => {
    dispatch(loadUserMoods(userId));
  }, [dispatch, showEditModal, showModal]);





  const handleEdit = (e) => {
    e.preventDefault();
    const newmoodlist = {
      id: x,
      name: name,
      color: color,
    };
    dispatch(editMoodlist(newmoodlist));
    dispatch(loadUserMoods(userId));
    setShowEditModal(false);
  };


  const handleShowModalData = (e) => {
    e.preventDefault();
    setX(+e.currentTarget.id);
    setShowEditModal(true);
  };

  const handleDelete = (e) => {
    e.preventDefault();
    const id = e.target.id;
    dispatch(deleteMoodlist(id));
  };
  return (
    <>
      <div className="moodlists">
        <h1 className="moodlistheader">Moodlists</h1>
        <a id="addamood">
          <AddFormModal setShowModal={setShowModal} showModal={showModal} />
        </a>
        <div className="moodlistcontent">
          {moodlists
            ?.map((mood) => (
              <>
                <div className={`moodboxes ${mood.color}style`} key={mood.id}>
                  <Link
                    className="textformoodlists"
                    to={`/moodlists/${mood.id}`}
                  >
                    <div className="eachmoodlist" key={mood?.id}>
                      <p id="moodname">{mood?.name}</p>
                    </div>
                  </Link>
                  <div className="buttons-for-moodlists">
                    <button
                      onClick={handleDelete}
                      id={mood?.id}
                      className="moodlistedit-delete"
                    >
                      Delete
                    </button>

                    <button
                      id={mood.id}
                      className="moodlistedit-delete"
                      onClick={(e) => handleShowModalData(e)}
                    >
                      Edit
                    </button>
                    {showEditModal && (
                      <Modal onClose={() => setShowEditModal(false)}>
                        <form className="edit" onSubmit={handleEdit}>
                          <h1 id="loginheader">Edit Mood</h1>
                          <label>
                            <input
                              className="userinput"
                              placeholder="New Mood"
                              type="text"
                              value={name}
                              onChange={(e) => setName(e.target.value)}
                            />
                          </label>
                          <select
                            className="colorinput"
                            value={color}
                            onChange={(e) => setColor(e.target.value)}
                          >
                            <option className="REDstyle" value="red">
                              Red
                            </option>
                            <option className="greenstyle" value="green">
                              Green
                            </option>
                            <option className="bluestyle" value="blue">
                              Blue
                            </option>
                            <option className="purplestyle" value="purple">
                              Purple
                            </option>
                            <option className="blackstyle" value="black">
                              Black
                            </option>
                          </select>
                          <button
                            className="loginbutton"
                            type="submit"
                          >
                            Confirm
                          </button>
                        </form>
                      </Modal>
                    )}
                  </div>
                </div>
              </>
            ))
            .reverse()}
        </div>
      </div>
    </>
  );
};
export default Moodlists;

// const updateUserData = useEffect(() => {
//   dispatch(loadUserMoods(userId));
// }, [dispatch]);
