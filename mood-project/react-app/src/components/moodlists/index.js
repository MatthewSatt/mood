import React, { useEffect, useState } from "react";
import {useDispatch, useSelector} from "react-redux";
import {Link} from 'react-router-dom'
import { loadUserMoods, deleteMoodlist, editMoodlist } from "../../store/moodlist";
import AddFormModal from "../AddMood";
import EditFormModal from "../EditMoodlist";
import { addMoodList } from "../../store/moodlist";
import EditForm from "../EditMoodlist/EditModal";
import './moodlists.css'
import { render } from "react-dom";


const Moodlists = () => {
    const dispatch = useDispatch();
    // const moodlists = useSelector((state) => state.moodlists)
    const moodlists = useSelector((state) => Object.values(state.moodlists))
    const userId = useSelector(state => state.session.user.id)
    const [showModal, setShowModal] = useState(false);
    const [showEditModal, setShowEditModal] = useState(false)

useEffect(() => {
    dispatch(deleteMoodlist)
}, [dispatch])

useEffect(() => {
    dispatch(editMoodlist)
}, [dispatch, showModal])

useEffect(() => {
    dispatch(loadUserMoods(userId));
}, [dispatch, showEditModal, showModal])


useEffect(() => {
    dispatch(addMoodList)
}, [dispatch])


const handleDelete = async (e) => {
    e.preventDefault()
    const id = e.target.id
    await dispatch(deleteMoodlist(id))

}

return (
    <>
        <div className="moodlists">
            <a id='addamood'><AddFormModal setShowModal={setShowModal} showModal={showModal}/></a>
            {moodlists?.map((mood) => (
                <div className='eachmoodlist' key={mood?.id}>
                <p id='moodname'>{mood?.name}</p>
                <p>{mood?.color}</p>
                <p id='end'>mood.id = {mood?.id}</p>
                <p id='end'>user.id = {userId}</p>
                <button onClick={handleDelete} id={mood?.id} className="deletebutton">Delete</button>
                <a className="editbutton"><EditFormModal mood={mood?.id} setShowEditModal={setShowEditModal} showEditModal={showEditModal}/></a>
            </div>
            ))}
        </div>
    </>
    )
}
export default Moodlists
