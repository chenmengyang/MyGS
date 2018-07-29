# Notes

## Heroku config and auto-deploy tips 
* use pipenv to install packages
* make sure Pipfile and requirements.txt exist in the root dir, for letting heroku know its a Python project
* create heroku app using UI, user heroku CLI commands to connect git to heroku git (heroku git:remote)
* Procfile need to be under root dir, for letting heroku know how to serve WEB project
* read heroku documents:
  * [heroku git](https://devcenter.heroku.com/articles/git)
  * [heroku python + django](https://devcenter.heroku.com/categories/python-support)


