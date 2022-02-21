import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { loadMoodSongs, removeMoodSong } from "../../store/songs";
import { Modal } from "../../context/Modal";
import { editSong } from "../../store/songs";
import './Songs.css'
import AddSongForm from "../AddSong";

// TODO: Get single moodlist for song page
// TODO: complete edit functionality
// TODO: get songs to play
// TODO: error validations on front and backend
// TODO: update styles
// TODO: add search all songs feature
// TODO: figure out the color wheel
// TODO: play music
// TODO: add an easter egg



const Songs = () => {
  const dispatch = useDispatch();
  const songs = useSelector((state) => state.songs);
  const user = useSelector((state) => state.session.user.id);
  const moodlistId = useParams();


{/* --------------------------ADD----------------------------------------------- */}

  const [addSongModal, setAddSongModal] = useState(false);
  const [editSongModal, setEditSongModal] = useState(false)
  const [x, setX] = useState("")
  const [editName, setEditName] = useState("")
  const [editArtist, setEditArtist] = useState("")
  const [editRating, setEditRating] = useState(0)
  const [editImage, setEditImage] = useState("")
  const [editUrl, setEditUrl] = useState("")

  const handleShowModalData = (e) => {
    e.preventDefault();
    setX(+e.currentTarget.id)
    setEditSongModal(true)
  }
  const handleEdit = async (e) => {
    e.preventDefault();
    const song = {
      "id": x,
      "name": editName,
      "artist": editArtist,
      "rating": editRating,
      "image_url": editImage,
      "song_url": editUrl,
      "moodlistId": Number(moodlistId['moodId']),
      "userId": user
    }
    await dispatch(editSong(song))
    setEditSongModal(false);
    dispatch(loadMoodSongs(moodlistId.moodId))
  };

const handleDelete = async (e) => {
  e.preventDefault();
  console.log("REMOVE THE ID OF THE THE SONG", e.target.id);
  await dispatch(removeMoodSong(e.target.id));
  return;
};




const handlePlay = (e) => {
  e.preventDefault();
  console.log("PLAY THIS THE THE IDDDDDDDD", e.target.id);
};




  useEffect(() => {
    dispatch(loadMoodSongs(moodlistId.moodId));
  }, [dispatch, moodlistId.moodId]);



  return (
    <div className="songscontainer">
      <div className="moodlist-songs">
        <h1 className="moodlistsongtitle">Moodlist Name</h1>
        <button
          value={addSongModal}
          onClick={(e) => setAddSongModal(true)}
          className="addsongbutton"
        >
          Add Song
        </button>
        {addSongModal && (
          <AddSongForm addSongModal={addSongModal} setAddSongModal={setAddSongModal}/>
        )}
        {songs.map((song, i) => (
          <div className="eachsong" id={song.id} key={song.id}>
            <div className="titleandartist">
              <p song={song} key={song.name}>
                {/* <span className="songlabelstitle">Title </span> */}
                {song.name}
              </p>
              <p song={song}>
                {/* <span className="songlabelsartist">Artist </span> */}
                {song.artist}
              </p>
            </div>
            <p song={song}>
              {/* <span className="songlabelsrating">Rating </span> */}
              {song.rating}
            </p>
            <p className="songimage">
              {/* <span className="songlabelsimage">Image </span> */}
              {song.image_url}
            </p>
            <p>
              {/* <span className="songlabelslink">SongLink </span> */}
              {song.song_url}
            </p>
            <div className="songuseroptions">

{/* --------------------------PLAYBUTTON----------------------------------------------- */}
              <button id={song.id} onClick={handlePlay} className="playsong">
                TODO:Play Button
              </button>





{/* --------------------------DELETE----------------------------------------------- */}


              <button
                id={song.id}
                onClick={handleDelete}
                className="deletesong"
              >
                Delete Song
              </button>



{/* --------------------------EDIT---------------------------------------------- */}


        <button
          id={song.id}
          className="editsong"
          onClick={(e) => handleShowModalData(e)}
        >
          Edit Song
        </button>
        {editSongModal && (
          <Modal onClose={() => setEditSongModal(false)}>
            <form className="editsongmodel" onSubmit={handleEdit}>
              <h1 id="addsongtitle">Edit Song Details</h1>
              <label>
                <input
                  className="songinfo"
                  placeholder="title"
                  type="text"
                  value={editName}
                  onChange={(e) => setEditName(e.target.value)}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="artist"
                  type="text"
                  value={editArtist}
                  onChange={(e) => setEditArtist(e.target.value)}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="rating"
                  type="text"
                  value={editRating}
                  onChange={(e) => setEditRating(Number(e.target.value))}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="image"
                  type="text"
                  value={editImage}
                  onChange={(e) => setEditImage(e.target.value)}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="url"
                  type="text"
                  value={editUrl}
                  onChange={(e) => setEditUrl(e.target.value)}
                />
              </label>
              <button className="modaleditsong" type="submit">Edit</button>
            </form>
          </Modal>
)}

{/* ------------------------------------------------------------------------ */}

            </div>
          </div>
        )).reverse()}
      </div>
    </div>
  );
};

export default Songs;
