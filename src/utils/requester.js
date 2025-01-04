const host = "http://18.207.176.98:3000/";

const getRooms = async (name) => {
  const response = await fetch(`${host}room/${name}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const data = await response.json();
  return data;
};

const getQuiz = async (room_uuid) => {
  const response = await fetch(`${host}quiz/${room_uuid}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const data = await response.json();
  return data;
};

const getScore = async (name) => {
  const response = await fetch(`${host}score/${name}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const data = await response.json();
  return data;
};

const createScore = async (name, quiz_uuid, score) => {
  const response = await fetch(
    `${host}score?name=${name}&quiz_uuid=${quiz_uuid}&score=${score}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    }
  );

  const data = await response.json();
  return data;
};

export { getRooms, getQuiz, getScore, createScore };
