const LOAD_SONGS = 'song/loadSongs';
// const GET_ONE_SONG = 'song/oneSong'
// const ADD_SONG = 'song/addSongs';
// const UPDATE_SONG = 'song/updateSongs'
// const REMOVE_SONG = 'song/removeSongs'


export const loadSongs = (payload) => { // returned from server
    return {
        type: LOAD_SONGS,
        payload
    }
}

export const loadMoodSongs = (moodlistId) => async (dispatch) => {
    console.log('MOODID IN STORE', moodlistId)

    const res = await fetch(`/api/songs/moodlists/${moodlistId}`, {

    })
    if (res.ok) {
        const songs = await res.json();
        dispatch(loadSongs(songs))
        return songs
    }
}
//-------------------------------------------------------------------//
const GET_SONG = 'songs/GET_SONG';
//-------------------------------------------------------------------//
const ADD_SONG = 'songs/ADD_SONG';
//-------------------------------------------------------------------//
const EDIT_SONG = 'songs/EDIT_SONG';
//-------------------------------------------------------------------//
const REMOVE_SONG = 'songs/REMOVE_SONG';
//-------------------------------------------------------------------//
const initialState = []
export default function songReducer(state = initialState, action) {
    let newState;
    switch(action.type) {
        case LOAD_SONGS:
            return action.payload

        default:
            return state
    }
}
