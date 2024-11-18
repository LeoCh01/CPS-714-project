import { useNavigate } from "react-router-dom";

function BackButton({ className }) {
  let navigate = useNavigate();
  return (
    <>
      <button className={className} onClick={() => navigate(-1)}>
        Back
      </button>
    </>
  );
}

export default BackButton;
