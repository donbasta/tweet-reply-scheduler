# tweet-reply-scheduler

## approach

1. store the bottom-most tweet's ID
2. whenever it's time to post the new tweet, reply to the tweet with the ID above
3. update the latest ID for the next operation
