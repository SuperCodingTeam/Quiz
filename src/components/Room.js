import "../styles/components/Room.scss";

const Room = ({ room }) => {
  return (
    <a
      className="room-container"
      style={{
        border: `2px solid ${
          room.category == "전체"
            ? "green"
            : room.category == "프론트엔드"
            ? "skyblue"
            : "purple"
        }`,
      }}
      href={`/quiz/${room.room_uuid}`}
    >
      <span className="room-number">{room.number}</span>
      <span className="room-content">{room.content}</span>
    </a>
  );
};

export default Room;
