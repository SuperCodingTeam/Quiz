import { useEffect } from "react";

const Home = () => {
  var name;
  useEffect(() => {
    name = localStorage.getItem("name");
  });
  return <div>Home</div>;
};

export default Home;
