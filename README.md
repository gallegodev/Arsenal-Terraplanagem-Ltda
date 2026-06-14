# Arsenal Terraplanagem Ltda.

Django website for Arsenal Terraplanagem Ltda., a construction and earthworks company.

## Pages

- Home
- About
- Services
- Contact / quote request

## Local Development

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

The public site is intentionally static/content-driven. The old ecommerce, cart, checkout, profile, account, and admin routes from the source project are not installed or exposed.
