SESSION_TIMEOUT = 30

def create_session(user):
    return {
        "token": "session_token",
        "timeout": SESSION_TIMEOUT
    }