# Django / React todo

Demo for a decoupled, full stack React/Django Todo application. Code taken from [here](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react). This version has adapted that code to use funciton-based React components.

## Install:
- Set up a `venv` folder in the project's root directory: `python -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install the Python dependencies: `pip install -r reqs.txt`
- Install React dependencies (from `frontend` directory): `yarn install`
## Running backend:
- From the root directory: `cd backend`
- Run the backend: `python manage.py runserver`

## Running frontend:
- From the root directory: `cd frontend`
- `yarn start`