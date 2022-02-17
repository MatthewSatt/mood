import React from "react";
import { NavLink } from "react-router-dom";
import "./HomePage.css";
// import '.../public/logo.jpeg'

const HomePage = () => {
  return (
    <>
    <div className="homepagebuttons">
          <NavLink role="button" className="homepagelogin" to="/login" exact={true} activeClassName="active">
            <h1 id='login-button'>Login</h1>
          </NavLink>
          <NavLink className="homepagesignup" to="/sign-up" exact={true} activeClassName="active">
            <h1>Sign Up</h1>
          </NavLink>
    </div>
    </>
  );
};

export default HomePage;
