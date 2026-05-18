from django.apps import AppConfig


class AccountsConfig(AppConfig):
<<<<<<< HEAD
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"

    def ready(self):
        import apps.accounts.signals
=======
    name = "apps.accounts"
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
