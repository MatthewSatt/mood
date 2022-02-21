
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { Modal } from '../../context/Modal';
import { useParams } from "react-router-dom";
import { addSong } from "../../store/songs";



function AddSongForm({ addSongModal, setAddSongModal }) {
  const dispatch = useDispatch()
  const songs = useSelector((state) => state.songs);
  const user = useSelector((state) => state.session.user.id);
  const moodlistId = useParams();


  const [name, setName] = useState("")
  const [artist, setArtist] = useState("")
  const [rating, setRating] = useState(0)
  const [image, setImage] = useState("")
  const [url, setUrl] = useState("")

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
  }

  useEffect(() => {
    dispatch(addSong)
  }, [dispatch, name, artist, rating, image, url])



  return (
    <>
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
    </>
  );
}

export default AddSongForm;
