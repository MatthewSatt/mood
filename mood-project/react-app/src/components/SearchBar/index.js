import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {Link, Redirect} from 'react-router-dom'
import { searchSongs } from '../../store/songs'
import {useHistory} from 'react-router-dom'

import './SearchBar.css'

function SearchBar() {
    const dispatch = useDispatch()
    const history = useHistory()
    const [search, setSearch] = useState([])
    const [errors, setErrors] = useState([])


    useEffect(() => {
        if(errors.length === 0) {
            return
        } else {
            history.push('/')
        }
    }, [errors])



    useEffect( async () => {
        let errors = []
        const songsObj = await dispatch(searchSongs())
        songsObj.forEach(item => {
            if(item.name.includes(search) && !(errors.includes(item)) && search.length > 0 && errors.length < 5) {
                errors.push(item)

            }

        })
        setErrors(errors)
    }, [search])


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
               <Link onClick={() => setSearch("")} className='linktosongs' to={`songs/${error.id}`}>{error.name}-{error.artist}</Link>
            </li>
        ))}
        </ul>
  </div>
  )
}

export default SearchBar
