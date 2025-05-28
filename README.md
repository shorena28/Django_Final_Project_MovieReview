🎬 Movie Reviews - Django Project

This is a Django-based Movie Review web application that allows users to add movies, review them, and see others' reviews.

🔧 Features

🔐 **Custom User Model** — Login via email (`USERNAME_FIELD = 'email'`)
🧾 **Movie CRUD functionality**
⭐ **Genre and Watchlist support**
📝 **Review submission system**
🧪 **Unit testing** with `pytest` and `pytest-django`
🛠 **Custom Management Command** — Displays the last 10 movies and object counts in terminal
💠 **Base UI template (`base.html`)** styled with Bootstrap


📁 Project Structure

Movie_Reviews/
├── movies_app/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── templates/
│ │ └── base.html
│ ├── tests/
│ │ ├── test_movie.py
│ └── management/
│ └── commands/
│ └── show_info.py
├── users_app/
│ └── CustomUser model
├── manage.py
├── pytest.ini
└── README.md

🚀 How to Run the Project Locally

1. 📦 Clone the Repository

git clone https://github.com/your-username/movie-reviews.git
cd movie-reviews
2. 🐍 Set Up a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. 📥 Install Dependencies
Make sure you have Django and other required packages:

pip install -r requirements.txt
If you don’t have requirements.txt, install manually:

pip install django pytest pytest-django Pillow
4. 🛠 Apply Migrations

python manage.py makemigrations
python manage.py migrate
5. 👤 Create a Superuser (Optional)

python manage.py createsuperuser
6. ▶️ Run the Development Server

python manage.py runserver
Visit in your browser:

http://127.0.0.1:8000/
🧪 Running Tests
Use pytest to run all tests:

pytest
⚙️ Run Custom Management Command
To display the last 10 movies and count of all database objects:

python manage.py show_info
