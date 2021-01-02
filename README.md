# Pulse

[![Build Status](https://travis-ci.com/ctrl-alt-delete-3308/pulse.svg?branch=master)](https://travis-ci.com/ctrl-alt-delete-3308/pulse)

Providing unified keyword search across major social media platforms,
*Pulse* empowers users to understand the Internet's opinion. Built
on [Django](https://www.djangoproject.com/), continually deployed on
[Heroku](https://www.heroku.com).

Visit Pulse [here](https://csci-3308-pulse.herokuapp.com/).

## What Platforms are Supported?

We currently support search on the following social media platforms:

* Twitter
* Reddit
* YouTube

## Contributing

Have an issue, feature idea or code to add? Great! There are no
hard-spelled guidelines here. Just submit a pull request to the master
branch and we'll get the conversation going.

Django makes it pretty easy to get started with a local development server.
Dependencies can be installed using [Pipenv](https://pipenv.readthedocs.io/en/latest/):

```bash
# Install dependencies and setup virtualenv if it doesn't exist
pipenv install --python=3
# Run server in debug mode
pipenv run python3 manage.py runserver
# Run unit tests
pipenv run python3 manage.py test
```

A lot of Pulse internal settings rely on environment variables. For instance,
the following environment variables are required to be set in order to use
the Twitter, YouTube and Reddit APIs on a local development server:

```bash
PULSE_TWITTER_ACCESS_TOKEN='Twitter Access Token'
PULSE_TWITTER_ACCESS_TOKEN_SECRET='Twitter Access Token Secret'
PULSE_TWITTER_CONSUMER_KEY='Twitter Consumer Key'
PULSE_TWITTER_CONSUMER_SECRET='Twitter Consumer Key Secret'
PULSE_YOUTUBE_API_KEY='YouTube Data API Key'
PULSE_REDDIT_USER_AGENT='Reddit API User Agent String'
PULSE_REDDIT_CLIENTID='Reddit API Client ID'
PULSE_REDDIT_SECRET='Reddit API Client Secret'
```

Pipenv can make this process easy through its environment variable loading
feature (see the Pipenv docs on this topic [here](https://pipenv.readthedocs.io/en/latest/advanced/#automatic-loading-of-env)):

```bash
# Add Twitter Access Token to .env file in project root
echo 'PULSE_TWITTER_ACCESS_TOKEN=twitter access token' >> .env
# Pipenv automatically loads it from .env on 'pipenv run'
pipenv run python3 manage.py runserver
```

More information on obtaining API credentials for Twitter, Reddit and YouTube
can be found at:

* [Twitter API](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens)
* [Reddit API](https://github.com/reddit-archive/reddit/wiki/OAuth2)
* [YouTube API](https://developers.google.com/youtube/registering_an_application)

## Directory Structure

As Pulse was created within the [Django](djangoproject.com) framework, it follows
the typical [Django directory structure](https://www.revsys.com/tidbits/recommended-django-project-layout/).
Project-wide settings are located within the `pulse_project` directory. Supplemental
apps for the project are located within the `users` and `pulse_search` directories.
These apps modify the overarching Pulse project. Within the `users` directory are
files pertaining to the creation, modification, or display of users including login
support, account page views, etc are located. Within the `pulse_search` directory
files pertaining to all other functionality, including our search features, are located.

## License

This project is licensed under the MIT License. Please see the included
`LICENSE.md` file in this repository.

## Contact

Feel free to reach out to one of the creators of Pulse, Rhett, at the following:
rhha1623@colorado.edu
