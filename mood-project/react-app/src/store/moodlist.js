const GET_ALL_MOODLISTS = 'moodlists/GET_ALL_MOODLISTS';

export const loadMoods = (moodlists) => {
    return {
        type: GET_ALL_MOODLISTS,
        moodlists
    }
}
export const loadUserMoods = (id) => async (dispatch) => {

    const res = await fetch(`/api/moodlists/${id}`, {
        // headers: {"Content-Type": "application/json"}
    })
    if (res.ok) {
        const moods = await res.json();
        dispatch(loadMoods(moods))
        return moods
    }
}
//-------------------------------------------------------------------//
// const GET_MOODLIST = 'moodlist/GET_MOODLIST';

//-------------------------------------------------------------------//
const ADD_MOODLIST = 'moodlist/ADD_MOODLIST';

export const addMood = (mood) => {
    return {
        type: ADD_MOODLIST,
        mood
    }
}

export const addMoodList = (mood) => async (dispatch) =>{
    const res = await fetch(`/api/moodlists/new`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(
            mood
        )
    })
    if (res.ok){
        const newMood = await res.json();
        dispatch(addMood(newMood.mood))
        return newMood
    }
}

//-------------------------------------------------------------------//
const EDIT_MOODLIST = 'moodlist/EDIT_MOODLIST';

export const editMood = (payload) => {
    return {
        type: EDIT_MOODLIST,
        payload,
    }
}

export const editMoodlist = (moodlist) => async (dispatch) =>{
    const res = await fetch(`/api/moodlists/edit`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(
            moodlist
        )
    })
    if (res.ok){
        const changedMood = await res.json();
        dispatch(editMood(changedMood))
        return changedMood
    }
}
//-------------------------------------------------------------------//
const REMOVE_MOODLIST = 'moodlist/REMOVE_MOODLIST';

const deleteMood = (moodlist) => {
    return {
        type: REMOVE_MOODLIST,
        payload: moodlist,
    }
}
export const deleteMoodlist = (id) => async (dispatch) => {

    const res = await fetch(`/api/moodlists/${id}/delete`, {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'}
    })
    if(res.ok){
        const moodlist = await res.json();
        dispatch(deleteMood(moodlist))
        return "Sucess"
    } else {
        return null;
    }
}
//-------------------------------------------------------------------//
const initialState = []
export default function moodlistReducer(state = initialState, action) {
 let newState;
    switch (action.type) {
        case GET_ALL_MOODLISTS:
            return action.moodlists
        case ADD_MOODLIST:
            return [...state, action.mood];
        case REMOVE_MOODLIST:
            return state.filter((moodlist) => moodlist.id !== action.payload.id);
        case EDIT_MOODLIST:
            return{
                ...state,
                [action.payload.id]: action.payload
            }
        default:
            return state
    }
}
