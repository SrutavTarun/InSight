import { useState } from "react";
import "./styles/lung.css";

export const Lung = () => {
  const [file, setFile] = useState(null);

  const handleSubmit2 = async (event) => {
    event.preventDefault();

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("http://localhost:5000/python/function2", {
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
    <div className="lung">
      <form
        action="/python/function2"
        method="post"
        enctype="multipart/form-data"
        onSubmit={handleSubmit2}
      >
        <div className="heading">Chest X-ray</div>
        <div className="heading">scan</div>
        <div className="form">
          <input id="file-upload2" type="file" accept="image/*" onChange={(e) => setFile(e.target.files[0])}/>
          <label for="file-upload2" className="custom-file-upload">
            Choose file
          </label>
          <button id="file-submit2" className="" type="submit">
            Submit
          </button>
          <label for="file-submit2" className="custom-file-submit">
            Submit
          </label>
        </div>
      </form>
      <img src="" alt="" />
    </div>
  );
};
