# Recipe App

## Description
A brief description of your project, its purpose, and what it aims to achieve. This Recipe App allows users to create, manage, and share their favorite recipes. It includes user authentication, recipe management, and a user-friendly API.

## Features
- User registration and authentication
- Create, read, update, and delete recipes
- User-specific recipe management
- Token-based authentication for secure API access
- API documentation using DRF Spectacular

## Technologies Used
- __Django__: A high-level Python web framework for building web applications.
- __Django REST Framework__: A powerful toolkit for building Web APIs.
- __PostgreSQL__: A powerful, open-source object-relational database system.
- __Docker__: For containerization of the application.
- __Flake8__: For linting the code.

## Installation
### Prerequisites
- Python 3.x
- PostgreSQL
- Docker (optional, for containerized setup)

### Steps
1. Clone the repository:
```
git clone https://github.com/yourusername/recipe-app.git
cd recipe-app
```

2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages:
```
pip install -r requirements.txt
```

4. Set up the database:
- Create a PostgreSQL database and user.
- Update the database settings in app/app/settings.py.

5. Run migrations:
    python manage.py migrate

6. Run the development server:
    python manage.py runserver

## Usage
- Access the API at http://localhost:8000/api/.
- Use tools like Postman or cURL to interact with the API endpoints.

## API Endpoints
- __User Registration__: POST /api/user/create/
- __Token Generation__: POST /api/user/token/
- __Manage User__: GET /api/user/me/
- __Recipe Management:__
    - _List Recipes_: GET /api/recipe/recipes/
    - _Create Recipe_: POST /api/recipe/recipes/
    - _Update Recipe_: PATCH /api/recipe/recipes/{id}/
    - _Delete Recipe_: DELETE /api/recipe/recipes/{id}/

## Running Tests
To run the tests for the application, use the following command:
    python manage.py test

## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m "Your commit message").
4. Push your changes (git push origin feature/YourFeature).
5. Open a pull request to the main branch.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Inspiration from various recipe management applications.
- Thanks to the Django and Django REST Framework communities for their excellent documentation and support.