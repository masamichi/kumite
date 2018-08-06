import unittest
from django.test import TestCase as DjangoTest

from menu.models import Tea
from memu.forms import TeaSearchForm

class TeaManagerTest(DjangoTest):
    def setUp(self):
        Tea.objects.bulk_create([
            Tea(name="ダージリン", kind="english"),
            Tea(name="ウーロン茶", kind="chinese"),
            Tea(name="プーアル茶", kind="chinese"),
        ])
    def test_count_each_kind(self):
        result = Tea.objects.count_each_kind()
        self.assertEqual(result, dict(english=1, chinese=2
        ))

class TeaSearchFormTest(unittest.TestCase):
    def test_valid(self):
        """正常な入力をしたときにエラーにならないことを検証する"""
        params = dict(name="foo", kind=["english"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

    def test_ether1(self):
        """名称と種類どちらも入力しないとエラーになることを検証する"""
        params = dict()
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), False, form.errors.as_text())

    def test_ether2(self):
        """名称を入力すればエラーにならない"""
        params = dict(name="foo")
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

    def test_ether3(self):
        """種類を入力すればエラーにならない"""
        params = dict(kind=["english", "chinese"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())