import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Modal } from "../../context/Modal";
import { Link } from "react-router-dom";
import { editMoodlist } from "../../store/moodlist";
// {import { loadMoodSongs } from "../../store/songs";}

import { loadUserMoods, deleteMoodlist } from "../../store/moodlist";
import AddFormModal from "../AddMood";
import "./moodlists.css";

const Moodlists = () => {
  const dispatch = useDispatch();
  const moodlists = useSelector((state) => Object.values(state.moodlists));



  const userId = useSelector((state) => state.session.user.id);
  const [showModal, setShowModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [editName, setEditName] = useState("")
  const [editColor, setEditColor] = useState("")
  const [x, setX] = useState("");

  const [editErrors, setErrors] = useState([])
  useEffect(() => {
    const editErrors = []
    if (editName.length > 15) editErrors.push("The new name is too long")
    setErrors(editErrors)
  }, [editName])

  useEffect(() => {
    dispatch(loadUserMoods(userId));
  }, [dispatch, showEditModal, showModal, userId]);


  const handleEdit = async (e) => {
    e.preventDefault();
    const newmoodlist = {
      id: x,
      name: editName,
      color: editColor,
    };
    await dispatch(editMoodlist(newmoodlist));

    setShowEditModal(false);
    await dispatch(loadUserMoods(userId));
  };


  const handleShowModalData = (moodId, mood) => (e) => {
    e.preventDefault();
    setEditColor(mood.color)
    setEditName(mood.name)
    setX(+e.currentTarget.id);
    setShowEditModal(true);
  };

  const handleDelete = async (e) => {
    e.preventDefault();
    const id = e.target.id;
    dispatch(deleteMoodlist(id));
  };
  return (
    <>
      <div className="moodlists">
        <h1 className="moodlistheader">Moodlists</h1>
        <div id="addamood">
          <AddFormModal setShowModal={setShowModal} showModal={showModal} />
        </div>
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
                      onClick={handleShowModalData(mood.id, mood)}
                    >
                      Edit
                    </button>
                    {showEditModal && (
                      <Modal onClose={() => setShowEditModal(false)}>
                        <form className="edit" onSubmit={handleEdit}>
                        <ul className="errors">
                            {editErrors.length > 0 &&
                              editErrors.map((error) => {
                                return <li key={error}>{error}</li>;
                              })}
                          </ul>
                          <div className="editmoodform">
                          <h1 id="loginheader">Edit Mood</h1>
                          <label>
                            <input
                              className="nameinput"
                              placeholder="New Mood"
                              type="text"
                              value={editName}
                              onChange={(e) => setEditName(e.target.value)}
                            />
                          </label>
                          <select
                            className="colorinput"
                            value={editColor}
                            onChange={(e) => setEditColor(e.target.value)}
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
                              Orange-Yellow
                            </option>
                          </select>
                          <button
                          disabled={editErrors.length > 0 ? true : false}
                            type="submit"
                          >
                            Confirm
                          </button>
                          </div>
                        </form>
                      </Modal>
                    )}
                  </div>
                </div>
              </>
            ))
            }
        </div>
      </div>
    </>
  );
};
export default Moodlists;
