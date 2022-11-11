# Author Cafe Assignment

  **client** dir is the frontend.

  **server** dir is the backend.

  **data** dir contains the csv and json files.

I have used react-chartjs-2 and chart.js in frontend.

In backend i have used fastapi and mongodb for database


## To run the fastapi 

* first create virtual enviroment

  ``` bash
  cd server
  python -m venv venv
  ```

* install the python packages 
  
  ```bash
  pip install -r  requirements.txt 
  ```

* to start the server
  
  ```bash
  uvicorn main:app
  ```


## To run frontend 

* first install npm packages
  
  ```bash
  cd client
  npm i
  npm start
  ```