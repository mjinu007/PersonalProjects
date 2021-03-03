import praw
import re
import pandas as pd

all_tickers = {}
hot_tickers = {}

reddit = praw.Reddit(client_id = 'sFKZo_BWPrM3AA',
                     client_secret = '36VxrGBqxxBmaFmiDWCJkTEY9FNHJA',
                     user_agent = 'murdochcrab',
                     username = 'murdochcrab',
                     password = 'Trillion@321'

)

with open('nasdaqtraded.txt') as f:
    lines  = f.readlines()

companies = lines[1:]
for line in companies:
    ticker = line[2:line.find("|",2)]
    all_tickers[ticker] = 1

count = 0
regex_pattern = r'\b([A-Z]+)\b'
comment_list = []   
subreddit = reddit.subreddit('wallstreetbets')
hot_stock = subreddit.hot(limit = 1)

for submission in hot_stock:
    submission.comments.replace_more(limit= 0 )
    submission.comment_sort = "new" # to get only n ew comments
    print(submission.title, submission.ups, submission.downs)
    for comment in subreddit.stream.comments(): #live stream of comments
        comment_list.append(comment.body)
        if len(comment_list) > 100:
            print(f"Length of list is : {len(comment_list)}")
            series = pd.Series(hot_tickers).sort_values(ascending = False)
            print(series[:10], end ="", flush= True)
            hot_tickers = {}
            comment_list = []
            continue
        else:
            # print(len(comment_list))
            if len(comment_list) == 100:
                for s in comment_list:
                    for phrase in re.findall(regex_pattern,s ):
                        if phrase in all_tickers:
                            if phrase not in hot_tickers:
                                hot_tickers[phrase] = 1
                            else:
                                hot_tickers[phrase] += 1
            else:
                continue
            

            

        # for reply in comment.replies:
        #     print(reply.body)
        #     for reply2 in reply.replies:
        #         print(reply2.body)