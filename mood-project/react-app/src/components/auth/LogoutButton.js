import React from 'react';
import { useDispatch } from 'react-redux';
import { logout } from '../../store/session';
import "./Logout.css"

const LogoutButton = () => {
  const dispatch = useDispatch()
  // import { useSelector } from 'react-redux';
  // const user = useSelector((state) => state.session.user);
  const onLogout = async (e) => {
    await dispatch(logout());
  };

  return <button className='logoutbuttonmain' onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
