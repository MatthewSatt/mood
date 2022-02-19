import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { loadMoodSongs } from "../../store/songs";
import "./Songs.css"

const Songs = () => {
  const dispatch = useDispatch();
  const songs = useSelector((state) => state.songs);
  const user = useSelector((state) => state.session.user);
  const moodlistId = useParams();

  useEffect(() => {
    dispatch(loadMoodSongs(moodlistId.moodId));
  }, [dispatch]);

  return (
    <div className="moodlist-songs">
      <h1>Moodlist Name</h1>
        {songs.map((song, i) => (
          <div className="eachsong">
            <p song={song} key={song.id}>
              <span className="songlabelstitle">Title </span>
              {song.name}
            </p>
            <p song={song} key={song.id}>
              <span className="songlabelsartist">Artist </span>
              {song.artist}
            </p>
            <p song={song} key={song.id}>
              <span className="songlabelsrating">Rating </span>
              {song.rating}
            </p>
            <p song={song} key={song.id}>
              <span className="songlabelsimage">Image </span>{song.image_url}
            </p>
            <p song={song} key={song}>
              <span className="songlabelslink">SongLink </span>
              {song.song_url}
            </p>
            <div>Play Button</div>
            {/* <div><DeleteSong /></div>
          <div><EditSong /></div> */}
            <div>Delete Song</div>
            <div>Edit Song</div>
          </div>
        ))}
      </div>
  );
};

export default Songs;
