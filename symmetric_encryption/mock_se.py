from crypto.primitives import *

class SymmetricEncryption():
    """
    This class simulates a symmetric encryption scheme that is deterministic.
    """
    def __init__(self, key_len):
        """
        :param key_len: Key length in bytes.
        """
        self.key_len = key_len
        self.messages = {}
        self.ciphers = {}

    def encrypt(self, key, message):
        """
        This is a simulated encryption function. Simply use a key and message
        of any lenght.

        :param key: Key to use for simulated encryption, so this must be of
        length
                    ``self.key_len``.
        :param message: Message to be encrypted.
        :return: The cipher text for the message or ``None`` if the length
                 parameters are not met.
        """
        if len(key) is not self.key_len:
            raise ValueError("Invalid key length, key length was: " + \
                    str(len(key)) + " should be: " + str(self.key_len) + ".")

        if not (key, message) in self.ciphers:
            cipher = self._new_element(key, self.messages, len(message))
            self.ciphers[(key, message)] = cipher
            self.messages[(key, cipher)] = message

        return self.ciphers[(key, message)]

    def decrypt(self, key, cipher):
        """
        This is a simulated decryption function. Use of the correct key and
        cipher text will result in correct decryption. The cipher and key must
        have correct lengths.

        :param key: Key to use for simulated decryption, this must be of length,
                    ``self.key_len``.
        :param cipher: Cipher text to be decrypted.
        :return: The correct message for the cipher text, cipher, or
        ``None`` if parameters are not met.
        """
        if len(key) is not self.key_len:
            raise ValueError("Invalid key length, key length was: " + \
                    str(len(key)) + " should be: " + str(self.key_len) + ".")

        if not (key, cipher) in self.messages:
            message = self._new_element(key, self.ciphers, len(cipher))
            self.messages[(key, cipher)] = message
            self.ciphers[(key, message)] = cipher

        return self.messages[(key, cipher)]

    def _new_element(self, key, l, s_len):
        """
        Returns an element that has not yet been picked. We need this function
        to ensure we don't see any duplicates.

        :param key: Key to index into in list.
        :param l: List of two tuples to generate a new element in.
        :return: An element that is not yet in the list with the given
                 key.
        """
        e = random_string(s_len)
        while (key, e) in l:
            e = random_string(s_len)

        return e
