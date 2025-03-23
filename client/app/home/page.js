"use client"
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState, useEffect } from 'react';
import { redirect } from 'next/navigation';
import { useAuthContext } from '@/context/AuthContext';

export default function Home() {

  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")


  return (
    <div className="fixed inset-0 bg-slate-700 flex flex-col justify-center items-center">
      <div className="bg-cyan-800 p-5 rounded-2xl flex flex-col gap-4 items-center">
        <h1>Home</h1>
      </div>
    </div>
  )
}
