# Sales-dashboard

Simple project to create dashboard with Streamlit

## Prerequisites

- [Docker](https://www.docker.com/get-started) or A working Python application.
- Basic understanding of the command line.
- Knowledge of the deployment method you choose

## Getting Started

### With Python

1. **Package Dependencies**: Make sure your Python application's dependencies are listed in a `requirements.txt` file.

2. **Virtual Environment (Optional but Recommended)**: Create a virtual environment to isolate your application's dependencies from the system-wide Python environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate `

1.  Install Dependencies: Install your application's dependencies:

    ```bash
    pip install -r requirements.txt

2.  Run Application: Start your application:

    ```bash

    python your_app.py

### With Docker

1. **Clone this repository to your local machine:**

   ```bash
   git clone https://github.com/acaldo/sales-dashboard-live.git
   cd sales-dashboard-live. 

1.  Build the Docker image:

    ```bash

    docker build -t streamlit-app .

2.  Run the Docker container:

    ```bash
    docker run -p 8501:8501 streamlit-app

3.  Open your web browser and navigate to [http://localhost:8501](http://localhost:8501/) to access the Streamlit app.

Project Structure
-----------------

-   `streamlit_app.py`: The main Streamlit app file.
-   `requirements.txt`: List of Python packages required for the app.
-   `Dockerfile`: Configuration for building the Docker image.
-   `.streamlit`: Themes
-   Other project-related files.

Additional Notes
----------------

-   The `streamlit_app.py` file contains the Streamlit app code. You can customize it to fit your specific use case.
-   Modify the `requirements.txt` file if you need to add or update dependencies.
-   The Docker image is built using the `Dockerfile`. You can customize the Dockerfile based on your project's requirements.
