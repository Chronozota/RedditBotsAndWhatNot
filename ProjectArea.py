import praw
import time

# This verifies authenticity of a reddit account and that we are allowed to create a bot
from praw.exceptions import RedditErrorItem, APIException

reddit = praw.Reddit(client_id="G7it5PH88exEow",
                     client_secret="a0O8wZZ25hEq0Qercjqu95BzzAXTVA",
                     user_agent="my user agent",
                     username="LotusMagician",
                     password="Magicctr1030")
# This checks to make sure that the bot can interact with the website to make posts,comments,up vote,etc.
# if reddit.validate_on_submit is always false unless you change it like I have done below
reddit.validate_on_submit = True
# printing reddit.read_only will produce a boolean value. In this case the value will read false. It will read true if
# I didn't have line 8 and 9
print(reddit.read_only)
print("")
# A subreddit or a list of subreddits that the chosen post will be posted to
subreddits = ["bottestgang"]
pos = 0


def body_post():
    global subreddits
    global pos
    # This checks the subreddits that will be posted on and the amount of posts it will be making
    subreddit = reddit.subreddit(subreddits[pos])
    # This tells reddit what to post. It will post a title and some text which will be input by the user
    subreddit.submit(title, selftext=selftext)
    pos = pos + 1
    # This will check to see if there is anymore subreddits that it needs to post on.
    if pos <= len(subreddits) - 1:
        body_post()
    else:
        # If there is no other subreddit it needs to post on it will say post successful
        print("Post Successful")


def picture_post():
    global subreddits
    global pos
    # Check line 25 for explanation
    subreddit = reddit.subreddit(subreddits[pos])
    # This will tell reddit to post a title and a url. The url and title are user selected.
    subreddit.submit(title, url=url)
    pos = pos + 1
    # check line 30 and 34 to see explanation
    if pos <= len(subreddits) - 1:
        picture_post()
    else:
        print("Post Successful!")


def poll_post():
    global subreddits
    global pos
    # Check line 25 for explanation
    subreddit = reddit.subreddit(subreddits[pos])
    # This is telling reddit that it is going to post a poll, It will post a title that is selected by the user. The
    # selftext is not used and remains blank. The options is a list each item will be printed onto a separate box on
    # reddit. The duration is an integer and it tells reddit how many days the poll will be accepting votes from a min
    # of 1 days to a max of 7 days if numbers above 7 are added it will max at 7 days no error.
    subreddit.submit_poll(title, selftext='', options=options, duration=int(duration))
    pos = pos + 1
    # check line 30 and 34 for explanation
    if pos <= len(subreddits) - 1:
        poll_post()
    else:
        print("Post Successful")


def commentPost():
    # This lets the bot be the first comment on the newest post(which is the one that is made here) so right as you
    # post a comment is left on that post as well
    for submission in reddit.subreddit("bottestgang").new(limit=1):
        reply = reddit.submission(submission)
        reply.reply("Hey! That's great! While you're here on be sure to check out the owners socials! Youtube: Twitch: "
                    "Twitter: Twitch: Instagram")


def checkReddit():
    # This will check the subreddit to see that it successfully posted
    for submission in reddit.subreddit("bottestgang").new(limit=5):
        print("- " + submission.title)
        print()
    print("_____________")
    print("Done")


# This decides Whether the user wants to post a picture or wants to type out the text
postType = input('What kind of post would you like?\n Enter "Picture" or "Pic" for a post with a picture. \n Or \n '
                 'Enter '
                 '"Text" or "T" for a post with text.\n Or \n Enter "Poll" or "P" to start a poll.\n').lower()

# If the user enters Picture or Pic it will send the user down this path where the user will enter a link and it will
# post the link.
if postType == "picture" or postType == "pic":
    print("What would you like to title your picture?")
    title = input("")
    print("please enter a url (imgur links are the most friendly to me! \n Hint if you get stuck trying to post the "
          "link try clicking the line below the link and then pressing enter!")
    url = input("")
    # This will run the function post and will post a picture to the subreddit
    picture_post()

# Else, If the user enters Text or T, it will sent them down this path where they have to enter the text they want in
# the post
elif postType == "text" or postType == "t":
    print("What would you like you title of your text to be?")
    title = input("")
    print("please add your text here!")
    selftext = input("")
    # This will run the function and will post the entered text to the subreddit
    body_post()
# If the user happens to want a poll and enters poll or p, it will send them here
elif postType == "poll" or postType == "p":
    print("What would you like you title of your poll to be?")
    title = input("")
    print("how many options do you want to be in the poll?")
    # The user will choose how many options they want in their poll here
    items_poll = int(input(""))
    options = []
    for i in range(items_poll):
        print("what would you like to add?")
        # This adds the items they want to the list
        additions = input("")
        options.append(additions)
    # The duration in line 50 will take this variable
    # Prevents user from entering 0
    duration = input("how many days(1-7) would you like the poll to last? \n")
    while duration == "0":
        duration = input("Oops try again! A number between 1 and 7 \n")
        if duration != "0":
            break
    poll_post()
# If Picture, Pic, Text, T, Poll or P are not entered this will run and the rest of the program will finish and
# nothing will be uploaded to the subreddit
else:
    print('''Oops you didn't enter
    Picture or P
    Or
    Text or T''')
