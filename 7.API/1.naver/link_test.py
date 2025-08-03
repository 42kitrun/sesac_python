import os
from urllib.parse import urlencode
from dotenv import load_dotenv
import os

load_dotenv()


NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")  # 네이버 앱 아이디
NAVER_REDIRECT_URI = os.getenv("NAVER_REDIRECT_URI")  # http://127.0.0.1:5000/naver/callback

def get_naver_auth_url():
    params = {
        "response_type": "code",
        "client_id": NAVER_CLIENT_ID,
        "redirect_uri": NAVER_REDIRECT_URI,
        "state": "random_state_value"  # CSRF 방지용
    }
    url = "https://nid.naver.com/oauth2.0/authorize?" + urlencode(params)
    return url

print(get_naver_auth_url())