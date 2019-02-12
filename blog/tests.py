import datetime
from django.test import TestCase

from .models import Article

from django.urls import reverse

# Create your tests here.

def create_article(name, title, contents, url, email):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Article.objects.create(name=name, title=title, contents=contents, url=url, email=email)

class ArticleTests(TestCase):
    def test_article_model(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """

        crated_article = create_article('test_future_question','제목','내용','https://www.naver.com','jae6120@naver.com')
        self.assertEqual(1, crated_article.pk)

    def test_article_pk_same(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        crated_article = create_article('test_future_question','제목','내용','https://www.naver.com','jae6120@naver.com')
        url = reverse('blog:view', kwargs={'pk': 2})
        response = self.client.get(url)
        # print('test_future_question',crated_article.name)
        self.assertEqual(response.status_code, 404)

    def test_article_name_same(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        crated_article = create_article('test_past_question','제목','내용','https://www.naver.com','jae6120@naver.com')
        url = reverse('blog:view', kwargs={'pk': crated_article.pk})
        response = self.client.get(url)
        # print('test_past_question',crated_article.name)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, crated_article.name)

