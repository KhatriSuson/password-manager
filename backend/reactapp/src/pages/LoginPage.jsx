import React, { useState } from 'react';
import LoginForm from '../components/LoginForm';
import { useHistory } from 'react-router-dom';

const LoginPage = () => {
  const [user, setUser] = useState(null);
  const history =
