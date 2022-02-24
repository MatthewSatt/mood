// import React, { useState } from "react";
// import {useHistory} from 'react-router-dom'
// import { useDispatch, useSelector } from "react-redux";
// import {editMoodlist, loadUserMoods} from "../../store/moodlist";
// import { StoreEnhancer } from "redux";
// import "./EditForm.css"

// function EditForm({ setShowEditModal, mood, catcher}) {

//     const user = useSelector((state) => state.session.user)
//     const dispatch = useDispatch();

//     const [name, setName] = useState("");
//     const [color, setColor] = useState("");


//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     const newmoodlist = {
//         "id": mood,
//         'name': name,
//         'color': color,
//     }


//     await dispatch(editMoodlist(newmoodlist))
//     // await dispatch(loadUserMoods(user.id))
//     setShowEditModal(false)

//   };

//   return (

//     <form className="edit" onSubmit={handleSubmit}>
//       {/* <ul className="errors">
//         {errors.map((error, idx) => (
//           <li key={idx}>{error}</li>
//         ))}
//       </ul> */}

//       <h1 id="loginheader">Edit</h1>
//         <label>
//           <input
//             className="userinput"
//             placeholder="New Mood"
//             type="text"
//             value={name}
//             onChange={(e) => setName(e.target.value)}
//           />
//         </label>
//         <label>
//           <input
//             className="passwordinput"
//             placeholder="Color"
//             type="text"
//             value={color}
//             onChange={(e) => setColor(e.target.value)}

//           />
//         </label>
//         <button className="loginbutton" type="submit">Edit</button>
//     </form>
//   );
// }

// export default EditForm;
