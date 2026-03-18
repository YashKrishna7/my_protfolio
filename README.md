# Yash Krishna K P — Django Portfolio

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
python manage.py migrate

# 3. Start the server
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser.

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── portfolio/                  # Django app
│   ├── views.py                # All resume data lives here
│   └── urls.py
└── portfolio_project/
    ├── settings.py
    ├── urls.py
    ├── templates/
    │   └── portfolio/
    │       └── index.html      # Main template
    └── static/
        ├── css/style.css       # All styles
        └── js/main.js          # Scroll animations & nav
```

## Customisation

- **Update data**: Edit `portfolio/views.py` → `context` dict
- **Change colors**: Edit CSS variables in `static/css/style.css` (`:root` block)
- **Add LinkedIn/GitHub URLs**: Update `linkedin` and `github` fields in `views.py`
