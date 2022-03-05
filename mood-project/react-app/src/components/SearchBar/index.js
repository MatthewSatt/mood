import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {Link} from 'react-router-dom'
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



    useEffect( async () => {
        let errors = []
        const songsObj = await dispatch(searchSongs())
        // const eachSong = songs.map(song => song.name) // => ['Bored to Death', 'Nothing Inside', 'Demons', 'Warriyo', 'The Black Parade', "It's Time", 'Despacito']
        songsObj.forEach(item => {
            if(item.name.includes(search) && !(errors.includes(item)) && search.length > 0) {
                errors.push(item)

            }

        })
        setErrors(errors)
    }, [search])
    console.log(typeof(errors))
    console.log(errors)

  return (
      <div className='searchbar'>
        <input
        placeholder='Search Songs'
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        >
        </input>
        <ul className='songoptionscontainer'>
        {errors.length > 0 && errors.map(error => (
            <li className='eachsongoption' key={error.id}>
               <Link className='linktosongs' to={`songs/${error.id}`}>{error.name}</Link>
            </li>
        ))}
        </ul>
  </div>
  )
}

export default SearchBar
