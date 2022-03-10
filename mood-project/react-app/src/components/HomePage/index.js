import React from "react";
import { NavLink, Link } from "react-router-dom";
import "./HomePage.css";
// import '.../public/logo.jpeg'

const HomePage = () => {
  return (
    <>
    <div className="moodhome">
      <div className="homebody">
    <h1 id='homepagetitle'>Welcome to <span>m</span>o<span></span>o<span></span>d<span></span></h1>
    <h3>Organize and play music with your custom moodlists!</h3>
    <div className="homepagebuttons">
          <NavLink role="button" className="homepagelogin" to="/login" exact={true} activeClassName="active">
            <h1 id='login-button'>Login</h1>
          </NavLink>
          <NavLink className="homepagesignup" to="/sign-up" exact={true} activeClassName="active">
            <h1>Sign Up</h1>
          </NavLink>
    </div>
    </div>
    <div className="personallinks">
    </div>
    </div>
    <div className="homepagefooter">
    <a id='github' href='https://github.com/MatthewSatt'>Github</a>
    <h6 className="me">Created By: Matthew Satterwhite </h6>
    <a id ='linkedin' href="https://www.linkedin.com/in/matthew-satterwhite-008970211/">LinkedIn</a>

    </div>
    </>
  );
};

export default HomePage;
