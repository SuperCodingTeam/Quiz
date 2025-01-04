import { useEffect, useState } from "react";
import "../styles/components/Quiz.scss";

import { getScore, createScore } from "../utils/requester";
import Swal from "sweetalert2";

const Quiz = ({ idx, quiz }) => {
  const [isSubmit, setIsSubmit] = useState(false);
  const [score, setScore] = useState(isSubmit);

  const getColor = () => {
    return isSubmit ? (score ? "blue" : "red") : "black";
  };
  useEffect(() => {
    async function fetchSubmit() {
      const fetchedScore = await getScore(localStorage.getItem("name"));
      fetchedScore.forEach((element) => {
        if (element.quiz_uuid === quiz.quiz_uuid) {
          setIsSubmit(true);
          setScore(element.score);
        }
      });
    }
    fetchSubmit();
  }, [score]);
  return (
    <div
      className="quiz-container"
      style={{ border: `1px solid ${getColor()}` }}
    >
      <div className="quiz-number" style={{ color: getColor() }}>
        {idx + 1}
      </div>
      <div className="quiz-content" style={{ color: getColor() }}>
        {quiz.content}

        <div className="buttons" style={{ marginTop: "1vh" }}>
          <button
            className="button is-primary is-light is-large"
            disabled={isSubmit}
            onClick={async () => {
              setIsSubmit(true);
              setScore(quiz.answer === "O" ? true : false);
              await createScore(
                localStorage.getItem("name"),
                quiz.quiz_uuid,
                quiz.answer === "O" ? true : false
              );

              if (quiz.answer === "O" ? true : false) {
                return Swal.fire({
                  icon: "success",
                  title: "정답입니다!",
                  showConfirmButton: true,
                });
              } else {
                return Swal.fire({
                  icon: "error",
                  title: "오답입니다!",
                  text: "틀린 문제는 풀이를 제공합니다.",
                  showConfirmButton: true,
                });
              }
            }}
          >
            O
          </button>
          <button
            className="button is-danger is-light is-large"
            disabled={isSubmit}
            onClick={async () => {
              setIsSubmit(true);
              setScore(quiz.answer === "X" ? true : false);
              await createScore(
                localStorage.getItem("name"),
                quiz.quiz_uuid,
                quiz.answer === "X" ? true : false
              );

              if (quiz.answer === "X" ? true : false) {
                return Swal.fire({
                  icon: "success",
                  title: "정답입니다!",
                  showConfirmButton: true,
                });
              } else {
                return Swal.fire({
                  icon: "error",
                  title: "오답입니다!",
                  text: "틀린 문제는 풀이를 제공합니다.",
                  showConfirmButton: true,
                });
              }
            }}
          >
            X
          </button>
        </div>
        {isSubmit ? (
          score ? null : (
            <button
              className="button is-info is-light is-small"
              onClick={() => {
                return Swal.fire({
                  icon: "info",
                  title: "풀이",
                  text: quiz.explanation,
                  showConfirmButton: true,
                });
              }}
            >
              풀이
            </button>
          )
        ) : null}
      </div>
    </div>
  );
};

export default Quiz;
