from django.test import TestCase
from testapp.models import HashTest

import hashlib

class TestHash(TestCase):
    def test_decode(self):

        obj = b"12345"
        
        hash = hashlib.sha1(obj).hexdigest()
        h = HashTest.objects.create(hash_field=hash, i=1)

        self.assertEqual(hash, h.hash_field)
