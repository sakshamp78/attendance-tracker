import React from 'react'
import './footer.css'

function Footer() {
    return (
        <>
            <footer className="site-footer">
                <div className="container">
                    <div className="row">
                        <div className="col-sm-12 col-md-6">
                            <h6>About</h6>
                            <p className="text-justify"> This website is a project for <b>Imbesideyou Development Task</b> </p>
                        </div>
                    </div>
                    <hr></hr>
                </div>
                <div className="container">
                    <div className="row">
                        <div className="col-md-8 col-sm-6 col-xs-12">
                            <p className="copyright-text">Copyright &copy; 2022 All Rights Reserved by &nbsp; 
                                <u><b>Saksham Pandey</b></u>
                            </p>
                        </div>

                        <div className="col-md-4 col-sm-6 col-xs-12">
                            <ul className="social-icons">
                                <li><a className="github" href="https://github.com/sakshamp78" target="_blank" rel="noopener noreferrer"><i className="fa fa-github"></i></a></li>
                                <li><a className="linkedin" href="https://www.linkedin.com/in/saksham-pandey-3183a9211/" target="_blank" rel="noopener noreferrer"><i className="fa fa-linkedin"></i></a></li>
                                <li><a className="facebook" href="https://www.facebook.com/saksham.pandey.3511/" target="_blank" rel="noopener noreferrer"><i className="fa fa-facebook"></i></a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </footer>
        </>
    )
}

export default Footer