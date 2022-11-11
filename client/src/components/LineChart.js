import React from 'react'
import { Line } from 'react-chartjs-2'
import 'chart.js/auto'


function LineChart (props) {

const {chartData,chartName}=props


let datasets=chartData.datasets



// function getRandomColor(num) {
//   var letters = '0123456789ABCDEF'.split('');
//   var colors=[]
//   for(var j=0;j<num;j++){
//   var color = '#';
//   for (var i = 0; i < 6; i++ ) {
//       color += letters[Math.floor(Math.random() * 16)];
//   }
//   colors.push(color)
// }
//   return colors;
// }


let colors=['#80B300','#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
'#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
 '#809900', '#E6B3B3']
for(let i=0;i<datasets.length;i++){
  datasets[i]['fill']=true
  datasets[i]['borderColor']=colors[i]
  datasets[i]['backgroundColor']=colors[i]
  console.log(datasets[i])
}

  const data = {
    labels: chartData.labels,
    datasets: datasets
  }

  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: chartName,
        font:{
          size:22
        }
        
      },
      tooltip: {
        mode: 'index'
      },
    },
    interaction: {
      mode: 'nearest',
      axis: 'x',
      intersect: false
    },
    scales: {


      // yAxes:{
      //   stacked:false,
        
      // },
      x: {
        title: {
          display: true,
          text: 'Year',
          font:{
            size:16
          }
        }
      },
     
      y: {
        stacked: true,
        ticks:{
          // display:false,
          stepSize:500,
        },
        min:100,
        title: {
          display: true,
          text: 'No of theses',
          font:{
            size:16
          },
        }
      }
    }
  }

  return <Line data={data} options={options} />
}

export default LineChart
