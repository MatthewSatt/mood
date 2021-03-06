import "./AddModel.css";
import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addMoodList } from "../../store/moodlist";


// import "./EditForm.css"

function AddForm({ setShowModal }) {
  const userId = useSelector((state) => state.session.user.id);
  const dispatch = useDispatch();
  const [name, setName] = useState("");
  const [color, setColor] = useState('red')
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    const errors = [];
    if (name.length < 1) errors.push("Name field is required");
    if (name.length > 15)errors.push("Name can't be longer than 15 letters")
    setErrors(errors);
  }, [name, color]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newmoodlist = {
      name: name,
      color: color,
      userId: userId,
    };

    await dispatch(addMoodList(newmoodlist));
    setShowModal(false);
  };

  useEffect(() => {
    dispatch(addMoodList);
  }, [dispatch]);

  return (
    <form className="model" onSubmit={handleSubmit}>
      <ul className="errors">
        {errors.length > 0 &&
          errors.map((error) => {
            return <li key={error}>{error}</li>;
          })}
      </ul>
        <div className="addmoodmodel">
      <h1 id="loginheader">Add Mood</h1>
      <label>
        <input
          className="nameinput"
          placeholder="Enter a new mood"
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
          Orange-Yellow
        </option>
      </select>
      <button
        className="loginbutton"
        type="submit"
        disabled={errors.length > 0 ? true : false}
      >
        Add
      </button>
      </div>
    </form>
  );
}

export default AddForm;
