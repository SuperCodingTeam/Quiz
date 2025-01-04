import "../styles/pages/Quiz.scss";

import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { getQuiz } from "../utils/requester";
import Quiz from "../components/Quiz";

import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";

const QuizPage = () => {
  const { room_uuid } = useParams();
  const [quizs, setQuizs] = useState([]);

  useEffect(() => {
    async function fetchQuiz(room_uuid) {
      const fetchedQuiz = await getQuiz(room_uuid);
      setQuizs(fetchedQuiz);
    }

    fetchQuiz(room_uuid);
    console.log(quizs);
  }, [room_uuid]);

  return (
    <div className="quiz-page-container">
      <Swiper slidesPerView={5} direction={"vertical"}>
        {quizs.map((quiz, idx) => (
          <SwiperSlide key={quiz.quiz_uuid}>
            <Quiz quiz={quiz} idx={idx} />
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default QuizPage;
