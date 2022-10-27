import Cards from './components/Cards';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Signup from './components/Signup';
import Signin from './components/Signin';
import {
  Route,
  Routes
} from "react-router-dom";
function App() {
  return (
    <div>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Cards/>}/>
      <Route  path="/signin" element = {<Signin/>}/>
      <Route  path="/signup" element = {<Signup/>}/>
      </Routes>
      <Footer/>
    </div>
  )
}

export default App;