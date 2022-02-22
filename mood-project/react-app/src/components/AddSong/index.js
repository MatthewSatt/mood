import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Modal } from "../../context/Modal";
import { useParams } from "react-router-dom";
import { addSong } from "../../store/songs";
import './AddSong.css'

function AddSongForm({ setAddSongModal }) {
  const dispatch = useDispatch();
  // const songs = useSelector((state) => state.songs);
  const userId = useSelector((state) => state.session.user.id);
  const moodlistId = useParams();

  const [name, setName] = useState("");
  const [artist, setArtist] = useState("");
  const [rating, setRating] = useState(1);
  const [image, setImage] = useState("");
  const [url, setUrl] = useState("");
  const [songErrors, setSongErrors] = useState([]);

  useEffect(() => {
    const songErrors = [];
    if (name.length > 30)
      songErrors.push("Name must not be longer than 30 characters");
    if (name.length < 3)
      songErrors.push("Name must not be shorter than 3 characters");
    if (artist.length > 20) songErrors.push("I said an artist not a book");
    if (artist.length < 1) songErrors.push("Must include an artist");
    if (rating < 0) songErrors.push("Song rating must be at least 0");
    if (rating > 10) songErrors.push("Song rating must be 10 or less");
    setSongErrors(songErrors);
  }, [name, artist, rating]);

  console.log(rating)


  const handleAdd = async (e) => {
    const y = Number(moodlistId["moodId"]);
    e.preventDefault();
    const song = {
      name: name,
      artist: artist,
      rating: Number(rating),
      image_url: image,
      song_url: url,
      moodlistId: y,
      userId: userId,
    };
    await dispatch(addSong(song));
    setAddSongModal(false);
  };

  // useEffect(() => {
  //   dispatch(addSong);
  // }, [dispatch]);

  return (
    <>
      <Modal onClose={() => setAddSongModal(false)}>
        <form className="addsongmodel">
          <ul className="errors">
            {songErrors.length > 0 &&
              songErrors.map((error) => {
                return <li key={error}>{error}</li>;
              })}
          </ul>
          <div className="addsongform">
          <h1 id="addsongtitle">Add Song</h1>
          <label>
            Name
            <input
              className="songinfo"
              placeholder="title"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </label>
          <label>
            Artist
            <input
              className="songinfo"
              type="text"
              value={artist}
              onChange={(e) => setArtist(e.target.value)}
            />
          </label>
          <label>
            Rating
            <input
              className="songinfo"
              placeholder="rating"
              type="number"
              value={rating}
              onChange={(e) => setRating(e.target.value)}
            />
          </label>
          Image
          <label>
            <input
              className="songinfo"
              placeholder="Optional"
              type="text"
              value={image}
              onChange={(e) => setImage(e.target.value)}
            />
          </label>
          Song Link
          <label>
            <input
              className="songinfo"
              placeholder="Optional"
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              />
          </label>
          <button disabled={songErrors.length > 0 ? true : false} onClick={handleAdd} className="modaladdsong" type="submit">
            Add
          </button>
              </div>
        </form>
      </Modal>
    </>
  );
}

export default AddSongForm;
