import { useState } from "react";
import "./App.css";

import { Navbar } from "./components/navbar";
import { Tumour } from "./components/tumour";
import { Lung } from "./components/lung";
import { Parkinsons } from "./components/parkinsons";

function App() {
  return (
    <>
      <Navbar />
      <div className="main">
        <div className="component main-tumour">
          <Tumour />
        </div>
        <div className="component main-lung">
          <Lung />
        </div>
        <div className="component main-park">
          <Parkinsons />
        </div>
      </div>
    </>
  );
}

export default App;
