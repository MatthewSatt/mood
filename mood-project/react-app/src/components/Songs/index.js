import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { loadMoodSongs, removeMoodSong } from "../../store/songs";
import { loadUserMoods } from "../../store/moodlist";
import { Modal } from "../../context/Modal";
import { editSong } from "../../store/songs";
import "./Songs.css";
import { Link } from "react-router-dom";
import AddSongForm from "../AddSong";
import Player from "../SongPlayer";

const Songs = () => {
  const dispatch = useDispatch();
  const songs = useSelector((state) => state.songs);
  const user = useSelector((state) => state.session.user.id);
  const moodlists = useSelector((state) => Object.values(state.moodlists));
  const moodlistId = useParams();
  const {moodid} = useParams()
  const moodName = moodlists.find(name => name.id === +moodlistId.moodId)

  const [addSongModal, setAddSongModal] = useState(false);
  const [editSongModal, setEditSongModal] = useState(false);
  const [editSongErrors, setEditSongErrors] = useState([]);
  const [editId, setEditId] = useState("");
  const [editName, setEditName] = useState("");
  const [editArtist, setEditArtist] = useState("");
  const [editRating, setEditRating] = useState(1);
  const [editUserId, setEditUserId] = useState("");

  useEffect(() => {
    const editSongErrors = [];
    if (editName.length > 30)
      editSongErrors.push("Name must not be longer than 30 characters");
    if (editName.length < 3)
      editSongErrors.push("Name must not be shorter than 3 characters");
    if (editArtist.length > 20)
      editSongErrors.push("I said an artist not a book");
    if (editArtist.length < 1) editSongErrors.push("Must include an artist");
    if (editRating < 0) editSongErrors.push("Song rating must be at least 1");
    if (editRating > 10) editSongErrors.push("Song rating must be 10 or less");
    setEditSongErrors(editSongErrors);
  }, [editName, editArtist, editRating, editUserId, moodlistId]);

  const handleShowModalData = (song) => async (e) => {
    e.preventDefault();
    setEditId(song.id);
    setEditName(song.name);
    setEditArtist(song.artist);
    setEditRating(song.rating);
    setEditUserId(song.userId);
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

  if (user === songs[0]?.userId || moodlists[0]?.userId === user) {
    return (
      <div className="songscontainer">
        <div className="moodlist-songs">
          <h1 className="moodlistsongtitle">{moodName?.name} Songs</h1>
          <button
            value={addSongModal}
            onClick={(e) => setAddSongModal(true)}
            className="addmoodbutton"
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
                  <Link className="linktosinglesong" to={`/songs/${song.id}`}>
                    <div className="leftlink">
                      <div className="songName">
                        <h2 song={song} key={song.name}>
                          {song.name}
                        </h2>
                      </div>
                      <div className="songArtist">
                        <h3 song={song}>{song.artist}</h3>
                      </div>
                      <div className="songratingdiv">
                        {Array(song.rating).fill(<p>??????</p>)}
                      </div>
                    </div>
                    {/* <div className="rightlink">
                      <div className="songImage">
                        {song.song_image && (
                          <img id="songlistimage" src={song.song_image}></img>
                        )}
                      </div>
                    </div> */}
                  </Link>
                </div>

                <div className="songuseroptions">
                  <div className="songdetails" key={song.id}>
                    <Player prop={song.song_url} />
                  </div>
                  <div className="songcrudbuttons">
                    <button
                      id={song.id}
                      onClick={handleDelete}
                      className="songeditdeletebuttons"
                    >
                      Delete Song
                    </button>

                    <button
                      id={song.id}
                      className="songeditdeletebuttons"
                      onClick={handleShowModalData(song)}
                    >
                      Edit Song
                    </button>
                  </div>
                  {editSongModal && (
                    <Modal onClose={() => setEditSongModal(false)}>
                      <form className="editsongmodel" onSubmit={handleEdit}>
                        <ul className="errors">
                          {editSongErrors.length > 0 &&
                            editSongErrors.map((error) => {
                              return <li key={error}>{error}</li>;
                            })}
                        </ul>
                        <div className="editsongform">
                          <h1 id="addsongtitle">Edit Song Details</h1>
                          <div>Title</div>
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
                            <div></div>
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
                              min={1}
                              max={10}
                              value={editRating}
                              onChange={(e) => setEditRating(e.target.value)}
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
  }
  return <h1>Not Authorized</h1>;
};
// return <h1>Not Authorized</h1>
export default Songs;
