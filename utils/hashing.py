from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class Hash:

    @staticmethod
    def encrypt(raw_pass: str):
        return pwd_context.hash(raw_pass)

    @staticmethod
    def decrypt(raw_pass: str, hash_pass: str):
        return pwd_context.verify(raw_pass, hash_pass)
