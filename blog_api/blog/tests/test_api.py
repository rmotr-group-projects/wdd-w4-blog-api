import json
from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Author
from .fixtures import *


class AuthorTestCase(APITestCase):

    def setUp(self):
        super(AuthorTestCase, self).setUp()
        self.author = AuthorFactory(name='Author 1', email='author1@email.com')
        self.author_2 = AuthorFactory(name='Author 2', email='author2@email.com')

    def test_list(self):
        """Should return a list of all authors"""
        expected = {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'url': 'http://testserver/api/authors/1',
                    'email': 'author1@email.com',
                    'name': 'Author 1',
                    'nationality': 'Argentina'
                },
                {
                    'url': 'http://testserver/api/authors/2',
                    'email': 'author2@email.com',
                    'name': 'Author 2',
                    'nationality': 'Argentina'
                }
            ]
        }
        response = self.client.get('/api/authors')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_detail(self):
        """Should return the detail of given author"""
        expected = {
            'url': 'http://testserver/api/authors/1',
            'email': 'author1@email.com',
            'name': 'Author 1',
            'nationality': 'Argentina'
        }
        response = self.client.get('/api/authors/{}'.format(self.author.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_detail_not_found_id(self):
        """Should return 404 when author when given id does not exist"""
        response = self.client.get('/api/authors/{}'.format('foobar'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create(self):
        """Should create a new author when given data is valid"""
        self.assertEqual(Author.objects.count(), 2)
        payload = {
            'name': 'Author 3',
            'email': 'author3@email.com',
            'nationality': 'de'
        }
        response = self.client.post('/api/authors', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 3)
        author = Author.objects.get(name='Author 3')
        self.assertEqual(author.email, 'author3@email.com')
        self.assertEqual(author.nationality, 'de')

    def test_create_empty_payload(self):
        """Should return 400 bad request when missing required fields in payload"""
        self.assertEqual(Author.objects.count(), 2)
        payload = {}
        expected = {
            'email': ['This field is required.'],
            'name': ['This field is required.'],
            'nationality': ['This field is required.']
        }
        response = self.client.post('/api/authors', payload)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), expected)

    def test_full_update(self):
        """Should full update an author when given data is valid"""
        payload = {
            'name': 'New Author 1 name',
            'email': 'author3@newemail.com',
            'nationality': 'fr'
        }
        response = self.client.put(
            '/api/authors/{}'.format(self.author.id), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(author.name, 'New Author 1 name')
        self.assertEqual(author.email, 'author3@newemail.com')
        self.assertEqual(author.nationality, 'fr')

    def test_partial_update(self):
        """Should partial update an author when given data is valid"""
        payload = {
            'name': 'New Author 1 name'
        }
        response = self.client.patch(
            '/api/authors/{}'.format(self.author.id), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(author.name, 'New Author 1 name')

    def test_delete(self):
        """Should delete author when given id is valid"""
        self.assertEqual(Author.objects.count(), 2)
        response = self.client.delete('/api/authors/{}'.format(self.author.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 1)
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(name='Author 1')

    def test_list_search(self):
        """Should filter authors by name when search param is given"""
        expected = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'email': 'author1@email.com',
                    'name': 'Author 1',
                    'nationality': 'Argentina',
                    'url': 'http://testserver/api/authors/1'
                }
            ]
        }
        params = {'search': 'Author 1'}
        response = self.client.get('/api/authors', params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_list_ordering(self):
        """Should order authors by id when ordering='id' param is given"""
        expected = {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'url': 'http://testserver/api/authors/1',
                    'email': 'author1@email.com',
                    'name': 'Author 1',
                    'nationality': 'Argentina'
                },
                {
                    'url': 'http://testserver/api/authors/2',
                    'email': 'author2@email.com',
                    'name': 'Author 2',
                    'nationality': 'Argentina'
                }
            ]
        }
        params = {'ordering': 'id'}
        response = self.client.get('/api/authors', params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_list_ordering_reverse(self):
        """Should reverse order authors by id when ordering='-id' param is given"""
        expected = {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'url': 'http://testserver/api/authors/2',
                    'email': 'author2@email.com',
                    'name': 'Author 2',
                    'nationality': 'Argentina'
                },
                {
                    'url': 'http://testserver/api/authors/1',
                    'email': 'author1@email.com',
                    'name': 'Author 1',
                    'nationality': 'Argentina'
                }
            ]
        }
        params = {'ordering': '-id'}
        response = self.client.get('/api/authors', params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)


class EntryTestCase(APITestCase):

    def setUp(self):
        super(EntryTestCase, self).setUp()
        self.blog = BlogFactory()
        self.author = AuthorFactory(name='Author 1')

        self.entry = EntryFactory(
            blog=self.blog, scoring=2.04, number_comments='10')
        self.entry.authors.add(self.author)
        self.entry.pub_date = date(2016, 1, 15)
        self.entry.save()

        self.entry_2 = EntryFactory(
            blog=self.blog, scoring=4.25, number_comments='20')
        self.entry_2.pub_date = date(2016, 1, 15)
        self.entry_2.save()

    def test_list(self):
        """Should return a list of all entries"""
        expected = {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'authors': [
                        'http://testserver/api/authors/1'
                    ],
                    'blog': 'http://testserver/api/blogs/1',
                    'body_text': 'Some body text',
                    'headline': 'Some headline',
                    'mod_date': str(date.today()),
                    'number_comments': 10,
                    'pub_date': '2016-01-15',
                    'scoring': '2.04',
                    'url': 'http://testserver/api/entries/1'
                },
                {
                    'authors': [],
                    'blog': 'http://testserver/api/blogs/1',
                    'body_text': 'Some body text',
                    'headline': 'Some headline',
                    'mod_date': str(date.today()),
                    'number_comments': 20,
                    'pub_date': '2016-01-15',
                    'scoring': '4.25',
                    'url': 'http://testserver/api/entries/2'
                }
            ]
        }
        response = self.client.get('/api/entries')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_detail(self):
        """Should return the detail of given entry"""
        expected = {
            'authors': [
                'http://testserver/api/authors/1'
            ],
            'blog': 'http://testserver/api/blogs/1',
            'body_text': 'Some body text',
            'headline': 'Some headline',
            'mod_date': str(date.today()),
            'number_comments': 10,
            'pub_date': '2016-01-15',
            'scoring': '2.04',
            'url': 'http://testserver/api/entries/1'
        }
        response = self.client.get('/api/entries/{}'.format(self.entry.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_create(self):
        """Should create a new entry when given data is valid"""
        self.assertEqual(Entry.objects.count(), 2)
        payload = {
            'blog': 'http://testserver/api/blogs/1',
            'authors': ['http://testserver/api/authors/1'],
            'headline': 'New entry',
            'body_text': 'Some body text',
            'number_comments': 15,
            'scoring': 4.25
        }
        response = self.client.post('/api/entries', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Entry.objects.count(), 3)
        entry = Entry.objects.get(headline='New entry')
        self.assertEqual(entry.blog, self.blog)
        self.assertEqual(entry.authors.count(), 1)
        self.assertEqual(entry.body_text, 'Some body text')
        self.assertEqual(entry.number_comments, 15)
        self.assertEqual(entry.scoring, 4.25)

    def test_full_update(self):
        """Should full update an entry when given data is valid"""
        payload = {
            'blog': 'http://testserver/api/blogs/1',
            'authors': ['http://testserver/api/authors/1'],
            'headline': 'New headline',
            'body_text': 'Some body text',
            'number_comments': 15,
            'scoring': 4.25
        }
        response = self.client.put(
            '/api/entries/{}'.format(self.entry.id), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entry = Entry.objects.get(id=self.entry.id)
        self.assertEqual(entry.headline, 'New headline')

    def test_partial_update(self):
        """Should partial update an entry when given data is valid"""
        payload = {
            'headline': 'New headline',
        }
        response = self.client.patch(
            '/api/entries/{}'.format(self.entry.id), payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        entry = Entry.objects.get(id=self.entry.id)
        self.assertEqual(entry.headline, 'New headline')

    def test_delete(self):
        """Should delete author when given id is valid"""
        self.assertEqual(Entry.objects.count(), 2)
        response = self.client.delete('/api/entries/{}'.format(self.entry.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Entry.objects.count(), 1)
        with self.assertRaises(Entry.DoesNotExist):
            Entry.objects.get(id=self.entry.id)
