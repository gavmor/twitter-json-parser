# twitter-json-parser

Original by Luhang Sun, this script parses JSON as returned by Twitter 2.0 API into DataFrames.

# Example

```
~/workspace/twitter-parser>>./TwitterAPI2_0_parser.py 
Enter the directory path of your JSON files here: datafiles
Enter the directory path of your csv output file here: .     
Enter your csv output file name here: test123
```

For datafiles like this:
```json
{
    "data":
    [
{
    "id": "123",
    "created_at": "2020-02-28T21:32:27.000Z",
    "public_metrics":
    {
        "retweet_count": 0,
        "reply_count": 0,
        "like_count": 1,
        "quote_count": 0
    },
    "conversation_id": "456",
    "source": "Twitter for iPhone",
    "lang": "en",
    "reply_settings": "everyone",
    "entities":
    {
        "mentions":
        [
            {
                "start": 0,
                "end": 14,
                "username": "zzz",
                "id": "789"
            }
        ]
    },
    "in_reply_to_user_id": "123",
    "referenced_tweets":
    [
        {
            "type": "replied_to",
            "id": "456"
        }
    ],
    "text": "foo, bar baz",
    "possibly_sensitive": false,
    "author_id": "987"
},
    ],
    "includes":
    {
        "users": [...],
        "tweets": [...],
        "media": [...]
    },
    "errors":[...],
    "meta":
    {
        "newest_id": ...,
        "oldest_id": ...,
        "result_count": ...,
        "next_token": ...
    }
}
```
