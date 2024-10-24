from multiprocessing.spawn import old_main_modules
from django.urls import reverse
from django.test import TestCase
from computer_hardware_store import factories, models
from computer_hardware_store.models import Computer


class ComputerShelfTestCase(TestCase):
    def setUp(self):
        self.computer = factories.ComputerFactory()

    def test_get_computers_list(self):
        url = reverse('computers_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['computers'].count(), models.Computer.objects.count())

    def test_get_computer_detail(self):
        url = reverse('computer_detail', kwargs={'pk': self.computer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_computer(self):
        url = reverse('computer_update', kwargs={'pk': self.computer.pk})
        old_title = self.computer.title
        response = self.client.post(url, {'title': 'new_title'})
        self.computer.refresh_from_db()
        #print(response.content)
        #self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.computer.title, old_title)
        self.computer.refresh_from_db()
        print(models.Computer.objects.all())

    def test_delete_computer(self):
        url = reverse('computer_delete', kwargs={'pk': self.computer.pk})
        old_computer_count = models.Computer.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_computer_count, models.Computer.objects.count())
        print(old_computer_count, models.Computer.objects.count())

    def test_create_computer(self):
        url = reverse('computer_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        print(models.Computer.objects.count())
        print(models.Computer.objects.all())
