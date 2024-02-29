import './App.css'
import ufImage from './assets/uf.png';
import UFBody from "./components/UFBody.jsx";

function App() {
  return (
      <div>
        <img className={'logo'} src={ufImage} alt="uf"/>
        <h1>Consulta el valor de la UF</h1>
        <UFBody></UFBody>
      </div>
  )
}

export default App
