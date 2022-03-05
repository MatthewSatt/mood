import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { searchSongs } from '../../store/songs'
import {useHistory} from 'react-router-dom'

import './SearchBar.css'

function SearchBar() {
    const dispatch = useDispatch()
    const history = useHistory()
    const [search, setSearch] = useState([])
    const [errors, setErrors] = useState([])


    // const thesongs = finalResultData.filter(word =>{
    //     return (word[0].includes(searchTerm.toUpperCase()) || word[1].toUpperCase().includes(searchTerm.toUpperCase()))
    // })



    const handleSubmit = (e) => {
        e.preventDefault()
        history.push("/")
    }

    useEffect( async () => {
        let errors = []
        const songs = await dispatch(searchSongs())
        const eachSong = songs.map(song => song.name) // => ['Bored to Death', 'Nothing Inside', 'Demons', 'Warriyo', 'The Black Parade', "It's Time", 'Despacito']
        eachSong.forEach(item => {
            if(item.includes(search) && !(errors.includes(item)) && search.length > 0) {
                errors.push(item)
            }

        })
        setErrors(errors)
    }, [search])


  return (
    <form onSubmit={handleSubmit}>
        <input
        placeholder='Search Songs'
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        >
        </input>
        <ul className='dropdown'>

        {errors && errors.map(error => (
            <li key={error.id}>
                {error}
            </li>
        ))}
        </ul>
    </form>
  )
}

export default SearchBar
