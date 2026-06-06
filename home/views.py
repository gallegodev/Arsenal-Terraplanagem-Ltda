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
]

PROJECTS = [
    {
        'title': 'Preparacao de lote urbano',
        'location': 'Terreno residencial',
        'image': 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'title': 'Base para galpao',
        'location': 'Area comercial',
        'image': 'https://images.unsplash.com/photo-1581094288338-2314dddb7ece?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'title': 'Acesso e regularizacao',
        'location': 'Via interna de obra',
        'image': 'https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=1200&q=80',
    },
]

TESTIMONIALS = [
    {
        'quote': (
            'A equipe entregou a preparacao do terreno no prazo e manteve '
            'comunicacao clara durante toda a obra.'
        ),
        'name': 'Cliente residencial',
    },
    {
        'quote': (
            'Precisavamos de regularizacao e acesso para equipamentos pesados. '
            'O trabalho foi direto, organizado e bem executado.'
        ),
        'name': 'Gestor de obra comercial',
    },
    {
        'quote': (
            'O levantamento inicial ajudou a prever drenagem e movimentacao de '
            'solo antes do cronograma apertar.'
        ),
        'name': 'Engenheiro parceiro',
    },
]


def index(request):
    """Return the home page."""
    return render(request, 'home/index.html', {
        'services': SERVICES[:3],
        'projects': PROJECTS,
        'testimonials': TESTIMONIALS[:2],
    })


def about(request):
    """Return the about page."""
    return render(request, 'home/about.html')


def services(request):
    """Return the services page."""
    return render(request, 'home/services.html', {'services': SERVICES})


def projects(request):
    """Return the projects/gallery page."""
    return render(request, 'home/projects.html', {'projects': PROJECTS})


def testimonials(request):
    """Return the testimonials page."""
    return render(request, 'home/testimonials.html', {
        'testimonials': TESTIMONIALS,
    })


def contact(request):
    """Return the contact page and acknowledge quote requests."""
    if request.method == 'POST':
        messages.success(
            request,
            'Obrigado. Recebemos sua solicitacao de orcamento e entraremos em contato em breve.',
        )
        return redirect('contact')

    return render(request, 'home/contact.html')
