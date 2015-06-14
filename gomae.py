import settings
from requests_oauthlib import OAuth1Session

tweet_url = settings.api_root + 'statuses/update.json'
twitter = OAuth1Session(
    settings.customer_key,
    settings.customer_secret,
    settings.access_token,
    settings.access_token_secret
)

def tweet(text):
    params = {'status': text}
    return twitter.post(tweet_url, params).json()
