canary_tokens = {
    "api_key": "sk-CANARY-abc123xyz",
    "github_token": "ghp-CANARY-tok111",
    "password": "P@ss-CANARY-9921",
}
def check_canary(user_input):
    for name, token in canary_tokens.items():
        if token in user_input:
            return name
    return None