# PicsParler

PicsParler is a social web application built with Django, designed for sharing and commenting on pictures. Users can create accounts, post pictures, follow other users, and engage with posts through likes and comments.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

PicsParler is a platform where users can:
- Share pictures.
- Follow other users and see their posts.
- Like and comment on pictures.
- Receive notifications for activities on their posts.

## Features

- User Authentication (Sign Up, Login, Logout)
- Profile Creation and Management
- Picture Uploading
- Commenting on Pictures
- Liking Pictures
- Following Users
- User Feeds
- Notifications

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- pip (Python package installer)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/PicsParler.git
    cd PicsParler
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application running.

## Usage

1. **Sign Up/Login**: Create a new account or log into an existing one.
2. **Profile Management**: Update your profile details and upload a profile picture.
3. **Posting Pictures**: Upload and share your pictures with the community.
4. **Interactions**: Like and comment on posts from other users.
5. **Follow Users**: Follow users to see their posts in your feed.
6. **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

Please ensure your code follows our coding standards and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

