import os, re, requests

cookies = {
    "c_user": "",
    "xs": ""
}
friend_id = ""


def load_photo(input_url):
    req = requests.Session()
    offset = 0

    while True:
        url = "{}{}".format(input_url, offset)
        res = req.get(url, cookies=cookies)
        html = res.text
        match = re.findall(r"/photo.php\?fbid=([0-9]*)&amp;", html)
        if match:
            for m in match:
                f = open("{}/{}.jpg".format(friend_id, m),"wb")
                res = req.get("https://mbasic.facebook.com/photo/view_full_size/?fbid={}".format(m), cookies=cookies)
                html = res.text
                z = re.search(r"a href=\"(.*?)\"", html)
                if z:
                    url = str(z.groups()[0]).replace("&amp;", "&")
                    res = req.get(url, cookies=cookies)
                    f.write(res.content)
                    f.close()
                else:
                    break
            offset+=12
            print(offset)
        else:
            break


if __name__ == "__main__":
    if not os.path.exists(friend_id):
        os.makedirs(friend_id)

    url_photo_tag = "https://mbasic.facebook.com/{}/photoset/pb.{}.-2207520000../?owner_id={}&offset=".format(friend_id, friend_id, friend_id)
    url_photo_upload = "https://mbasic.facebook.com/{}/photoset/t.{}/?owner_id={}&offset=".format(friend_id, friend_id, friend_id)

    load_photo(url_photo_tag)
    load_photo(url_photo_upload)