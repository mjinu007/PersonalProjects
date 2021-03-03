import praw
import re
import pandas as pd

reddit = praw.Reddit(client_id = 'sFKZo_BWPrM3AA',
                     client_secret = '36VxrGBqxxBmaFmiDWCJkTEY9FNHJA',
                     user_agent = 'murdochcrab',
                     username = 'murdochcrab',
                     password = 'Trillion@321'

)

subreddit = reddit.subreddit('wallstreetbets')
#submission = reddit.submission('wallstreetbets')

# with open('nasdaqtraded.txt') as f:
#     lines  = f.readlines()
#     companies = lines[1:]
#     print(companies[1][2:companies[1].find('|',2)])

# all_tickers = {}
# hot_tickers = {}

# for line in companies:
#     ticker = line[2:line.find("|",2)]
#     all_tickers[ticker]  = 1
    
# regex_pattern = r'\b([A-Z]+)\b'
# comment_count = []
# count = 0

# for submission in subreddit.hot(limit=10): # get top ten
#     print(submission.title)

# for submission in subreddit.rising(limit=None): # get All Rising/gilded/controversial/hot/new/top
#     print(submission.title)
#     print(submission.score)
#     print(submission.url)

hot_stock = subreddit.hot(limit = 1)
for submission in hot_stock:
    submission.comments.replace_more(limit= 0 )
    print(submission.title, submission.ups, submission.downs)
    comments = submission.comments.list()

    
# for submission in subreddit.hot(Limit = 1):
#     submission.comments.replace_more(limit= 0 )
#     print(submission.title)
#     print(len(submission.comments.list()))

# strings=[]
# print("Here")
# for submission in subreddit.hot(limit = 1):
#     print(submission.title)
#     submission.comments.replace_more(limit= 0 )
#     for comment in submission.comments: 
#         print(comment.body)
#         for reply in comment.replies:
#             print(reply.body)
#             for third_level in reply.replies:
#                 print(third_level.body)
#                 break
#         break
        
# submission.comments.replace_more(limit=0)
# comment_queue = submission.comments[:]  # Seed with top-level
# while comment_queue:
#     comment = comment_queue.pop(0)
#     print(comment.body)
#     comment_queue.extend(comment.replies)


# count = 0
# for comment in subreddit:
#     count = count+1
#     print(count)




#         strings.append(comment.body)  
#     for s in strings:
#         for phrase in re.findall(regex_pattern, s):
#             if phrase in all_tickers:
#                 if phrase not in hot_tickers:
#                     hot_tickers[phrase] = 1
#                 else:
#                     hot_tickers[phrase] += 1
# print(hot_tickers)
# series = pd.series(hot_tickers).sort_values(ascending = False)
# series[:10]
#     submission.comments.replace_more(limit = 0)
#     for comment in submission.comments.list():
#         comment_count.append(comment)
# print(len(comment_count))