import "swiper/css";
import "../styles/pages/Home.scss";

import { Swiper, SwiperSlide } from "swiper/react";
import { getRooms } from "../utils/requester";
import Room from "../components/Room";
import { useState, useEffect } from "react";

const Home = () => {
  const [rooms, setRooms] = useState([]);
  const name = localStorage.getItem("name");

  useEffect(() => {
    async function fetchRooms(name) {
      const fetchedRooms = await getRooms(name);
      setRooms(fetchedRooms);
    }
    fetchRooms(name);
  }, [name]);

  return (
    <div>
      <header className="hero">
        <div className="hero-body">
          <p className="title">환영합니다! {name}님!</p>
          <p className="subtitle">퀴즈 목차를 선택해 주세요!</p>
        </div>
      </header>

      <main className="home-container">
        <Swiper slidesPerView={5} direction={"vertical"}>
          {rooms.map((room) => (
            <SwiperSlide key={room.id}>
              <Room room={room} />
            </SwiperSlide>
          ))}
        </Swiper>
      </main>
    </div>
  );
};

export default Home;
