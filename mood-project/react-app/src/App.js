import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignupForm';
import HomePage from './components/HomePage'
import NavBar from './components/NavBar/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
// import UsersList from './components/UsersList';
// import User from './components/User';
import Songs from './components/Songs'
import MoodLists from './components/Moodlists'
import { authenticate } from './store/session';
import OneSong from './components/OneSong';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>

        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>

        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>

        <ProtectedRoute path='/moodlists/:moodId' exact={true} >
          <Songs />
        </ProtectedRoute>

        <ProtectedRoute path='/songs/:songId' exact={true} >
          <OneSong />
        </ProtectedRoute>

        <ProtectedRoute path='/' exact={true} >
          <MoodLists />
        </ProtectedRoute>

        <Route path="/home" >
          <HomePage />
        </Route>

        <Route path="">
          <h1>Page does not exist</h1>
        </Route>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
