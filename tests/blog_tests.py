import os
import unittest
import tempfile
from src.blog import  *

class BlogTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.db_fn = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ self.db_fn
        app.config['TESTING'] = True
        self.app = app.test_client()
        init_db()

    def test_login(self):
        print(self.app.get('login'))

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_fn)

if __name__ == '__main__':
    unittest.main()