import "./styles/lung.css";

export const Lung = () => {
  return (
    <div className="lung">
      <form action="/t" method="post" enctype="multipart/form-data">
      <div className="heading">Upload X-ray</div>
        <div className="heading">scan</div>
        <div className="form">
            <input id="file-upload" type="file" accept="image/*" />
            <label for="file-upload" className="custom-file-upload">
              Choose file
            </label>
            <button id="file-submit" className="" type="submit">
              Submit
            </button>
            <label for="file-submit" className="custom-file-submit">
              Submit
            </label>
        </div>
      </form>
      <img src="" alt="" />
    </div>
  );
};
