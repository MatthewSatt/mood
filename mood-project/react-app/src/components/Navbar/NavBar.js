
import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import SearchBar from '../SearchBar';
import './NavBar.css'

const NavBar = () => {
  const user = useSelector((state) => state.session.user);
  return (
    <nav className='navbar'>
      <div className='navbar-main'>
        <div className='home-page-logo'>
          <NavLink to='/' exact={true} activeClassName='active'>
           <img className="moodlogoimage" alt='whatever' src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE04ozIKvVCBiRbRYzCBhr6w5AInT7-ue1GA&usqp=CAU" />
          </NavLink>
        </div>
        <div className='searchbox'>
          <SearchBar />
        </div>
        <h1 className='title'>mood</h1>
        {user &&
        <div className='logged-in-nav'>

        <div className='logout-button'>
          <LogoutButton />
        </div>
        </div>
        }
      </div>
    </nav>
  );
}

export default NavBar;
