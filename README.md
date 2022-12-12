<p align="center">
<img width="410" alt="the-small" src="https://user-images.githubusercontent.com/14722995/206960778-a66af496-bed0-440e-8d0e-8ada872d7236.png">
</p>

# Medieval Name Generator - Powered by OpenAI

This is a medieval name generator app which uses the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework and is optionally set up to deploy to Heroku. Heroku worker configuration is set up in `Procfile`. Follow the instructions below to get set up.

## Live Demo
[Live Demo on Heroku](https://stormy-anchorage-84211.herokuapp.com/)

## Setup and run with flask

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/) or use `brew`.

*Note: Make sure you're using version <= `python-3.10.8` because one of the requirements doesn't work with newer versions (I think it's pandas - don't qoute me on this though).*

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd ai-lord-generator
   ```

4. Create a new virtual environment (Note: this might be `python` rather than `python3` depending on your setup)

   ```bash
   $ python3 -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements (Note: this might be `pip` rather than `pip3` depending on your setup)

   ```bash
   $ pip3 install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app locally using Flask.

   ```bash
   $ flask run
   ```
   
You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!


## Setup and run with Heroku

1. Optionally, the project is configured to be able to run with Heroku locally using the Heroku CLI or deployed to a dyno.

2. Setup following this guide [python-and-heroku](https://devcenter.heroku.com/articles/getting-started-with-python).
