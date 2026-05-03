from fastapi import Depends, HTTPException
from core.security import decode_token, oauth2_scheme


async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    return user_id
