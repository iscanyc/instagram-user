class User:
    def __init__(self, userdata):
        self.name = userdata["full_name"]
        self.username = userdata["username"]
        self.biography = userdata["biography"]
        self.url = userdata["external_url"]
        self.followers = userdata["edge_followed_by"]["count"]
        self.followed = userdata["edge_follow"]["count"]
        self.id = userdata["id"]
        self.private = userdata["is_private"]
        self.verified = userdata["is_verified"]
        self.profile_photo = userdata["profile_pic_url_hd"]
