import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { loadMoodSongs, removeMoodSong } from "../../store/songs";
import { Modal } from "../../context/Modal";
import { editSong } from "../../store/songs";
import "./Songs.css";
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

  {
    /* --------------------------Edit----------------------------------------------- */
  }

  const [addSongModal, setAddSongModal] = useState(false);
  const [editSongModal, setEditSongModal] = useState(false);
  const [x, setX] = useState("");
  const [editName, setEditName] = useState("");
  const [editArtist, setEditArtist] = useState("");
  const [editRating, setEditRating] = useState(0);
  const [editImage, setEditImage] = useState("");
  const [editUrl, setEditUrl] = useState("");
  const [editSongErrors, setEditSongErrors] = useState([]);

  useEffect(() => {
    const editSongErrors = [];
    if (editName.length > 30)
      editSongErrors.push("Name must not be longer than 30 characters");
    if (editName.length < 3)
      editSongErrors.push("Name must not be shorter than 3 characters");
    if (editArtist.length > 20)
      editSongErrors.push("I said an artist not a book");
    if (editArtist.length < 1)
      editSongErrors.push("Must include an artist");
    if (editRating < 0) editSongErrors.push("Song rating must be at least 0");
    if (editRating > 10) editSongErrors.push("Song rating must be 10 or less");
    setEditSongErrors(editSongErrors);
  }, [editName, editArtist, editRating]);

  const handleShowModalData = (e) => {
    e.preventDefault();
    setX(+e.currentTarget.id);
    setEditSongModal(true);
  };
  const handleEdit = async (e) => {
    e.preventDefault();
    const song = {
      id: x,
      name: editName,
      artist: editArtist,
      rating: editRating,
      image_url: editImage,
      song_url: editUrl,
      moodlistId: Number(moodlistId["moodId"]),
      userId: user,
    };
    await dispatch(editSong(song));
    setEditSongModal(false);
    dispatch(loadMoodSongs(moodlistId.moodId));
  };

  {
    /* --------------------------Edit----------------------------------------------- */
  }

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
          <AddSongForm
            addSongModal={addSongModal}
            setAddSongModal={setAddSongModal}
          />
        )}
        {songs
          .map((song, i) => (
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
                      <ul className="errors">
                        {editSongErrors.length > 0 &&
                          editSongErrors.map((error) => {
                            return <li key={error}>{error}</li>;
                          })}
                      </ul>
                      <h1 id="addsongtitle">Edit Song Details</h1>
                      <label>
                        Title
                        <input
                          className="songinfo"
                          type="text"
                          value={editName}
                          onChange={(e) => setEditName(e.target.value)}
                        />
                      </label>
                      <label>
                        Artist
                        <input
                          className="songinfo"
                          type="text"
                          value={editArtist}
                          onChange={(e) => setEditArtist(e.target.value)}
                        />
                      </label>

                      <label>
                        Rating
                        <input
                          className="songinfo"
                          type="number"
                          value={editRating}
                          onChange={(e) =>
                            setEditRating(Number(e.target.value))
                          }
                        />
                      </label>
                      <label>
                        Image
                        <input
                          className="songinfo"
                          placeholder="Optional"
                          type="text"
                          value={editImage}
                          onChange={(e) => setEditImage(e.target.value)}
                        />
                      </label>
                      <label>
                        Song Link
                        <input
                          className="songinfo"
                          placeholder="Optional"
                          type="text"
                          value={editUrl}
                          onChange={(e) => setEditUrl(e.target.value)}
                        />
                      </label>
                      <button disabled={editSongErrors.length > 0 ? true : false} className="modaleditsong" type="submit">
                        Change
                      </button>
                    </form>
                  </Modal>
                )}

                {/* ------------------------------------------------------------------------ */}
              </div>
            </div>
          ))
          .reverse()}
      </div>
    </div>
  );
};

export default Songs;
