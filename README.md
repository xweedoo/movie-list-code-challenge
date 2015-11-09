# movie-list-code-challenge
## Introduction
Web sevices providing the following services:
* Return a list of Movies
* Add a movie
* Update movie details
* Delete a movie

## Setup
First get yourself setup with [Virtual Env] (http://docs.python-guide.org/en/latest/dev/virtualenvs/) so we don't break any other Python stuff you have on your machine. After you've got that installed let's setup an environment for our app:

```
$ virtualenv movie-app
New python executable in movie-app/bin/python
Installing setuptools, pip, wheel...done
```
```
$ source movie-app/bin/activate
```
The next step is to install the dependencies for the app:
```
(movie-app)$ pip install -r requirements.txt
...
Successfully installed bottle-0.12.9 nose-1.3.7 requests-2.8.1
```
And finally let’s start up a Bottle web server:
```
(movie-app)$ python movie.py
Bottle v0.12.9 server starting up (using WSGIRefServer())...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.
```
## Endpoints
Return a single Movie
```
// JSON object for a single movie with release date and production company
curl http://localhost:8080/movie/Rambo%20Two
```
Return a list of Movies
```
// list of JSON object for movie search with release dates and production companies
curl http://localhost:8080/movie/search?q=rambo
```
Delete a movie
```
curl -X DELETE http://localhost:8080/movie/Rambo%20Two
```
Add a movie
```
// list of JSON objects for movie search results
curl -i -H "Content-Type: application/json" -H "Accept: application/json; charset=UTF-8" -X POST -d "{{\"Rambo 3\":{\"Release Date\":\"01/01/2015\",\"Production Company\":\"CompanyIIII\"}} http://localhost:8080/movie/Rambo%203
```
Update movie details
```
curl -i -H "Content-Type: application/json" -H "Accept: application/json; charset=UTF-8" -X PUT -d ""{{\"Rambo 3\":{\"Release Date\":\"11/11/2015\",\"Production Company\":\"CompanyI\"}} http://localhost:8080/movie/Rambo%203
```

## Testing
```
nosetests -v tests/TestMoviesServices.py
```
