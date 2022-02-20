import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { loadMoodSongs, removeMoodSong } from "../../store/songs";
import "./Songs.css";

const Songs = () => {
  const dispatch = useDispatch();
  const songs = useSelector((state) => state.songs);
  const user = useSelector((state) => state.session.user);
  const moodlistId = useParams();

  const [songId, setSongId] = useState("");

  useEffect(() => {
    dispatch(loadMoodSongs(moodlistId.moodId));
  }, [dispatch]);

  useEffect(() => {
    dispatch(removeMoodSong);
  }, [dispatch]);

  const handleDelete = async (e) => {
    e.preventDefault();
    console.log("THE ID OF THE THE SONG", e.target.id);
    await dispatch(removeMoodSong(e.target.id));
    return;
  };

  return (
    <div className="songscontainer">
      <div className="moodlist-songs">

        <h1 className="moodlistsongtitle">Moodlist Name</h1>
        <div className="addsongbutton">Add Song</div>
        {songs.map((song, i) => (
          <div className="eachsong" songId={song.id} key={song.id}>
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
            <div className="playsong">Play Button</div>
              {/* <div><DeleteSong /></div>
              <div><EditSong /></div> */}
              <div id={song.id} onClick={handleDelete} className="deletesong">
                Delete Song
              </div>
              <div id={song.id} className="editsong">Edit Song</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Songs;
