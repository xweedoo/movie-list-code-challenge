#!/usr/bin/env python

import unittest, os, sys, json, requests

def compare(dict1, dict2):
    for k, v in dict1.items():
        if dict2.has_key('title') and k == dict2['title']:
            for k2, v2 in v.items():
                if v2 != dict2[k2]:
                    return False
        else:
            return False
    return True

class TestService(unittest.TestCase):
    def setUp(self):
    	pass

    def test_get_all(self):
        r = requests.get('http://localhost:8080/movie')
        self.assertEqual(r.status_code, 200)
        self.assertNotEqual(len(r.json()), 0)
        print r.json()

    def test_get_list(self):
        r = requests.get('http://localhost:8080/movie/search?q=rambo')
        self.assertEqual(r.status_code, 200)
        self.assertNotEqual(len(r.json()), 0)
        print r.json()

    def test_get(self):
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Accept-Charset": "utf-8"}
        url = "http://localhost:8080/movie"
        for num in range(1,2):
            title = "Title_" + str(num)
            company ="Company_" + str(num)
            date = "10/10/200" + str(num)
            payload = {title: {"Release Date": date,
                               "Production Company":company}}

            # add (post)
            temp_url = url + "/" + title
            r = requests.post(temp_url,
                             data=json.dumps(payload),
                             headers=headers)

            # test get
            r = requests.get(temp_url)
            self.assertEqual(r.status_code, 200)
            self.assertNotEqual(len(r.json()), 0)
            self.assertTrue(compare(payload,r.json()))

            # cleanup (delete)
            r = requests.delete(temp_url)

    def test_delete(self):
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Accept-Charset": "utf-8"}
        url = "http://localhost:8080/movie"

        for num in range(1,2):
            title = "Title_" + str(num)
            company ="Company_" + str(num)
            date = "10/10/200" + str(num)
            payload = {title: {"Release Date": date,
                               "Production Company":company}}

            # add (post)
            temp_url = url + "/" + title
            r = requests.post(temp_url,
                             data=json.dumps(payload),
                             headers=headers)

            # now delete (delete)
            r = requests.delete(temp_url)
            self.assertEqual(r.status_code, 200)
            self.assertNotEqual(len(r.json()), 0)
            self.assertTrue((r.json())['success'])
            r = requests.get(temp_url)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(len(r.json()), 0)

    def test_post(self):
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Accept-Charset": "utf-8"}
        url = "http://localhost:8080/movie"

        for num in range(1,2):
            title = "Title_" + str(num)
            company ="Company_" + str(num)
            date = "10/10/200" + str(num)
            payload = {title: {"Release Date": date,
                               "Production Company":company}}

            # test add (post)
            temp_url = url + "/" + title
            r = requests.post(temp_url,
                             data=json.dumps(payload),
                             headers=headers)
            self.assertEqual(r.status_code, 200)
            self.assertNotEqual(len(r.json()), 0)
            self.assertTrue((r.json())['success'])
            r = requests.get(temp_url)
            self.assertEqual(r.status_code, 200)
            self.assertNotEqual(len(r.json()), 0)
            self.assertTrue(compare(payload,r.json()))

            # cleanup e (delete)
            r = requests.delete(temp_url)

    def test_put(self):
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Accept-Charset": "utf-8"}
        url = "http://localhost:8080/movie"

        for num in range(1,2):
            title = "Title_" + str(num)
            company ="Company_" + str(num)
            date = "10/10/200" + str(num)
            payload = {title: {"Release Date": date,
                               "Production Company":company}}

            # add (post)
            temp_url = url + "/" + title
            r = requests.post(temp_url,
                             data=json.dumps(payload),
                             headers=headers)
            # test put
            company ="Company_" + str(num) + str(num)
            date = "10/10/200" + str(num) + str(num)
            payload = {title: {"Release Date": date,
                               "Production Company":company}}
            r = requests.put(temp_url,
                             data=json.dumps(payload),
                             headers=headers)
            self.assertEqual(r.status_code, 200)
            self.assertNotEqual(len(r.json()), 0)
            self.assertTrue((r.json())['success'])
            r = requests.get(temp_url)
            self.assertEqual(r.status_code, 200)
            self.assertNotEqual(len(r.json()), 0)
            self.assertTrue(compare(payload, r.json()))

            # cleanup e (delete)
            r = requests.delete(temp_url)

if __name__ == '__main__':
    unittest.main()
