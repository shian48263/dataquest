## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
res = requests.get('https://oauth.reddit.com/r/python/top', headers=headers, params={'t': 'day'})
python_top = res.json()
print(python_top)

## 3. Getting the most upvoted article ##

python_top_articles = python_top['data']['children']
ups = 0
most_upvoted = ''
for article in python_top_articles:
    if article['data']['ups'] > ups:
        ups = article['data']['ups']
        most_upvoted = article['data']['id']
print(most_upvoted)

## 4. Getting article comments ##

res = requests.get('https://oauth.reddit.com/r/python/comments/4b7w9u', headers=headers)
comments = res.json()
print(comments)

## 5. Getting the most upvoted comment ##

comments_list = comments[1]['data']['children']
ups = 0
most_upvoted_comment = ''
for comment in comments_list:
    if comment['data']['ups'] > ups:
        ups = comment['data']['ups']
        most_upvoted_comment = comment['data']['id']
print(most_upvoted_comment)

## 6. Upvoting a comment ##

req={'dir': 1, 'id': 'd16y4ry'}
res = requests.post('https://oauth.reddit.com/api/vote', json=req, headers=headers)
status = res.status_code
print(status)