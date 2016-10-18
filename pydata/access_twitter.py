# -*- coding: utf-8 -*-
import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'J4pevsxysB21KtQc8llfBxgzl'
CONSUMER_SECRET = 'LcbPbV91uB267wPh5LSXjRfrHKbPUclfG5X8BoQR8Cyvpy37lT'
OAUTH_TOKEN = '314594057-Y87fHWHUgY5WDlfoAweoySwowlIzvI4WNEKDj2uj'
OAUTH_TOKEN_SECRET = 'QXZMX3gNdTJCXIhuvRQHS389I6Jnf7mZOqTv2Gk8SNwrS'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print twitter_api
