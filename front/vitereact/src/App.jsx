import './App.css'
import UFBody from "./components/UFBody.jsx";

function App() {
  return (
      <div>
        <img className={'logo'} src="src/assets/uf.png" alt="uf"/>
        <h1>Consulta el valor de la UF</h1>
        <UFBody></UFBody>
      </div>
  )
}

export default App
