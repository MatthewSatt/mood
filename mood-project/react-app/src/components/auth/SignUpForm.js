import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import './SignupForm.css'

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data)
      }
    }
  };
useEffect(() => {
  const errors = []
  if(username.length < 5) errors.push("Username must be greater than 5")
  if(username.length > 30) errors.push("Username must be less than 30")
  if((!(email.includes("@"))))errors.push("Must be a valid email.")
  if(password.length < 5) errors.push("You must have a longer password")
  if(repeatPassword !== password) errors.push("Passwords don't match")
  setErrors(errors)
}, [username, password, email, password, repeatPassword])

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };



  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <form onSubmit={onSignUp} className='signupuserform'>
      <div className='signupuser'>
      <div className='loginerrors'>
        {errors.map((error, ind) => (
          <div className='loginerror' key={ind}>{error}</div>
        ))}
      </div>
      <div>
        <div className='namecontainer'>
        <label>User Name</label>
        </div>
        <input
          type='text'
          name='username'
          onChange={updateUsername}
          value={username}
        ></input>
      </div>
      <div>
        <div className='namecontainer'>
          <div>
            <label>Email</label>
          </div>
        </div>
        <input
          type='text'
          name='email'
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div className='namecontainer'>
        <div>
          <label>Password</label>
        </div>
        </div>
        <input
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
          ></input>
      <div>
          <div className='namecontainer'>
            <label>Repeat Password</label>

          </div>
        <input
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <button disabled={errors.length > 0 ? true : false }id="loginbutton2" type='submit'>Sign Up</button>
      </div>
    </form>
  );
};

export default SignUpForm;
