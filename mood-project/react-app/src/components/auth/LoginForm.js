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
    <form onSubmit={onLogin} className="loginuserform">
      <div className="loginuserformcontent">
        <div className="loginerrors">
          {errors.map((error, ind) => (
            <div className="loginerror" key={ind}>
              {error}
            </div>
          ))}
        </div>
        <div className="emailcontainer">
          <div>
            <label id="labelforemail" htmlFor="email">
              Email
            </label>
          </div>
          <input
            name="email"
            type="text"
            value={email}
            onChange={updateEmail}
          />
        </div>
        <div>
          <div className="passwordcontainer">
            <label id="labelforemail" htmlFor="password">
              Password
            </label>
          </div>
          <input
            name="password"
            type="password"
            value={password}
            onChange={updatePassword}
          />
          <div className="loginbuttoncontainer">
            <button id="loginbutton" type="submit">
              Login
            </button>
            <button id="loginbutton" onClick={handleDemo}>
              Demo
            </button>
          </div>
        </div>
      </div>
    </form>
  );
};

export default LoginForm;
