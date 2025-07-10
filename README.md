# Django Twitter Clone

A simple Twitter-like microblogging web application built with Django 5.2.4. Users can post short messages ("tweets"), view a list of tweets, and delete their own tweets. This project is ideal for learning Django's core concepts including models, views, forms, templates, and URL routing.

## Features

- 📝 Create, view, and delete tweets
- 👥 Basic user interaction flow
- 📄 Clean HTML templates (Bootstrap-ready)
- 🔐 Admin interface for managing tweets

## Technologies Used

- Python 3.11+
- Django 5.2.4
- SQLite (default development database)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-twitter.git
cd django-twitter/django_twitter
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python twittermain/manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python twittermain/manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python twittermain/manage.py runserver
```

Then navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Project Structure

```
django_twitter/
├── twittermain/
│   ├── twittermain/        # Project settings
│   └── x/                  # Core app (tweets)
├── requirements.txt
└── .git/
```

## App Details

### Tweet Model
Supports basic tweet fields with add/delete capability.

### Templates
Located in `x/templates/`:
- `index.html`: Home page
- `tweet_list.html`: Tweet feed
- `tweet_form.html`: Create/edit tweet
- `tweet_delete.html`: Confirm deletion

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

## License

[MIT](LICENSE)

---

Built for educational purposes and Django experimentation.

-> Author
[Sameer Harapanahalli] – [sameerhrv@gmail.com]  
GitHub: [SameerHRV](https://github.com/SameerHRV)
