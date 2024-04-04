import { useState } from "react";
import "./styles/parkinsons.css";

export const Parkinsons = () => {
  const [file, setFile] = useState(null);

  const handleSubmit3 = async (event) => {
    event.preventDefault();

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("http://localhost:5000/python/function3", {
        method: "POST",
        body: formData,
      });

      const text = await response.text();
      console.log(text);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="parkinsons">
      <form
        action="/python/function3"
        method="post"
        enctype="multipart/form-data"
        onSubmit={handleSubmit3}
      >
        <div className="heading">Alzheimer's</div>
        <div className="heading">MRI scan</div>
        <div className="form">
          <input id="file-upload3" type="file" accept="image/*" onChange={(e) => setFile(e.target.files[0])}/>
          <label for="file-upload3" className="custom-file-upload">
            Choose file
          </label>
          <button id="file-submit3" className="" type="submit">
            Submit
          </button>
          <label for="file-submit3" className="custom-file-submit">
            Submit
          </label>
        </div>
      </form>
      <img src="" alt="" />
    </div>
  );
};
