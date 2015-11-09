#!/usr/bin/env python

import json

from bottle import route, run, request, response, abort

movies = {'Rambo': {'Release Date': '01/01/2000', 'Production Company': 'company1'},
          'Rambo 2': {'Release Date': '01/01/2001', 'Production Company': 'company1'},
          'Star War': {'Release Date': '01/01/2002', 'Production Company': 'company1'}}

# Retrieve all movies
@route("/movie", method='GET')
def list_movie():
    response.content_type = "application/json"
    entity = []
    for title, item in movies.items():
        data = {"title":title}
        for k, v in item.items():
            data[k] = v
        entity.append(data)
    return json.dumps(entity)

# Retrieve a list of movies
@route("/movie/search", method='GET')
def list_movie():
    try:
        q = request.query["q"]
    except Exception:
        return []
    else:
        response.content_type = "application/json"
        entity = []
        for title, item in movies.items():
            if title.lower().find(q.lower()) > -1:
                data = {"title":title}
                for k, v in item.items():
                    data[k] = v
                entity.append(data)
        return json.dumps(entity)

# Retrieve a movie
@route('/movie/<title>', method='GET')
def get_movie(title):
    response.content_type = "application/json"
    entity ={}
    if movies.has_key(title):
        entity["title"] = title
        for k, v in movies[title].items():
            entity[k] = v
    return json.dumps(entity)

# Delete a movie
@route('/movie/<title>', method='DELETE')
def del_movie(title):
    response.content_type = "application/json"
    try:
        if movies.has_key(title):
            del movies[title]
            return json.dumps({"success": True})
        else:
            return json.dumps({"success": False,
                               "error:": title + " movie does not exits"})
    except Exception:
        return json.dumps({"success": False})

# update an existing movie
@route('/movie/<title>', method='PUT')
def put_movie(title):
    response.content_type = "application/json"
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
        #return {"sucess": False, "error": "insert/update called without content"}
    payload = json.loads(data)
    if not payload.has_key(title):
        abort(400,'No title specified')
        #return {"sucess": False, "error": "insert/update called without a title"}

    try:
        #database insert/update
        for title, v1 in payload.items():
            if movies.has_key(title):
                for k2, v2 in v1.items():
                    movies[title][k2] = v2

        return json.dumps({"success": True})
    except Exception as e:
        abort(400, str(e))

# create a new movie
@route('/movie/<title>', method='POST')
def post_movie(title):
    response.content_type = "application/json"
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
        # return json.dumps({"success": False,
        #                   "error": "insert called without content"})
    payload = json.loads(data)
    if not payload.has_key(title):
        abort(400,'No title specified')
    try:
        #database insert
        for title, v1 in payload.items():
            print "title: %s ;value: %s" % (title, v1)
            if not movies.has_key(title):
                movies[title] ={}
                for k2, v2 in v1.items():
                    movies[title][k2] = v2
        return json.dumps({"success": True})
    except Exception as e:
        abort(400, str(e))

if __name__ == "__main__":
    run(host='localhost', port=8080)
