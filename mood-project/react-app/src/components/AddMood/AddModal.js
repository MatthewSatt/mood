import "./AddModel.css";
import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addMoodList } from "../../store/moodlist";


// import "./EditForm.css"

function AddForm({ setShowModal }) {
  const userId = useSelector((state) => state.session.user.id);
  const dispatch = useDispatch();
  const [name, setName] = useState("");
  const [color, setColor] = useState('')
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

      <h1 id="loginheader">New mood</h1>
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
        onClick={(e) => setColor(e.target.value)}
      >
        <option className="redstyle" value="red">
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
        disabled={errors.length > 0 ? true : false}
      >
        Add
      </button>
    </form>
  );
}

export default AddForm;
