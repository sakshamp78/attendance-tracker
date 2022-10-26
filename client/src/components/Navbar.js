import React from 'react';
import icons8 from "../images/icons8.png";

function Navbar() {
  return (
    <nav className="navbar sticky-top  navbar-expand-lg navbar-dark" style={{backgroundColor : "#0B132B" , fontWeight : "bold"}}>
      <div className="container-fluid">
        <img src={icons8} alt="" width="34" height="34" className="d-inline-block align-text-top mx-2"/>
          Attendance Portal 
      </div>
    </nav>
  )
}

export default Navbar