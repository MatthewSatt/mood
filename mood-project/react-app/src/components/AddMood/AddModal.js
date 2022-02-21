import './AddModel.css'
import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addMoodList} from "../../store/moodlist";

// import "./EditForm.css"

function AddForm({ setShowModal, showModal }) {
    const userId = useSelector(state => state.session.user.id)
    const dispatch = useDispatch();
    const [name, setName] = useState("");
    const [color, setColor] = useState("");


  const handleSubmit = async (e) => {
    e.preventDefault();
    const newmoodlist = {
        'name': name,
        'color': color,
        "userId": userId
    }

    await dispatch(addMoodList(newmoodlist))
    setShowModal(false)
  };

  useEffect(() => {
    dispatch(addMoodList)
  }, [dispatch, name, color])

  return (

    <form className="edit" onSubmit={handleSubmit}>
      {/* <ul className="errors">
        {errors.map((error, idx) => (
          <li key={idx}>{error}</li>
        ))}
      </ul> */}

      <h1 id="loginheader">New mood</h1>
        <label>
          <input
            className="userinput"
            placeholder="Enter a new mood"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <label>
          <input
            className="passwordinput"
            placeholder="Color Theme"
            type="text"
            value={color}
            onChange={(e) => setColor(e.target.value)}

          />
        </label>
        <button className="loginbutton" type="submit">Add</button>
    </form>
  );
}

export default AddForm;
