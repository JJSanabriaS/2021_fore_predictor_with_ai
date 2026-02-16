import praw
reddit = praw.Reddit(client_id="riotimusjjss1976",client_secret=" ",user_agent=”my user agent” )
#To test if your instance is working use:
print(reddit.read_only) # Output: True