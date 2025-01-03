import "../styles/components/Card.scss";

const Card = ({ name, position }) => {
  return (
    <a
      class="card"
      href="/home"
      onClick={() => {
        localStorage.setItem("name", name);
      }}
    >
      <div class="card-image">
        <figure class="image is-3by4">
          <img src={`./assets/${name}.jpg`} />
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <p class="title is-4">{name}</p>
            <p class="subtitle is-8">{position}</p>
          </div>
        </div>

        <div class="content">
          {name} <br />
          {position} 개발자 입니다.
          <br />
        </div>
      </div>
    </a>
  );
};

export default Card;
