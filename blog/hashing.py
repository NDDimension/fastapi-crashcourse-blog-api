from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(self, password):
        return pwd_cxt.hash(password)

    def verify(self, password, hashed_password):
        return pwd_cxt.verify(password, hashed_password)
