from nose.tools import *
import unittest

from satoshi.models.key import Key


class KeyTestCase():

    PASSPHRASE = 'correct horse battery staple'
    SECRET_EXPONENT = (
        'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a'
    )
    PRIVATE_KEY = '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS'
    COMPRESSED_PRIVATE_KEY = (
        'L3p8oAcQTtuokSCRHQ7i4MhjWc9zornvpJLfmg62sYpLRJF9woSu'
    )
    PUBLIC_KEY = (
        '04'  # First byte, per the Bitcoin specification
        '78d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71'  # x
        'a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455'  # y
    )
    COMPRESSED_PUBLIC_KEY = (
        '03' # First byte, determines sign of y
        '78d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71'
    )
    ADDRESS = '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T'
    COMPRESSED_ADDRESS = '1C7zdTfnkzmr13HfA2vNm5SJYRK6nEKyq8'

    def test_passphrase(self):
        with assert_raises(AttributeError):
            _ = self.key.passphrase

    def test_secret_exponent(self):
        with assert_raises(AttributeError):
            _ = self.key.secret_exponent

    def test_private_key(self):
        with assert_raises(AttributeError):
            _ = self.key.private_key

    def test_address(self):
        assert_equal(
            self.key.address,
            self.ADDRESS,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            self.PUBLIC_KEY,
        )


class PassphraseTestCase(KeyTestCase, unittest.TestCase):
    def setUp(self):
        self.key = Key(passphrase=self.PASSPHRASE)

    def test_passphrase(self):
        assert_equal(
            self.key.passphrase,
            self.PASSPHRASE,
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            self.SECRET_EXPONENT,
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            self.PRIVATE_KEY,
        )


class PrivateKeyTestCase(KeyTestCase, unittest.TestCase):
    def setUp(self):
        self.key = Key(private_key=self.PRIVATE_KEY)

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            self.PRIVATE_KEY,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            self.PUBLIC_KEY,
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            self.SECRET_EXPONENT,
        )


class CompressedPassphraseTestCase(KeyTestCase, unittest.TestCase):
    """Initialized with a passphrase, compress public and private keys"""
    def setUp(self):
        self.key = Key(
            passphrase=self.PASSPHRASE,
            compressed=True
        )

    def test_passphrase(self):
        assert_equal(
            self.key.passphrase,
            self.PASSPHRASE,
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            self.COMPRESSED_PRIVATE_KEY
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            self.COMPRESSED_PUBLIC_KEY,
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            self.SECRET_EXPONENT,
        )

    def test_address(self):
        assert_equal(
            self.key.address,
            self.COMPRESSED_ADDRESS
        )


class CompressedPassphraseTestCase2(CompressedPassphraseTestCase):
    """This case is to cover then the resultant compressed public key is
    prefixed with '02' instead of '03'. The above test case covers the latter.
    """
    PASSPHRASE = 'weak passphrase'
    SECRET_EXPONENT = (
        '9d7682a6cbc705ed086c9c64658b42896f692e4d44202c9460908e0dcd7ad5a9'
    )
    COMPRESSED_PRIVATE_KEY = (
        'L2VoFYS8oeGAdthWrZRgiP61TD5mUWESXrBa7xa5bDzZ5hkzKWoW'
    )
    COMPRESSED_PUBLIC_KEY = (
        '02'
        '4b0b81bd7575b4207e4fa5a0913a050db07249f5004f1a1796c922221fd41e59'
    )
    COMPRESSED_ADDRESS = '1ML29MAbyvKmS12igR1eG97SjGRthgxv83'

class SecretExponentTestCase(KeyTestCase, unittest.TestCase):
    def setUp(self):
        self.key = Key(secret_exponent=self.SECRET_EXPONENT)

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            self.SECRET_EXPONENT,
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            self.PRIVATE_KEY,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            self.PUBLIC_KEY,
        )


class PublicKeyTestCase(KeyTestCase, unittest.TestCase):
    def setUp(self):
        self.key = Key(public_key=self.PUBLIC_KEY)


class AddressTestCase(KeyTestCase, unittest.TestCase):

    def setUp(self):
        self.key = Key(address=self.ADDRESS)

    def test_public_key(self):
        with assert_raises(AttributeError):
            _ = self.key.public_key