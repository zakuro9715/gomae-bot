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

def subtract_min_from_max(a, b):
    return max(a, b) - min(a, b)

if __name__ == '__main__':
    import time
    from datetime import datetime, timezone, timedelta
    import dateutil.parser

    local_time = datetime.now(timezone.utc)
    
    target_time = local_time + timedelta(minutes=settings.wait_minutes)
    target_time = datetime(*(target_time.timetuple()[:5]), tzinfo=timezone.utc)
    print('目標時刻 %s' % target_time.isoformat())
    
    server_time = dateutil.parser.parse(tweet(settings.pre_text)['created_at'])
    delta = server_time - local_time
    print('時刻誤差 %s' % subtract_min_from_max(server_time, local_time))

    wait_seconds = (target_time - datetime.now(timezone.utc) - delta).seconds
    print('待機時間 %s秒' % wait_seconds)
    time.sleep(wait_seconds + settings.tolerance_seconds)
    
    tweeted_time = dateutil.parser.parse(tweet(settings.text)['created_at'])
    print('tweet時刻 %s' % (tweeted_time.isoformat())) 
    print('誤差 %s' % subtract_min_from_max(tweeted_time, target_time)) 
