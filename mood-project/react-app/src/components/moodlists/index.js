import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import {
  loadUserMoods,
  deleteMoodlist,
} from "../../store/moodlist";
import AddFormModal from "../AddMood";
import EditFormModal from "../EditMoodlist";

import "./moodlists.css";

const Moodlists = () => {
  const dispatch = useDispatch();
  const moodlists = useSelector((state) => Object.values(state.moodlists));
  const userId = useSelector((state) => state.session.user.id);
  const [showModal, setShowModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);



  useEffect(() => {
    dispatch(loadUserMoods(userId));
  }, [dispatch, showEditModal, showModal]);

  // useEffect(() => {
  //     dispatch(addMoodList)
  // }, [dispatch])

  const handleDelete = async (e) => {
    e.preventDefault();
    const id = e.target.id;
    await dispatch(deleteMoodlist(id));
  };
  return (
    <>
      <div className="moodlists">
        <h1 className="moodlistheader">Moodlists</h1>
        <a id="addamood">
          <AddFormModal setShowModal={setShowModal} showModal={showModal} />
        </a>
        <div className="moodlistcontent">
        {moodlists?.map((mood) => (
          <>
          <div className="moodboxes">
            <Link to={`/moodlists/${mood.id}`}>
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

            <a className="moodlistedit-delete">
              <EditFormModal
              
                mood={mood?.id}
                setShowEditModal={setShowEditModal}
                showEditModal={showEditModal}
                />
            </a>
        </div>
                </div>
          </>
        ))}
        </div>
      </div>
      </>
  );
};
export default Moodlists;
