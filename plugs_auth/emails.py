"""
Email Template Definition
"""

from urllib.parse import urlencode

from .settings import plugs_auth_settings as settings

from plugs_mail.mail import PlugsMail


class ActivateAccount(PlugsMail):
    """
    Email sent to user after registration with link to activate his account
    """
    template = 'ACTIVATE_ACCOUNT'
    context = ('User', )
    description = 'Email sent to user after registration with link to activate his account'
    subject = 'Ativa a tua conta'

    def get_extra_context(self):
        user = self.context_data.get('user')
        params = '?' + urlencode({
            'token': user.token
        })
        print('line 28', settings)
        activate_uri = settings['SITE_ACTIVATE_VIEW'] + params
        return {'activate_uri': activate_uri}


class ResetPassword(PlugsMail):
    """
    Email sent to user with reset password link
    """
    template = 'RESET_PASSWORD'
    context = ('User', )
    description = 'Email sent to user with reset password link'
    subject = 'Perdeste a tua password?'

    def get_extra_context(self):
        """
        Adds reset_password_uri as extra context
        """
        user = self.context_data.get('user')

        params = '?' + urlencode({
            'email': user.email,
            'token': user.token
        })

        reset_password_uri = settings['SITE_RESET_VIEW'] + params
        return {'reset_password_uri': reset_password_uri}


class AccountActivated(PlugsMail):
    """
    Email sent to user after succesful account activation
    """
    template = 'ACCOUNT_ACTIVATED'
    context = ('User', )
    description = 'Email sent to user after succesful account activation'
    subject = 'Conta ativada com sucesso'
