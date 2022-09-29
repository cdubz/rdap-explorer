# -*- coding: utf-8 -*-
from django.core.management import call_command
from django.test import Client, TestCase

from datetime import date, datetime

from .models import Log


class ModelsTestCase(TestCase):
    def setUp(self):
        call_command("migrate", verbosity=0)

    def test_log_defaults(self):
        log = Log(query="8.8.8.8")
        log.save()
        self.assertIsInstance(log, Log)
        self.assertEqual(log.query, "8.8.8.8")
        self.assertIsInstance(log.date, datetime)
        self.assertEqual(log.date.date(), date.today())
        self.assertEqual(log.private, False)

    def test_log(self):
        log = Log(query="1.1.2.2", private=True)
        log.save()
        self.assertIsInstance(log, Log)
        self.assertEqual(log.query, "1.1.2.2")
        self.assertEqual(log.private, True)


class ViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ViewsTestCase, cls).setUpClass()
        call_command("migrate", verbosity=0)
        cls.c = Client()

    def test_root(self):
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertInHTML("<title>Query | RDAP Explorer</title>", html)

    def test_query(self):
        results_url = "/8.8.8.8/results/"
        response = self.c.post("/", {"query": "8.8.8.8"})
        self.assertRedirects(response, results_url)

        response = self.c.get(results_url)
        html = response.content.decode("utf-8")
        self.assertInHTML("<h3>Results for <strong>8.8.8.8</strong></h3>", html)

    def test_query_error_invalid_ip(self):
        response = self.c.post("/", {"query": "not an ip"})
        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf-8")
        self.assertInHTML(
            '<div class="toast toast-danger">'
            "<strong>Error:</strong>"
            "Enter a valid IPv4 or IPv6 address."
            "</div>",
            html,
        )
