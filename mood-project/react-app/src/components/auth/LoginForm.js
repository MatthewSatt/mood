import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import * as sessionActions from "../../store/session";
import { login } from "../../store/session";
import "./LoginForm.css";
const LoginForm = () => {
  const history = useHistory();

  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const handleDemo = async (e) => {
    e.preventDefault();
    await dispatch(sessionActions.login("demo@aa.io", "password"));
    history.push("/");
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <>
     <div class="container">
    <div class="key white black" id='key1' ><h3></h3></div>
    <div class="key white black" id='key2'><h3></h3></div>
    <div class="key white" id='key3'><h3></h3></div>
    <div class="key white black" id='key4'><h3></h3></div>
    <div class="key white black" id='key5' ><h3></h3></div>
    <div class="key white black" id='key6'><h3></h3></div>
    <div class="key white" id='key7'><h3></h3></div>
    <div class="key white black" id='key8' ><h3></h3></div>
    <div class="key white black" id='key9'><h3></h3></div>
    <div class="key white" id='key10'><h3 id='key10'></h3></div>
   </div>
    <form onSubmit={onLogin} className="loginuserform">
      <div className="loginuserformcontent">
        <div className="loginpageheader">mood</div>
        <div className="loginerrorsss">
          {errors.map((error, ind) => (
            <div className="loginerrorsss" key={ind}>
              {error}
            </div>
          ))}
        </div>
        <div className="loginformcontainer">
          <div className="coverkeys">
            <div id="leftkey"></div>
            <div id="middlekey"></div>
            <div id='rightkey'></div>
            </div>
          <h4 id="logindirection">Login to your account</h4>
        <div className="emailcontainer">
          <div className="emailinput">
          <input
            name="email"
            placeholder="Email"
            type="text"
            value={email}
            onChange={updateEmail}
            />
          </div>
        </div>

          <div className="passwordcontainer">
            <label id="labelforemail" htmlFor="password">
            </label>
          <input
            name="password"
            placeholder="Password"
            type="password"
            value={password}
            onChange={updatePassword}
            />
            </div>
          <div className="loginbuttoncontainer">
            <button id="loginbutton" type="submit">
              Login
            </button>
            <button id="logindemobutton" onClick={handleDemo}>
              Demo
            </button>
          </div>
        </div>
      </div>
    </form>
            </>
  );
};

export default LoginForm;
