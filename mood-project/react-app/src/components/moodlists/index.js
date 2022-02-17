import React, { useEffect, useState } from "react";
import {useDispatch, useSelector} from "react-redux";
import {Link} from 'react-router-dom'
import { loadUserMoods, deleteMoodlist, editMoodlist } from "../../store/moodlist";
import EditFormModal from "../EditMoodlist";
import EditForm from "../EditMoodlist/EditModal";
import './moodlists.css'


const Moodlists = () => {
    const dispatch = useDispatch();
    // const moodlists = useSelector((state) => state.moodlists)
    const moodlists = useSelector((state) => Object.values(state.moodlists))
    const userId = useSelector(state => state.session.user.id)


useEffect(() => {
    dispatch(deleteMoodlist)
}, [dispatch])

useEffect(() => {
    dispatch(editMoodlist)
}, [dispatch])

useEffect(() => {
    dispatch(loadUserMoods(userId));
}, [dispatch, userId])

const addNewMood = (e) => {
    e.preventDefault()
    console.log("Open Model to create MoodList")
    // return <AddMoodModel />
}

const handleEdit = (e) => {
    e.preventDefault()
    const id = e.target.id
    console.log(`Open Modal to edit moodlist.id ${id}`)
}

const handleDelete = (e) => {
    e.preventDefault()
    const id = e.target.id
    dispatch(deleteMoodlist(id))
    return
}

return (
    <>
    <button onClick={addNewMood} id='addamood'>Add New Mood</button>
        <div className="moodlists">
            {moodlists?.map((mood) => (
                <div className='eachmoodlist' key={mood.id}>
                <p id='moodname'>{mood.name}</p>
                <p>{mood.color}</p>
                <p id='end'>mood.id = {mood.id}</p>
                <p id='end'>user.id = {userId}</p>
                <button onClick={handleDelete} id={mood.id} className="deletebutton">Delete</button>
                <a className="editbutton"><EditFormModal id={mood.id} /></a>
            </div>
            ))}
        </div>
    </>
    )
}
export default Moodlists
