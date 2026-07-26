# Arsenal Terraplanagem Ltda.

Django website for Arsenal Terraplanagem Ltda., a construction and earthworks company.

## Pages

- Home
- Sobre
- Servicos
- Contato / solicitacao de orcamento

## Local Development

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Production email delivery

The contact form sends quote requests to `arsenalterra@gmail.com` by default.
Local development uses Django's console email backend unless SMTP settings are
provided by the hosting environment.

Set these environment variables in production:

```bash
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=true
EMAIL_HOST_USER=your-sender@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-sender@gmail.com
CONTACT_EMAIL_RECIPIENTS=arsenalterra@gmail.com
```

For local testing, copy `.env.example` to `.env` and replace the placeholder
values. The `.env` file is ignored by git so real credentials stay out of the
repository.

For Gmail, `EMAIL_HOST_PASSWORD` should be an app password for the sender
account, not the account's normal login password.

The public site is intentionally static/content-driven. The old ecommerce, cart, checkout, profile, account, and admin routes from the source project are not installed or exposed.
