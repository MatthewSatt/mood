import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { loadMoodSongs, removeMoodSong } from "../../store/songs";
import { Modal } from "../../context/Modal";
import { addSong } from "../../store/songs";
import "./Songs.css";

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

  const [addSongModal, setAddSongModal] = useState(false);
  const [editModal, setEditModal] = useState(false);
  const [name, setName] = useState("")
  const [artist, setArtist] = useState("")
  const [rating, setRating] = useState(0)
  const [image, setImage] = useState("")
  const [url, setUrl] = useState("")

  useEffect(() => {
    dispatch(loadMoodSongs(moodlistId.moodId));
  }, [dispatch]);

  useEffect(() => {
    dispatch(removeMoodSong);
  }, [dispatch]);

  useEffect(() => {
    dispatch(addSong)
  }, [dispatch])

  const handlePlay = async (e) => {
    e.preventDefault();
    console.log("PLAY THIS THE THE IDDDDDDDD", e.target.id);
  };

  const handleAdd = async (e) => {
    const x = Number(moodlistId['moodId'])
    e.preventDefault();
    const song = {
      "name": name,
      "artist": artist,
      "rating": rating,
      "image_url": image,
      "song_url": url,
      "moodlistId": x,
      "userId": user
    }
    await dispatch(addSong(song))
    setAddSongModal(false);
    dispatch(loadMoodSongs(moodlistId.moodId))
  };

  const handleEdit = async (e) => {
    e.preventDefault();
    console.log("EDIT THIS THE THE IDDDDDDDD", e.target.id);
  };

  const handleDelete = async (e) => {
    e.preventDefault();
    console.log("REMOVE THE ID OF THE THE SONG", e.target.id);
    await dispatch(removeMoodSong(e.target.id));
    return;
  };

  return (
    <div className="songscontainer">
      <div className="moodlist-songs">
        <h1 className="moodlistsongtitle">Moodlist Name</h1>




          {/* FIXME: ADD SONG COMPLETE ----------------------------------------------------------------- */}
        <button
          value={addSongModal}
          onClick={(e) => setAddSongModal(true)}
          className="addsongbutton"
        >
          Add Song
        </button>
        {addSongModal && (
          <Modal onClose={() => setAddSongModal(false)}>
            <form className="addsongmodel">
              <h1 id="addsongtitle">Add Song</h1>
              <label>
                <input
                  className="songinfo"
                  placeholder="title"
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="artist"
                  type="text"
                  value={artist}
                  onChange={(e) => setArtist(e.target.value)}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="rating"
                  type="text"
                  value={rating}
                  onChange={(e) => setRating(e.target.value)}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="image"
                  type="text"
                  value={image}
                  onChange={(e) => setImage(e.target.value)}
                />
              </label>
              <label>
                <input
                  className="songinfo"
                  placeholder="url"
                  type="text"
                  value={url}
                  onChange={(e) => setUrl(e.target.value)}
                />
              </label>
              <button onClick={handleAdd} className="modaladdsong" type="submit">Add</button>
            </form>
          </Modal>
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








              <button id={song.id} onClick={handlePlay} className="playsong">
                TODO:Play Button
              </button>








              <button
                id={song.id}
                onClick={handleDelete}
                className="deletesong"
              >
                Delete Song
              </button>









              <button id={song.id} onClick={handleEdit} className="editsong">
                TODO:Edit Song
              </button>








            </div>
          </div>
        )).reverse()}
      </div>
    </div>
  );
};

export default Songs;
