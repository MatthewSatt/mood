import React from "react";
import { NavLink, Link } from "react-router-dom";
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

    <h6>Created By: Matthew Satterwhite </h6>
    <a href='https://github.com/MatthewSatt'>Github</a>
    <div></div>
    <a href="https://www.linkedin.com/in/matthew-satterwhite-008970211/">LinkedIn</a>
    </>
  );
};

export default HomePage;
