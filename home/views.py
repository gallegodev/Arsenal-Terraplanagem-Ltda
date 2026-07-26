import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

logger = logging.getLogger(__name__)

AUTO_REPLY_BODY = """Olá,

Muito obrigado pelo seu e-mail!

No momento, todos os nossos agentes estão ocupados, mas já recebemos a sua mensagem e entraremos em contato com você o mais rápido possível.

Atenciosamente,

Suzana Gallego"""

SERVICES = [
    {
        'title': 'Terraplanagem',
        'description': (
            'Preparação, nivelamento e conformação de terrenos para obras '
            'residenciais, comerciais e industriais.'
        ),
        'icon': 'fa-mountain-sun',
    },
    {
        'title': 'Escavação e aterro',
        'description': (
            'Movimentação de solo, cortes, aterros e compactação com foco em '
            'base estável e execução segura.'
        ),
        'icon': 'fa-person-digging',
    },
    {
        'title': 'Drenagem e acesso',
        'description': (
            'Abertura de acessos, preparação de vias internas e soluções de '
            'escoamento para reduzir riscos no canteiro.'
        ),
        'icon': 'fa-road',
    },
    {
        'title': 'Limpeza de terreno',
        'description': (
            'Remoção de vegetação, entulho e materiais soltos antes da fase '
            'principal da obra.'
        ),
        'icon': 'fa-truck-ramp-box',
    },
    {
        'title': 'Locação de caminhões',
        'description': (
            'Aluguel de caminhões para transporte de terra, entulho, pedra, '
            'areia e apoio logístico em obras e terraplanagem.'
        ),
        'icon': 'fa-truck',
    },
    {
        'title': 'Locação de máquinas pesadas',
        'description': (
            'Disponibilidade de equipamentos para obra conforme a necessidade '
            'do terreno e do serviço.'
        ),
        'icon': 'fa-truck-monster',
    },
]

def index(request):
    """Return the home page."""
    return render(request, 'home/index.html', {
        'services': SERVICES,
    })


def about(request):
    """Return the about page."""
    return render(request, 'home/about.html')


def services(request):
    """Return the services page."""
    return render(request, 'home/services.html', {'services': SERVICES})


def contact(request):
    """Return the contact page and acknowledge quote requests."""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        email_body = (
            'Nova solicitação de orçamento recebida pelo site.\n\n'
            f'Nome: {name}\n'
            f'Telefone: {phone}\n'
            f'E-mail: {email or "Não informado"}\n'
            f'Serviço desejado: {service}\n\n'
            'Detalhes da obra:\n'
            f'{message}\n'
        )

        reply_to = [email] if email else None
        quote_email = EmailMessage(
            subject='Nova solicitação de orçamento - Arsenal Terraplanagem',
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=settings.CONTACT_EMAIL_RECIPIENTS,
            reply_to=reply_to,
        )

        try:
            quote_email.send(fail_silently=False)
        except Exception:
            logger.exception('Failed to send contact form email.')
            messages.error(
                request,
                'Não foi possível enviar a solicitação agora. Por favor, tente novamente em instantes.',
            )
        else:
            if email:
                auto_reply = EmailMessage(
                    subject='Recebemos sua mensagem - Arsenal Terraplanagem',
                    body=AUTO_REPLY_BODY,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[email],
                )

                try:
                    auto_reply.send(fail_silently=False)
                except Exception:
                    logger.exception('Failed to send contact form auto-reply.')

            messages.success(
                request,
                'Obrigado. Recebemos sua solicitação de orçamento e entraremos em contato em breve.',
            )
        return redirect('contact')

    return render(request, 'home/contact.html')
