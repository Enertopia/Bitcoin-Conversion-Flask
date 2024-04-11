Instructions to Run the Application

    Set up virtual environment:

    bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

bash

pip install -r requirements.txt

Initialize the database (if using Flask-Migrate):

bash

flask db init
flask db migrate -m "Initial migration."
flask db upgrade

Run the application:

bash

python main.py

Build and run with Docker (optional):

bash

docker build -t flask_conversion_app .
docker run -p 5000:5000 flask_conversion_app
