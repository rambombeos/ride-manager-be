# Installation Guide for RAMBS Ride Manager Backend

This guide will walk you through the process of setting up and running the RAMBS Ride Manager backend application.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL

## Steps

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/rambs-ride-manager-backend.git
   cd rambs-ride-manager-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the PostgreSQL database:
   - Create a new database for the project
   - Update the database configuration in `settings.py` or use environment variables

6. Set up environment variables:
   - Create a `.env` file in the project root
   - Add necessary environment variables (e.g., SECRET_KEY, DATABASE_URL)

7. Run database migrations:
   ```
   python manage.py migrate
   ```

8. Create a superuser (admin) account:
   ```
   python manage.py createsuperuser
   ```

9. Start the development server:
   ```
   python manage.py runserver
   ```

The backend should now be running on `http://localhost:8000/`.

## Additional Setup

- To create sample users for testing, use the custom management command:
  ```
  python manage.py create_sample_users <total_users>
  ```
  Replace `<total_users>` with the number of users you want to create.
  For example, to create 10 sample users:
  ```
  python manage.py create_sample_users 10
  ```

- To create sample rides for testing, use the custom management command:
  ```
  python manage.py create_sample_rides <total_users>
  ```
  Replace `<total_rides>` with the number of rides you want to create.
  For example, to create 10 sample rides:
  ```
  python manage.py create_sample_rides 10
  ```

- For more information on available commands, please refer to the [Commands Documentation](README.COMMANDS.md).

- For production deployment, consider using a production-grade web server like Gunicorn and a reverse proxy like Nginx.

## Troubleshooting

If you encounter any issues during the installation process, please refer to the project's documentation or open an issue on the GitHub repository.
