import unittest
from task_solutions import *

class TestDistance(unittest.TestCase):
    def test_distance_same_location(self):
        self.assertEqual(distance(128.7,34.5,128.7,34.5), 0)
    def test_distance_the_same(self):
        self.assertEqual(distance(8.1,92.4,18.7,17.2), distance(8.1,92.4,18.7,17.2))

class TestGetData(unittest.TestCase):
    def setUp(self):
        self.posts_url = 'https://jsonplaceholder.typicode.com/posts'
    def test_posts_from_URL(self):
        self.assertIsNotNone(get_data_from_URL(self.posts_url))
    def test_users_from_URL(self):
        self.assertIsNotNone(get_data_from_URL(self.posts_url))

class TestFindeNearestUser(unittest.TestCase):
    def setUp(self):
        self.users = get_data_from_URL('https://jsonplaceholder.typicode.com/users')
    def test_nearest_user(self):
        self.assertEqual(find_nearest_user(self.users)['Leanne Graham'], 'Chelsey Dietrich')
        self.assertEqual(find_nearest_user(self.users)['Patricia Lebsack'], 'Nicholas Runolfsdottir V')
        self.assertEqual(find_nearest_user(self.users)['Glenna Reichert'], 'Clementina DuBuque')

class TestCountPosts(unittest.TestCase):
    def setUp(self):
        self.posts = get_data_from_URL('https://jsonplaceholder.typicode.com/posts')
        self.users = get_data_from_URL('https://jsonplaceholder.typicode.com/users')
    def test_count_posts(self):
        count_for_user = count_posts(self.posts, self.users)
        self.assertEqual(count_for_user[0],'Leanne Graham napisał(a) 10 postów')
        self.assertEqual(count_for_user[8],'Glenna Reichert napisał(a) 10 postów')
        self.assertEqual(count_for_user[6],'Kurtis Weissnat napisał(a) 10 postów')

class TestGetNotUnique(unittest.TestCase):
    def setUp(self):
        self.posts = get_data_from_URL('https://jsonplaceholder.typicode.com/posts')
    def test__get_not_unique(self):
        self.assertEqual(len(get_not_unique(self.posts)), 0)

if __name__ == '__main__':
    unittest.main()