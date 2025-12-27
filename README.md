# Django Business Website

A professional business website built using Django, providing features for managing business operations such as client contact forms, newsletters, and more. This project demonstrates how to use Django in building a fully functional business website with modern features.

## Features

- **Contact Form**: Users can reach out via a simple contact form.
- **Newsletter Subscription**: Users can subscribe to newsletters with email.
- **Admin Dashboard**: A fully featured Django admin interface for managing contacts and newsletters.
- **Responsive Design**: The website is fully responsive and adapts to different screen sizes.
- **User Authentication**: Built-in support for user registration, login, and authentication.

## Technologies Used

- **Django**: Web framework for building the website.
- **Python**: Programming language used.
- **HTML/CSS**: Front-end structure and styling.
- **Bootstrap**: Responsive design for easy mobile compatibility.
- **SQLite**: Default database (can be switched to PostgreSQL or MySQL).
- **JavaScript**: For interactive front-end features.
  
## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/SaeidJavadi/Django-Business-Website.git
    cd Django-Business-Website
    ```

2. **Set up a virtual environment**:

    If you don’t have `virtualenv` installed, you can install it with:

    ```bash
    pip install virtualenv
    ```

    Create and activate the virtual environment:

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On MacOS/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

    Your website should now be accessible at `http://127.0.0.1:8000/`.

## Configuration

- **Database**: The project uses SQLite by default. If you want to switch to PostgreSQL or MySQL, modify the `DATABASES` setting in `settings.py` and install the corresponding database adapter (`psycopg2` for PostgreSQL or `mysqlclient` for MySQL).
  
- **Static and Media Files**: Ensure proper handling of static and media files in production by setting `STATIC_ROOT` and `MEDIA_ROOT` in `settings.py`.

## Screenshots

Add a few screenshots to showcase the look of your website (you can upload them in the repository or use external links).

![Homepage](https://via.placeholder.com/800x400.png?text=Homepage)
![Contact Form](https://via.placeholder.com/800x400.png?text=Contact+Form)

## Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Django**: The web framework used to build this website.
- **Bootstrap**: For making the website responsive.
- **SQLite**: The default database used for development.