from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Joao Paulo Canario',
            cpf='12345678901',
            email='jopacanario@gmail.com',
            phone='71-999538382'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        '''Subscription must have an auto created_at attribute'''

        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Joao Paulo Canario', str(self.obj))