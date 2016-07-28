# Django hash field

Hash field for django stored in binary but converted to/from hex notation.

# Installation

```
pip install django-hash-field
```

# Usage

See [the test project](testproject/testapp).
Declare a hash field on your model:

```{py}
class HashTest(models.Model):
    hash_field = HashField()
```

Populate field with hex notation:

```{py}
hash = hashlib.sha1(b"12345").hexdigest()
h = HashTest.objects.create(hash_field=hash)
```

Although the field is stored in a binary db field, you can read/write it in hex notation:

```{py}
assert h.hash == "8cb2237d0679ca88db6464eac60da96345513964"
```
