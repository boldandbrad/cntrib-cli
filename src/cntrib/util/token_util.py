import base64

import keyring

SERVICE_NAME = "cntrib-cli"
TOKEN_KEY = "gh_token"
ENCODING = "utf-8"


def set_gh_token(token: str) -> None:
    keyring.set_password(
        SERVICE_NAME,
        TOKEN_KEY,
        base64.b64encode(bytes(token, ENCODING)).decode(ENCODING),
    )


def get_gh_token() -> str:
    return base64.b64decode(keyring.get_password(SERVICE_NAME, TOKEN_KEY)).decode(
        ENCODING
    )


def clear_gh_token() -> None:
    keyring.delete_password(SERVICE_NAME, TOKEN_KEY)
