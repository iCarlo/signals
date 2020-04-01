from django.apps import AppConfig


class SignalsAppConfig(AppConfig):
    name = 'signals_app'

    def ready(self):
        import signals_app.signals
