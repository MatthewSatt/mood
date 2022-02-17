
import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'
// import '.../public/logo.jpeg'

const NavBar = () => {
  return (
    <nav className='navbar'>
      <ul className='navbar-main'>
        <li className='home-page-logo'>
          <NavLink to='/home' exact={true} activeClassName='active'>
           <img src="../../public"></img>
          </NavLink>
        </li>
        <h1 className='title'>mood</h1>
        <li className='logout-button'>
          <LogoutButton />
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;
