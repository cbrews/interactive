# mvflask-scaffold
mvflask-scaffold is a "formalization" of a Python/Flask scaffold that I've been using for quickly starting Flask MVP projects.  It's based on Digital Ocean's [excellent guide for structing large flask projects ](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications) (with some of the more complex modularization removed).  I've primarily been using it for MVP micro-service development.

## Components
This scaffold comes pre-installed with flask (of course), and uses mysql and sqlalchemy connectors (because that's what I'm usually starting with).  You can update the requirements.txt to include another database connector if you prefer.

## Configuration
1. Clone this repository and cd into the project directory
2. Install and run [venv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

    ```
    $ pip install virtualenv
    $ virtualenv venv
    $ . venv/bin/activate
    ```
3. Install dependencies

    ```
    $ pip install -r requirements.txt
    ```
4. Run project

    ```
    $ python app.py
    ```

From there you can update your git remote and start developing!  Configuration parameters should be configured in the root directory config.py.

# TODO
1. Finish story work
2. New decorator that wraps routes for: auth handling, blueprinting of modules, json response
