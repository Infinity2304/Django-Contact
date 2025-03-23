"use client";
import { createContext, useState, useContext, useEffect } from "react";

export const AuthContext = createContext();

export const useAuthContext = () => {
    return useContext(AuthContext);
};

export const AuthContextProvider = ({ children }) => {
    const [AuthUser, setAuthUser] = useState(null);

    useEffect(() => {
        // Check for user_id cookie on component mount
        const userId = document.cookie.replace(/(?:(?:^|.*;\s*)user_id\s*=\s*([^;]*).*$)|^.*$/, "$1");

        if (userId) {
            setAuthUser(true); // Or fetch user data if needed
        } else {
            setAuthUser(false);
        }
    }, []);

    const value = {
        AuthUser,setAuthUser
    };

    return <AuthContext.Provider value={value}>
        {children}
        </AuthContext.Provider>;
};