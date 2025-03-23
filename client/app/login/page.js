"use client"
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import useLogin from '@/hooks/useLogin';
import { useState, useEffect } from 'react';
import { redirect } from 'next/dist/server/api-utils';
import Cookies from 'js-cookie';
import { useAuthContext } from '@/context/AuthContext';

export default function Login() {

  const [inputs, setInputs] = useState({
    username: '',
    password: ''
});

  const { login, loading } = useLogin();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(inputs);
}
  return (
    <div className="fixed inset-0 bg-slate-700 flex flex-col justify-center items-center">
      <div className="bg-cyan-800 p-5 rounded-2xl flex flex-col gap-4 items-center">
        <h1>Contact App</h1>
        <TextField
          id="standard-password-input"
          label="Username"
          type="username"
          autoComplete="current-password"
          variant="standard"
          value={inputs.username}
          onChange={(e) => setInputs({...inputs, username: e.target.value})}
        />
        <TextField
          id="standard-password-input"
          label="Password"
          type="password"
          autoComplete="current-password"
          variant="standard"
          value={inputs.password}
          onChange={(e) => setInputs({...inputs, password: e.target.value})}
        />
        <Button variant="contained" onClick={handleSubmit} disabled={!inputs.username || !inputs.password ? true:false}>
        Submit
        </Button>
        <Button variant="contained">
        SignUp
        </Button>

      </div>
    </div>
  )
}
