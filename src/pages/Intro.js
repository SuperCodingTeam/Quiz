import "../styles/pages/Intro.scss";
import Card from "../components/Card";

const Intro = () => {
  return (
    <div>
      <header className="hero">
        <div className="hero-body">
          <p className="title">환영합니다!</p>
          <p className="subtitle">SuperCodingTeam Quiz 사이트입니다!</p>
        </div>
      </header>

      <div style={{ textAlign: "center" }}>당신은 누구입니까?</div>
      <div className="section">
        <Card name="강은주" position="프론트엔드" />
        <Card name="박준원" position="프론트엔드" />
        <Card name="김태호" position="백엔드" />
        <Card name="조연우" position="백엔드" />
      </div>
    </div>
  );
};

export default Intro;
