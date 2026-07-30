import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, ExpiredSignatureError, JWTError
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY: str | None = os.getenv("SECRET_KEY")
ALGORITHM: str | None = os.getenv("ALGORITHM")

bearer_scheme = HTTPBearer()


class TokenManager:
    @staticmethod
    def create_token(data: dict):
        to_encode = data.copy()
        expire_date = datetime.now(timezone.utc) + timedelta(minutes=1)
        to_encode.update({"exp": int(expire_date.timestamp())})

        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def get_current_user(
            credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    ):
        access_token = credentials.credentials
        try:
            payload = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user_id = payload.get("id")
            return user_id
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token müddəti bitmişdir",
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token etibarsızdır"
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Token xəta verdi"
            )
