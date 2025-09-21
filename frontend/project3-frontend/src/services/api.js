// src/services/api.js
import axios from "axios";

// Base URL for your Django backend API
const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

// Login request
export const loginUser = async (username, password) => {
  try {
    const response = await API.post("accounts/login/", { username, password });
    return response.data; // should return token or user info
  } catch (error) {
    throw error.response?.data || { detail: "Login failed" };
  }
};

export default API;
