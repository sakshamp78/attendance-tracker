import logo from './logo.svg';
// import './App.css';
import Item from './components/Item';

function App() {
  function add(x,y){
    console.log(x+y);
  }
  return (
    <div className="App">
      <ul>
        {/* <li>prakhar</li>
        <li>bhimeshwa</li>
        <li>saksham</li>
        <li>rohit</li> */}

        <Item isGreen={true} age="5" add={add}>prakhar</Item>
        <Item age="15">bhimeshwa</Item>
        <Item age="5">saksham</Item>
        <Item age="5">rohit</Item>
      </ul>
    </div>
  );
}

export default App;
