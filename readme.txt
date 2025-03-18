** TASK 2

Time Difference Calculation API
This REST API calculates the absolute time difference in seconds between two timestamps. The input is a set of timestamp pairs, and the API returns the absolute difference between each pair.

1. Installation
Ensure you have Python 3.8+ installed on your machine.



Install the required dependencies:


pip install -r requirements.txt

The requirements.txt file should contain the necessary dependencies like fastapi, pydantic, and uvicorn.

2. Running the Application
Using Uvicorn:
After installing the dependencies, you can run the FastAPI application using Uvicorn by executing the following command in your terminal:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Once the server is running, you should see output similar to the following:


INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started server process [12708]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

The API will be available at http://127.0.0.1:8000.

Swagger UI for Testing:
To interact with the API via a user interface, you can access the Swagger UI at:


http://127.0.0.1:8000/docs

In Swagger UI, you can test the API by clicking on the POST /calculate_time_difference endpoint and then entering the input in the JSON format. For example:


{
  "input_text": "2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000"
}
After clicking "Execute", you will receive the time difference in seconds as the output.

3. API Endpoints
POST /calculate_time_difference
This endpoint accepts a POST request with a JSON body containing the input text. The input text should follow the format:

The first line contains an integer T, the number of test cases.
Each subsequent pair of lines contains two timestamps in the format:

Day dd Mon yyyy hh:mm:ss +xxxx
Request Body Example:

{
  "input_text": "2\nSun 10 May 2015 13:54:36 -0700\nSun 10 May 2015 13:54:36 -0000\nSat 02 May 2015 19:54:36 +0530\nFri 01 May 2015 13:54:36 -0000"
}
Response Example:

[
  "25200",
  "88200"
]
The response is a JSON array containing the absolute time differences between the pairs of timestamps, in seconds.

4. Error Handling
The API will return an error if any input is invalid:

If the input text cannot be parsed correctly, a 400 Bad Request status code with an error message will be returned.
If the number of test cases (T) does not match the number of lines provided, the API will raise an error indicating the mismatch.
5. Testing the API
You can test the API using tools like Postman or cURL. Here's how to send a request using cURL:

** TASK 3

Build the Docker Images:

Navigate to the project directory where your Dockerfile is located and build the Docker images for each app (app1, app2, app3):

docker-compose build
Run the Containers:

After building the images, you can start the containers using Docker Compose:

docker-compose up
Access the Application:

Once the containers are running, you can access the FastAPI endpoints via the exposed ports:
App1: http://localhost:8001
App2: http://localhost:8002
App3: http://localhost:8003
You can also access the Swagger UI at http://localhost:8001/docs (for app1).
Stopping the Containers:

To stop the running Docker containers, use the following command:

docker-compose down