import LineChart from './components/LineChart';
import './App.css'
import { useEffect,useState } from 'react';
import {api} from './api-config'


function App() {

const [annunalchartData, setannunalChartData] = useState(null)


const getChartData= ()=>{
  api.get('/annual').then((res)=>setannunalChartData(res.data)).catch((err)=>console.log(err))
}



  useEffect(()=>{
  getChartData()
  },[])

  if(annunalchartData ){
    return(
    <div className="App">
      <div className='chart'>
          <LineChart chartData={annunalchartData} chartName='Annual total of all the PhDs published by Dutch Universities '/>
        </div>
    </div>
    )
  }
  else{
    return (
      <h1>loading</h1>
      );
  }
  
}

export default App;
