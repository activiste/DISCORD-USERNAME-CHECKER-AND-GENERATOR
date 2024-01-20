import requests
import json
import uuid

def gencookie():
    return str(uuid.uuid4())

def readusers(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def readproxies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"
userpath = "users.txt"
validpath = "valid.txt"
proxypath = "proxies.txt"

proxies = readproxies(proxypath)

reqheaders = {
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wKChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEyMS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyMS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjYwMTAxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "X-Fingerprint": "1198031150283751475.sPxZAtEn6vEJHJ_Bvd13C8AKxpA",
    "X-Discord-Locale": "fr",
    "X-Discord-Timezone": "Europe/Paris",
    "X-Debug-Options": "bugReporterEnabled",
    "Origin": "https://discord.com",
    "Referer": "https://discord.com/register",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "Content-Type": "application/json",
}

usernames = readusers(userpath)

for username, current_proxy in zip(usernames, proxies):
    current_cookie = gencookie()

    body = {
        "username": username,
    }
    body_json = json.dumps(body)

    headers = reqheaders.copy()
    headers["Cookie"] = f"__dcfduid={current_cookie}"

    try:
        response = requests.post(url, headers=headers, data=body_json, proxies={"https": current_proxy})
        print(f"{username} | Proxy: {current_proxy} | {response.text}")

        if "taken" in response.text and "false" in response.text:
            with open(validpath, 'a') as valid_file:
                valid_file.write(f"{username}\n")

    except requests.RequestException as e:
        print(f"Error for {username} using proxy {current_proxy}: {str(e)}")
