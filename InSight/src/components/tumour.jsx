import { useState, useEffect } from "react";
import "./styles/tumour.css";

export const Tumour = () => {
  const [file, setFile] = useState(null);

  const handleSubmit1 = async (event) => {
    event.preventDefault();

    try {
      const formData = new FormData();
      formData.append('file', file);
      
      const response = await fetch('http://localhost:5000/python/function1', {
        method: 'POST',
        body: formData,
      });

      const text = await response.text();
      console.log(text);
    } 

    catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="tumour">
      <form
        action="/python/function1"
        method="post"
        enctype="multipart/form-data"
        onSubmit={handleSubmit1}
      >
        <div className="heading">Tumour MRI</div>
        <div className="heading">scan</div>
        <div className="form">
          <input
            id="file-upload"
            type="file"
            accept="image/*"
            onChange={(e) => setFile(e.target.files[0])}
          />
          <label for="file-upload" className="custom-file-upload">
            Choose file
          </label>
          <button id="file-submit1" className="" type="submit">
            Submit
          </button>
          <label for="file-submit1" className="custom-file-submit">
            Submit
          </label>
        </div>
      </form>
    </div>
  );
};
