import praw
import re

hold_upvote = 0
buy_upvote = 0
sell_upvote = 0

reddit = praw.Reddit(client_id = 'sFKZo_BWPrM3AA',
                     client_secret = '36VxrGBqxxBmaFmiDWCJkTEY9FNHJA',
                     user_agent = 'murdochcrab',
                     username = 'murdochcrab',
                     password = 'Trillion@321'

)

subreddit = reddit.subreddit('wallstreetbets')

hot_news = subreddit.hot(limit = 1)

for submission in hot_news: 
    print(submission.title)
    submission.comments.replace_more(limit = 0) # to avoid error
    comments = submission.comments.list()
    for comment in comments:
        buy_list = re.findall(r'\bbuy', comment.body, flags = re.IGNORECASE)
        sell_list = re.findall(r'\bsell', comment.body, flags = re.IGNORECASE)
        hold_list = re.findall(r'\bhold', comment.body, flags = re.IGNORECASE)
        dont_buy_list = re.findall(r"\bdont buy", comment.body,flags = re.IGNORECASE)
        dont_sell_list = re.findall(r"\bdont sell", comment.body,flags = re.IGNORECASE)
        dont_hold_list = re.findall(r"\bdont hold", comment.body, flags = re.IGNORECASE)

        if buy_list == []:
            buy_upvote = buy_upvote
        elif dont_buy_list == []:
            buy_upvote += comment.ups
        else:
            buy_upvote = buy_upvote
        
        if sell_list == []:
            sell_upvote = sell_upvote
        elif dont_sell_list == []:
            sell_upvote += comment.ups
        else:
            sell_upvote = sell_upvote
            hold_upvote += comment.ups

        if hold_list == []:
            hold_upvote = hold_upvote
        elif dont_hold_list == []:
            hold_upvote += comment.ups
        else:
            hold_upvote = hold_upvote 
            sell_upvote += comment.ups


print(buy_upvote)
print(sell_upvote)
print(hold_upvote)
