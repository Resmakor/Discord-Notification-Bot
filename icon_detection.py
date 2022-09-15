import urllib.request
import re

def link(nickname):
    html = urllib.request.urlopen("https://www.twitch.tv/" + str(nickname))
    icon_ids = re.findall(r"jtv_user_pictures/(\S{1,})-profile_image-300x300.png", html.read().decode())
    if len(icon_ids) > 0:
        icon = icon_ids[0]
        return str("https://static-cdn.jtvnw.net/jtv_user_pictures/" + str(icon) + '-profile_image-300x300.png')
    else:
        print("Can't find avatar!")
        return