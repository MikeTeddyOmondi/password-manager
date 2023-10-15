# Bcrypt | PyPi Package

## Usage
Password Hashing

Hashing and then later checking that a password matches the previous hashed password is very simple:

```
>>> import bcrypt
>>> password = b"super secret password"
>>> # Hash a password for the first time, with a randomly-generated salt
>>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
>>> # Check that an unhashed password matches one that has previously been
>>> # hashed
>>> if bcrypt.checkpw(password, hashed):
...     print("It Matches!")
... else:
...     print("It Does not Match :(")

```

# KDF

As of 3.0.0 bcrypt now offers a kdf function which does bcrypt_pbkdf. This KDF is used in OpenSSH's newer encrypted private key format.

```

>>> import bcrypt
>>> key = bcrypt.kdf(
...     password=b'password',
...     salt=b'salt',
...     desired_key_bytes=32,
...     rounds=100)

```
# Adjustable Work Factor

One of bcrypt's features is an adjustable logarithmic work factor. To adjust the work factor merely pass the desired number of rounds to bcrypt.gensalt(rounds=12) which defaults to 12):

```
>>> import bcrypt
>>> password = b"super secret password"
>>> # Hash a password for the first time, with a certain number of rounds
>>> hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
>>> # Check that a unhashed password matches one that has previously been
>>> #   hashed
>>> if bcrypt.checkpw(password, hashed):
...     print("It Matches!")
... else:
...     print("It Does not Match :(")

```

# Adjustable Prefix

Another one of bcrypt's features is an adjustable prefix to let you define what libraries you'll remain compatible with. To adjust this, pass either 2a or 2b (the default) to bcrypt.gensalt(prefix=b"2b") as a bytes object.

As of 3.0.0 the $2y$ prefix is still supported in hashpw but deprecated.
Maximum Password Length

The bcrypt algorithm only handles passwords up to 72 characters, any characters beyond that are ignored. To work around this, a common approach is to hash a password with a cryptographic hash (such as sha256) and then base64 encode it to prevent NULL byte problems before hashing the result with bcrypt:


```
>>> password = b"an incredibly long password" * 10
>>> hashed = bcrypt.hashpw(
...     base64.b64encode(hashlib.sha256(password).digest()),
...     bcrypt.gensalt()
... )

```