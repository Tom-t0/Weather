# Weather
A simple Python script to fetch and display current weather information for any city using the OpenWeatherMap API.
Features
City-based search: Automatically gets the latitude and longitude from a city name.

Weather data retrieval: Fetches current temperature, high, low, and humidity.

Clean output: Displays weather information in a simple, user-friendly format.

Getting Started
Follow these steps to get the app up and running on your local machine.

1. Prerequisites
Make sure you have Python installed. You'll also need to install a few libraries using pip:
pip install requests
pip install python-dotenv

3. OpenWeatherMap API Key
This project requires an API key from OpenWeatherMap to access weather data.
Sign up for a free account at OpenWeatherMap.
Once you have your API key, create a new file named .env in the root directory of your project.
Add the following line to the .env file, replacing your_api_key_here with your actual key:

API_KEY="your_api_key_here"
Note: The .env file is included in .gitignore, so your API key will not be uploaded to GitHub. This is a crucial security step.

3. How to Run
After setting up your API key, you can run the program from your terminal:
python your_script_name.py
Replace your_script_name.py with the actual name of your Python file.
The program will then prompt you to enter a city name.
