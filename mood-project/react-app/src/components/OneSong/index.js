import React, { useEffect, useState } from 'react'
import { getOneSong } from '../../store/songs'
import { useSelector, useDispatch } from 'react-redux'
import SearchBar from '../SearchBar'
import {useParams} from 'react-router-dom'
import Player from "../SongPlayer";
import './OneSong.css'

function OneSong() {
const songs = useSelector(state => state.songs)
const moodlists = useSelector(state => state.moodlists)
const user = useSelector(state => state.session.user)
const dispatch = useDispatch()
const {songId} = useParams()
const [song, setSong] = useState('')


useEffect(async () => {
  const song = await dispatch(getOneSong(Number(songId)))
  setSong(song)
}, [])


  return (
    <div className='onesong'>
      <div>
      <h1 className='onesongtitle'>{song.name}</h1>
      </div>
      <div>
      <h1 className='onesongartist'>{song.artist}</h1>
      </div>
      <img className='songimage' src={song.song_image}></img>
      {song.song_url !== '' &&(
      <div className='player'>
        <Player className='player' prop={song.song_url} />
      </div>
      )}
      <div>
      {!song.song_url && (
        <h1 className='errors'>Error with mp3 file</h1>
  )}

      </div>
    </div>
  )
}

export default OneSong
