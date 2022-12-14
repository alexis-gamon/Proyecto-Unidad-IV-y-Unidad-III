from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='normal',
                                        email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self): 
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='normal',
                                                   email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


    def test_homepage_status_code(self):
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('vehiculos')) 
        self.assertEqual(response.status_code, 200)
 
    def test_homepage_url_name(self):
        response = self.client.get(reverse('almacen')) 
        self.assertEqual(response.status_code, 200)

    def test_homepage_does_not_contain_incorrect_html(self): 
        response = self.client.get('/')
        self.assertNotContains(response, 'ERROR.') 


    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_language_using_header(self):
       response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='fr')
       self.assertEqual(response.content, b"Bienvenue sur mon site.")

    def test_details(self):
       # Issue a GET request.
        response = self.client.get('vehiculos/2/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['vehiculos']), 5)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
        username='superadmin',
        email='superadmin@email.com',
        password='pila1234'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

#class AuthorModelTest(TestCase):
    

#    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
#        author.objects.create(first_name='Big', last_name='Bob')
#
#    def test_first_name_label(self):
#        author=author.objects.get(id=1)
#        field_label = author._meta.get_field('first_name').verbose_name
#        self.assertEquals(field_label,'first name')


#    def test_date_of_death_label(self):
#        author=author.objects.get(id=1)
#        field_label = author._meta.get_field('date_of_death').verbose_name
#        self.assertEquals(field_label,'died')
