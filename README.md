# django-graphene-example

A Django app to explore the Graphene framework for Python

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/Jpadilla1/django-graphene-example.git
$ cd django-graphene-example

$ pip install -r requirements.txt

$ createdb django_graphene_example

$ python manage.py migrate
$ python manage.py loadtestdata posts.Post:20
$ python manage.py loadtestdata comments.Comment:30

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

## Example Query

First 2 posts with 5 comments each

```
query {
  allPosts(first: 2) {
    edges {
      node {
        id,
        title,
        author,
        comment(first: 5) {
          edges {
            node {
              text
            }
          }
        }
      }
    }
  }
}
```
