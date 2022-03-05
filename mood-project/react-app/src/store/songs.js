const LOAD_SONGS = "song/loadSongs";

export const loadSongs = (payload) => {
  // returned from server
  return {
    type: LOAD_SONGS,
    payload,
  };
};

export const loadMoodSongs = (moodlistId) => async (dispatch) => {
  const res = await fetch(`/api/songs/moodlists/${moodlistId}`, {});
  if (res.ok) {
    const songs = await res.json();
    dispatch(loadSongs(songs));
    return songs;
  }
};
//-------------------------------------------------------------------//
const PLAY_SONG = "songs/PLAY_SONG";

export const playS = (songId) => {
  return {
    type: PLAY_SONG,
    songId,
  };
};

export const playSong = (songId) => async (dispatch) => {
    const res = await fetch(`/api/songs/play/${songId}`);
    if (res.ok) {
      const songs = await res.json();
      dispatch(playSong(songs));
      return songs;
    }
  };
//-------------------------------------------------------------------//
const ADD_SONG = "songs/ADD_SONG";

export const addS = (payload) => {
  return {
    type: ADD_SONG,
    payload,
  };
};
export const addSong = (song) => async (dispatch) => {
  const res = await fetch(`/api/songs/new`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(song),
  });
  if (res.ok) {
    const newsong = await res.json();
    dispatch(addS(newsong));
    return newsong;
  }
};

//-------------------------------------------------------------------//
const EDIT_SONG = "songs/EDIT_SONG";

export const editS = (payload) => {
  return {
    type: EDIT_SONG,
    payload,
  };
};

export const editSong = (song) => async (dispatch) => {
  const res = await fetch(`/api/songs/edit`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(song),
  });
  if (res.ok) {
    const updatedSong = await res.json();
    dispatch(editS(updatedSong));
    return updatedSong;
  }
};

//-------------------------------------------------------------------//
const REMOVE_SONG = "songs/REMOVE_SONG";

export const removeSong = (song) => {
  return {
    type: REMOVE_SONG,
    song,
  };
};

export const removeMoodSong = (songId) => async (dispatch) => {
  const res = await fetch(`/api/songs/delete/${songId}`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  });
  if (res.ok) {
    const song = await res.json();
    dispatch(removeSong(song));
    return song;
  } else {
    return null;
  }
};
//-------------------------------------------------------------------//
const SEARCH_SONGS = 'songs/SEARCH_SONGS'

const searchS = () => {
  return {
    type: searchSongs,
  };
};

export const searchSongs = () => async dispatch => {
  const res = await fetch('/api/songs/search')
  if(res.ok) {
    const songs = await res.json()
    dispatch(searchS(songs))
    return songs
  }
}
//-------------------------------------------------------------------//
const initialState = [];
export default function songReducer(state = initialState, action) {
  let newState;
  switch (action.type) {
    case LOAD_SONGS:
      return action.payload;
    case ADD_SONG:
      return [...state, action.payload];
    case REMOVE_SONG:
      return state.filter((song) => song.id !== action.song.id);
    case EDIT_SONG:
      // WHY ARE YOU LIKE THIS
      return (newState = [...state, (action.payload.id = action.payload)]);
    case PLAY_SONG:
        return action.song
    case SEARCH_SONGS:
      return [...state]


    default:
      return state;
  }
}
