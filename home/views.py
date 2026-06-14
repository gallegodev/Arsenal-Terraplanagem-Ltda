from django.contrib import messages
from django.shortcuts import redirect, render

SERVICES = [
    {
        'title': 'Terraplanagem',
        'description': (
            'Preparacao, nivelamento e conformacao de terrenos para obras '
            'residenciais, comerciais e industriais.'
        ),
        'icon': 'fa-mountain-sun',
    },
    {
        'title': 'Escavacao e aterro',
        'description': (
            'Movimentacao de solo, cortes, aterros e compactacao com foco em '
            'base estavel e execucao segura.'
        ),
        'icon': 'fa-person-digging',
    },
    {
        'title': 'Drenagem e acesso',
        'description': (
            'Abertura de acessos, preparacao de vias internas e solucoes de '
            'escoamento para reduzir riscos no canteiro.'
        ),
        'icon': 'fa-road',
    },
    {
        'title': 'Limpeza de terreno',
        'description': (
            'Remocao de vegetacao, entulho e materiais soltos antes da fase '
            'principal da obra.'
        ),
        'icon': 'fa-truck-ramp-box',
    },
    {
        'title': 'Locacao de caminhoes',
        'description': (
            'Aluguel de caminhoes para transporte de terra, entulho, pedra, '
            'areia e apoio logistico em obras e terraplanagem.'
        ),
        'icon': 'fa-truck',
    },
    {
        'title': 'Locacao de maquinas pesadas',
        'description': (
            'Disponibilidade de equipamentos para obra, incluindo maquinas '
            '180, 360 e outros equipamentos conforme a necessidade do terreno '
            'e do servico.'
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
        messages.success(
            request,
            'Obrigado. Recebemos sua solicitacao de orcamento e entraremos em contato em breve.',
        )
        return redirect('contact')

    return render(request, 'home/contact.html')
