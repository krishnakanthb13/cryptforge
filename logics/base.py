from abc import ABC, abstractmethod

class EncryptionLogic(ABC):
    """
    Abstract base class for all encryption logics.
    Any new logic must inherit from this class and implement
    the encrypt and decrypt methods.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """The unique name of the logic (e.g., 'aes', 'xor')."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """A brief description of what this logic does."""
        pass

    @abstractmethod
    def encrypt(self, data: bytes, password: str) -> bytes:
        """
        Encrypts the given data using the provided password.
        
        Args:
            data (bytes): The raw data to encrypt.
            password (str): The password to derive the key from.
            
        Returns:
            bytes: The encrypted data.
        """
        pass

    @abstractmethod
    def decrypt(self, data: bytes, password: str) -> bytes:
        """
        Decrypts the given data using the provided password.
        
        Args:
            data (bytes): The encrypted data.
            password (str): The password used for encryption.
            
        Returns:
            bytes: The decrypted data.
        """
        pass
