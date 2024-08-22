from django.db import models

# client_zone/models.py

from wagtail.models import Page


class ClientZonePage(Page):
    template = "client_zone/client_zone_page.html"

    content_panels = Page.content_panels + [
        # Можете добавить поля для кастомизации страницы, если нужно
    ]
