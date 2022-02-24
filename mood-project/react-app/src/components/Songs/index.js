import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { loadMoodSongs, removeMoodSong } from "../../store/songs";
import { Modal } from "../../context/Modal";
import { editSong } from "../../store/songs";
import "./Songs.css";
import AddSongForm from "../AddSong";
import Player from "../SongPlayer";

const Songs = () => {
  const dispatch = useDispatch();
  const songs = useSelector((state) => state.songs);
  const user = useSelector((state) => state.session.user.id);
  const moodlistId = useParams();


  const [addSongModal, setAddSongModal] = useState(false);
  const [editSongModal, setEditSongModal] = useState(false);
  const [editSongErrors, setEditSongErrors] = useState([]);
  const [editId, setEditId] = useState("");
  const [editName, setEditName] = useState("");
  const [editArtist, setEditArtist] = useState("");
  const [editRating, setEditRating] = useState(0);
  const [editUserId, setEditUserId] = useState("")

  useEffect(() => {
    const editSongErrors = [];
    if (editName.length > 30)
      editSongErrors.push("Name must not be longer than 30 characters");
    if (editName.length < 3)
      editSongErrors.push("Name must not be shorter than 3 characters");
    if (editArtist.length > 20)
      editSongErrors.push("I said an artist not a book");
    if (editArtist.length < 1) editSongErrors.push("Must include an artist");
    if (editRating < 0) editSongErrors.push("Song rating must be at least 0");
    if (editRating > 10) editSongErrors.push("Song rating must be 10 or less");
    setEditSongErrors(editSongErrors);
  }, [editName, editArtist, editRating, editUserId, moodlistId]);

  const handleShowModalData = (song) => async (e) => {
    e.preventDefault();
    setEditId(song.id);
    setEditName(song.name)
    setEditArtist(song.artist)
    setEditUserId(song.userId)
    setEditSongModal(true);
  };
  const handleEdit = async (e) => {
    e.preventDefault();
    const song = {
      id: editId,
      name: editName,
      artist: editArtist,
      rating: editRating,
      moodlistId: Number(moodlistId["moodId"]),
      userId: user,
    };
    await dispatch(editSong(song));
    setEditSongModal(false);
    dispatch(loadMoodSongs(moodlistId.moodId));
  };


  const handleDelete = async (e) => {
    e.preventDefault();
    await dispatch(removeMoodSong(e.target.id));
    return;
  };


  useEffect(() => {
    dispatch(loadMoodSongs(moodlistId.moodId));
  }, [dispatch]);

  return (
    <div className="songscontainer">
      <div className="moodlist-songs">
        <h1 className="moodlistsongtitle">Songs</h1>
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
          .map((song) => (
            <div className="eachsong" id={song.id} key={song.id}>
              <div className="titleandartist">
                <p song={song} key={song.name}>
                  {song.name}
                </p>
                <p song={song}>{song.artist}</p>
              </div>
              <h3>Rating: </h3>
              <h2>{song.rating}</h2>

              <div className="songuseroptions">
                <div className="songdetails" key={song.id}>
                  <Player prop={song.song_url} />
                </div>
                <button
                  id={song.id}
                  onClick={handleDelete}
                  className="deletesong"
                >
                  Delete Song
                </button>
                <button
                  id={song.id}
                  className="editsong"
                  onClick={handleShowModalData(song)}
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
                      <div className='editsongform'>
                      <h1 id="addsongtitle">Edit Song Details</h1>
                      <div>
                        Title
                      </div>
                      <label>
                        <input
                          className="songinfo"
                          type="text"
                          value={editName}
                          onChange={(e) => setEditName(e.target.value)}
                        />
                      </label>
                        Artist
                      <label>
                        <div>
                        </div>
                        <input
                          className="songinfo"
                          type="text"
                          value={editArtist}
                          onChange={(e) => setEditArtist(e.target.value)}
                        />
                      </label>
                        Rating
                      <label>
                        <input
                          className="songinfo"
                          type="number"
                          value={editRating}
                          onChange={(e) =>
                            setEditRating(Number(e.target.value))
                          }
                        />
                      </label>
                      <button
                        disabled={editSongErrors.length > 0 ? true : false}
                        className="modaleditsong"
                        type="submit"
                      >
                        Change
                      </button>
                      </div>
                    </form>
                  </Modal>
                )}
              </div>
            </div>
          ))
          .reverse()}
      </div>
    </div>
  );
};

export default Songs;
