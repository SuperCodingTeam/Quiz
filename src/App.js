import "bulma/css/bulma.css";
import "./styles/app.scss";

import Intro from "./pages/Intro";
import Home from "./pages/Home";
import Quiz from "./pages/Quiz";

import { Route, Routes } from "react-router-dom";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Intro />} />
      <Route path="/home" element={<Home />} />
      <Route path="/quiz/:room_uuid" element={<Quiz />} />
    </Routes>
  );
};

export default App;
