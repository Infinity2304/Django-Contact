import React from 'react'
import { useState } from 'react'
import { useAuthContext } from '../context/AuthContext'
import toast from 'react-hot-toast'

const useLogin = () => {
    const [loading, setloading] = useState(false) //Setting the loading state for submitting the user data
    const {setAuthUser} = useAuthContext();

    const login = async ( {username, password} ) => {
        const success = handleInputErrors({ username, password });

        if (!success) return; //Client side validation

        setloading(true);
        try {
            //Sending the data to server(backend)
            const res = await fetch("/api/login", { 
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password })
            });

            //Getting the error from server side    
            const data = await res.json();
            if (data.error) {
                throw new Error(data.error);
            }

            // Save user to local storage
            localStorage.setItem("user-info", JSON.stringify(data));

            //Saving as context
            // setAuthUser(data);
        } catch (error) {
            //handling errors
            toast.error(error.message);
        }finally {
            setloading(false);
        }
    }
  return { login, loading };
}

export default useLogin

// Client side validation
function handleInputErrors({ username, password}) {
    if (!username || !password) {
        toast.error("Please fill all the fields");
        return false;
    }
    return true;
}