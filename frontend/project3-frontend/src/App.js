import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  // States for login
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // States for jobs
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Handle login
  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/token/", {
        username: username,
        password: password,
      });

      // Save token and role (hardcoded for now, update later if you have API)
      localStorage.setItem("token", response.data.access);

      // Example: assign roles manually for testing
      if (username === "admin1") localStorage.setItem("role", "admin");
      else if (username === "GowthamKantubothu") localStorage.setItem("role", "recruiter");
      else if (username === "SirijaBaratam") localStorage.setItem("role", "manager");
      else localStorage.setItem("role", "admin");

      setIsLoggedIn(true);
    } catch (err) {
      console.error("Login failed:", err.response?.data || err.message);
      setError("Login failed. Please check your credentials.");
    }
  };

  // Fetch jobs after login
  useEffect(() => {
    if (!isLoggedIn) return;

    const fetchJobs = async () => {
      setLoading(true);
      setError("");

      try {
        const role = localStorage.getItem("role");
        let endpoint = "";

        if (role === "admin") endpoint = "http://127.0.0.1:8000/api/jobs/admin/";
        else if (role === "recruiter") endpoint = "http://127.0.0.1:8000/api/jobs/recruiter/";
        else if (role === "manager") endpoint = "http://127.0.0.1:8000/api/jobs/manager/";
        else {
          setError("Role not found.");
          setLoading(false);
          return;
        }

        const token = localStorage.getItem("token");
        if (!token) {
          setError("Token not found. Please login.");
          setLoading(false);
          return;
        }

        const response = await axios.get(endpoint, {
          headers: { Authorization: `Bearer ${token}` },
        });

        setJobs(response.data);
      } catch (err) {
        console.error("Error fetching jobs:", err.response?.data || err.message);
        setError("Failed to fetch jobs.");
      } finally {
        setLoading(false);
      }
    };

    fetchJobs();
  }, [isLoggedIn]);

  // Render login form if not logged in
  if (!isLoggedIn) {
    return (
      <div style={{ padding: "20px" }}>
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <div>
            <label>Username:</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit">Login</button>
        </form>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    );
  }

  // Render job listings
  return (
    <div style={{ padding: "20px" }}>
      <h1>Job Listings</h1>
      {loading ? (
        <p>Loading jobs...</p>
      ) : error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : jobs.length === 0 ? (
        <p>No jobs available.</p>
      ) : (
        <ul>
          {jobs.map((job) => (
            <li key={job.id}>
              <strong>{job.title}</strong> - {job.description}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
