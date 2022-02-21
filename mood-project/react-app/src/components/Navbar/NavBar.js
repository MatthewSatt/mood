
import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './NavBar.css'

const NavBar = () => {
  const user = useSelector((state) => state.session.user);
  return (
    <nav className='navbar'>
      <ul className='navbar-main'>
        <li className='home-page-logo'>
          <NavLink to='/' exact={true} activeClassName='active'>
           <img className="moodlogoimage" alt='whatever' src="/logo.jpeg" />
          </NavLink>
        </li>
        <h1 className='title'>mood</h1>
        {user &&
        <li className='logout-button'>
          <LogoutButton />
        </li>
        }
      </ul>
    </nav>
  );
}

export default NavBar;
