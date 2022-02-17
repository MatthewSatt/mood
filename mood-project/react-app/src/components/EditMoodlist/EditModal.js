import React, { useState } from "react";
import {useHistory} from 'react-router-dom'
import { useDispatch } from "react-redux";
import {editMoodlist} from "../../store/moodlist";
import "./EditForm.css"

function EditForm({ id }) {
    const dispatch = useDispatch();
    const history = useHistory()
    const [name, setName] = useState("");
    const [color, setColor] = useState("");
    console.log('HELLO1', id)


  const handleSubmit = (e) => {
    e.preventDefault();
    const newmoodlist = {
        "id": id,
        'name': name,
        'color': color,
    }

    dispatch(editMoodlist(newmoodlist, id))

  };

  return (

    <form className="edit" onSubmit={handleSubmit}>
      {/* <ul className="errors">
        {errors.map((error, idx) => (
          <li key={idx}>{error}</li>
        ))}
      </ul> */}

      <h1 id="loginheader">Edit</h1>
        <label>
          <input
            className="userinput"
            placeholder="New Mood"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <label>
          <input
            className="passwordinput"
            placeholder="Color"
            type="text"
            value={color}
            onChange={(e) => setColor(e.target.value)}

          />
        </label>
        <button className="loginbutton" type="submit">Edit</button>
    </form>
  );
}

export default EditForm;
