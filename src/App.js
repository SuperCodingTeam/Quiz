import "bulma/css/bulma.css";
import "./styles/app.scss";

import Intro from "./pages/Intro";
import Home from "./pages/Home";
import { Route, Routes } from "react-router-dom";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Intro />} />
      <Route path="/home" element={<Home />} />
    </Routes>
  );
};

export default App;
