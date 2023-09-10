from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # Test untuk view show_main, mensimulasikan request HTTP dan memeriksa respons
    def test_show_main_view(self):
        # Mengirim request ke view show_main
        response = Client().get('/main/')

        # Cek apakah respons status code adalah 200 
        self.assertEqual(response.status_code, 200)

        # Cek apakah template yang benar yang digunakan 
        self.assertTemplateUsed(response, 'main.html')

        # Cek context data yang di pass ke template
        self.assertEqual(response.context['app'], 'My Wardrobe')
        self.assertEqual(response.context['name'], 'Pak Bepe')
        self.assertEqual(response.context['class'], 'PBP A')