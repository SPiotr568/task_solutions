import urllib.request, json 
from math import radians, cos, sin, asin, sqrt


def get_data_from_URL(url):
    with urllib.request.urlopen(url) as url:
        return json.loads(url.read().decode())


def count_posts(posts, users):
    count_for_user = []
    count = 0
    counter_user = {}
    for post in posts:
        try:
            counter_user[int(post["userId"])] += 1
        except KeyError:
            counter_user[int(post["userId"])] = 1
    for user in users:
        try:
            count_for_user.append(f'{user["name"]} napisał(a) {counter_user[user["id"]]} postów')
        except KeyError:
            count_for_user.append(f'{user["name"]} napisał(a) 0 postów')
    return count_for_user


def get_not_unique(posts):
    not_unique = []
    posts_list = []
    for post in posts:
        if post["title"] in posts_list:
            not_unique.append(post["title"])
        else :
            posts_list.append(post["title"])
    return not_unique


def find_nearest_user(users):
    nearest_users = {}
    for user in users:
        lat, lng = float(user["address"]["geo"]["lat"]), float(user["address"]["geo"]["lng"])
        user_id = int(user['id'])
        nearest_user = min(users[:user_id - 1]+users[user_id:],\
                            key=lambda p: distance(lat,lng,\
                                                    float(p["address"]["geo"]["lat"]),\
                                                    float(p["address"]["geo"]["lng"])))
        nearest_users[user['name']] = nearest_user['name']
    return nearest_users


def distance(lat1, lng1, lat2, lng2):
    #zamiana na radiany
    lat1, long1, lat2, long2 = map(radians, [lat1, lng1, lat2, lng2])
    d_lon = lng2 - lng1 
    d_lat = lat2 - lat1 
    a = sin(d_lat/2)**2 + cos(lat1) * cos(lat2) * sin(d_lon/2)**2
    c = 2 * asin(sqrt(a))
    return 6371* c


if __name__ == "__main__":
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    posts = get_data_from_URL(posts_url)
    users = get_data_from_URL(users_url)

    # print(json.dumps(posts, indent=4, sort_keys=True))
    # print(json.dumps(users, indent=4, sort_keys=True))

    count_for_user = count_posts(posts=posts, users=users)
    for count in count_for_user:
        print(count)

    not_unique_titles = get_not_unique(posts)
    print("Tytuly nieunikalnych postów:")
    if len(not_unique_titles) == 0:
        print("Wszystkie tytuły są unikalne")
    else:
        for t in not_unique_titles:
             print(t)

    print("Użytkonik oraz użytkownik mieszkający najbliżej niego")
    nearest_user = find_nearest_user(users)
    print(json.dumps(nearest_user, indent=4, sort_keys=True))