from django.db import models
import binascii

class HashField(models.BinaryField):
    description = ('HashField is related to some other field in a model and'
        'stores its hashed value for better indexing performance.')

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 16
        kwargs.setdefault('db_index', True)
        kwargs.setdefault('editable', False)
        super(HashField, self).__init__(*args, **kwargs)
        
    def from_db_value(self, value, expression, connection, context):
        if value:
            return binascii.hexlify(value).decode("ascii")

    def get_prep_value(self, value):
        if value:
            return binascii.unhexlify(value)
