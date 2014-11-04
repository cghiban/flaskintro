from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/login', content_type='html/text')
    self.assertEqual(response.status_code, 200)

  def test_login_page_load(self):
    tester = app.test_client(self)
    response = tester.get('/login', content_type='html/text')
    self.assertTrue(b'Please login' in response.data)

  def test_login_works_on_invalid_credentials(self):
    tester = app.test_client(self)
    response = tester.post('/login', data=dict(u='x', p='y'), follow_redirects = True)
    self.assertTrue(b'Error:' in response.data)

  def test_login_works_on_post(self):
    tester = app.test_client(self)
    response = tester.post(
        '/login', 
        data=dict(u='admin', p='admin'), 
        follow_redirects = True
    )
    self.assertEqual(response.status_code, 200)

  def test_logout(self):
    tester = app.test_client(self)
    tester.post(
        '/login', 
        data=dict(u='admin', p='admin'), 
        follow_redirects = True
    )
    response = tester.get('/logout', follow_redirects=True)
    self.assertIn(b'Just logged out', response.data)

  def test_main_route_requires_login(self):
    tester = app.test_client(self)
    response = tester.get('/', follow_redirects=True)
    self.assertTrue('Please login' in response.data)

  def test_post_show_up(self):
    tester = app.test_client(self)
    resp = tester.post(
        '/login', 
        data=dict(u='admin', p='admin'), 
        follow_redirects = True
    )
    self.assertIn('Good', resp.data)
 
if __name__ == '__main__':
  unittest.main()
