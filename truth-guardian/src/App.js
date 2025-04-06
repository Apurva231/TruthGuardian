import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Home from "./pages/Home";
import TextDetector from "./pages/TextDetector";
import ImageDetector from "./pages/ImageDetector";
import AudioDetector from "./pages/AudioDetector";
import Insights from "./pages/Insights";
import About from "./pages/About";
import Tools from "./pages/Tools";
import Logout from "./pages/Logout";
import Chatbot from "./components/ChatbotWidget";
import Navbar from "./components/Navbar";
import ProtectedRoute from "./pages/ProtectedRoute";
import "./App.css";

function App() {
  return (
    <Router>
      <MainLayout />
    </Router>
  );
}

function MainLayout() {
  const location = useLocation();
  const hideNavbarPaths = ['/',"/login", "/signup"];

  const showNavbar = !hideNavbarPaths.includes(location.pathname);

  return (
    <>
      {showNavbar && <Navbar />}
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/" element={<Login />} />  <Route
          path="/home"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route
          path="/text"
          element={
            <ProtectedRoute>
              <TextDetector />
            </ProtectedRoute>
          }
        />
        <Route
          path="/image"
          element={
            <ProtectedRoute>
              <ImageDetector />
            </ProtectedRoute>
          }
        />
        <Route
          path="/audio"
          element={
            <ProtectedRoute>
              <AudioDetector />
            </ProtectedRoute>
          }
        />
        <Route
          path="/insights"
          element={
            <ProtectedRoute>
              <Insights />
            </ProtectedRoute>
          }
        />
        <Route
          path="/tools"
          element={
            <ProtectedRoute>
              <Tools />
            </ProtectedRoute>
          }
        />
        <Route
          path="/about"
          element={
            <ProtectedRoute>
              <About />
            </ProtectedRoute>
          }
        />
        <Route path="/logout" element={<Logout />} />
        <Route path="*" element={<Login />} />
      </Routes>
      {showNavbar && <Chatbot />}
    </>
  );
}

export default App;