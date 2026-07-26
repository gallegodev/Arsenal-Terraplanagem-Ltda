from django.contrib.messages import get_messages
from django.core import mail
from django.core.mail.backends.base import BaseEmailBackend
from django.test import TestCase, override_settings
from django.urls import reverse


class FailingEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        raise RuntimeError('SMTP unavailable')


class ContactEmailTests(TestCase):
    def post_contact_form(self, email='cliente@example.com'):
        return self.client.post(reverse('contact'), {
            'name': 'Cliente Teste',
            'phone': '11999999999',
            'email': email,
            'service': 'Terraplanagem',
            'message': 'Preciso preparar um terreno para obra.',
        })

    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        DEFAULT_FROM_EMAIL='website@arsenalterraplanagem.local',
        CONTACT_EMAIL_RECIPIENTS=['arsenalterra@gmail.com'],
    )
    def test_contact_form_sends_quote_request_to_company_email(self):
        response = self.post_contact_form()

        self.assertRedirects(response, reverse('contact'))
        self.assertEqual(len(mail.outbox), 2)

        message = mail.outbox[0]
        self.assertEqual(message.to, ['arsenalterra@gmail.com'])
        self.assertEqual(message.from_email, 'website@arsenalterraplanagem.local')
        self.assertEqual(message.reply_to, ['cliente@example.com'])
        self.assertEqual(
            message.subject,
            'Nova solicitação de orçamento - Arsenal Terraplanagem',
        )
        self.assertIn('Nome: Cliente Teste', message.body)
        self.assertIn('Telefone: 11999999999', message.body)
        self.assertIn('Serviço desejado: Terraplanagem', message.body)

        auto_reply = mail.outbox[1]
        self.assertEqual(auto_reply.to, ['cliente@example.com'])
        self.assertEqual(auto_reply.from_email, 'website@arsenalterraplanagem.local')
        self.assertEqual(
            auto_reply.subject,
            'Recebemos sua mensagem - Arsenal Terraplanagem',
        )
        self.assertIn('Olá,', auto_reply.body)
        self.assertIn('Muito obrigado pelo seu e-mail!', auto_reply.body)
        self.assertIn('Suzana Gallego', auto_reply.body)

    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        CONTACT_EMAIL_RECIPIENTS=['arsenalterra@gmail.com'],
    )
    def test_contact_form_skips_auto_reply_when_customer_email_is_empty(self):
        self.post_contact_form(email='')

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].reply_to, [])
        self.assertIn('E-mail: Não informado', mail.outbox[0].body)

    @override_settings(
        EMAIL_BACKEND='home.tests.FailingEmailBackend',
        CONTACT_EMAIL_RECIPIENTS=['arsenalterra@gmail.com'],
    )
    def test_contact_form_shows_error_message_when_email_delivery_fails(self):
        with self.assertLogs('home.views', level='ERROR'):
            response = self.post_contact_form()

        self.assertRedirects(response, reverse('contact'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertIn('Não foi possível enviar', str(messages[0]))
