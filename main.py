import requests

from User import User

username = input("What is your instagram username?\n")
request = requests.get("https://www.instagram.com/" + username + "/?__a=1")
if request.ok:
    data = request.json()
    userData = data["graphql"]["user"]
    user = User(userData)
    ## user returned as Object
    print(
        "Name: {} (ID: {})\nUsername: {}\nBiography: {}\nUrl: {}\n{} followers | {} followed\nPrivate: {}\nVerified: {}".format(
            user.name, user.id, user.username,
            user.biography, user.url,
            user.followers,
            user.followed, user.private, user.verified))
else:
    print("I can't found this user: {}".format(username))
