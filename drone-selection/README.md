# Drone Selection Application

This project is a web application built using the Flask framework to help users select suitable drones based on their requirements.

## Project Structure

```
drone-selection
├── app.py                # Main application file that defines the drone data and selection logic
├── requirements.txt      # Lists the required Python libraries and dependencies
├── templates
│   └── index.html       # HTML template for rendering the user interface
└── README.md            # Documentation for setting up and running the application
```

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory.

```bash
cd drone-selection
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, execute the following command:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`. You can access it through your web browser.

## Usage

Once the application is running, you can use the web interface to input your drone requirements (payload, range, and endurance) and select a suitable drone based on the provided data.

## License

This project is open-source and available under the MIT License.