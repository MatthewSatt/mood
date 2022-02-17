import React, { useEffect } from "react";
import {useDispatch, useSelector} from "react-redux";
import { loadUserMoods, deleteMoodlist, editMoodlist } from "../../store/moodlist";

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
    dispatch(loadUserMoods(userId));
    // let data = {
    //     "id": 2,
    //     "name": "Matthew",
    //     "color": "blue",
    // }
    // dispatch(editMoodlist(data))
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
                <button onClick={handleEdit} id={mood.id} className="editbutton">Edit</button>
            </div>
            ))}
        </div>
    </>
    )
}
export default Moodlists
