__author__ = 'Dario Coco'

import os
import unittest
import tempfile
from src.blog import  *
from src.models.user import User

class ModelsTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.db_fn = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ self.db_fn
        app.config['TESTING'] = True
        self.app = app.test_client()
        init_db()

    def test_user(self):
        admin = User('dario', 'dario.coco@xpeppers.com')
        db.session.add(admin)
        db.session.commit()

        users = User.query.all()
        self.assertEqual(1, len(users))
        self.assertEqual(users[0], admin)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_fn)

if __name__ == '__main__':
    unittest.main()
