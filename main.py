from user import User
from post import Post

app_user_one = User("ec@h.co", "Tim Smith", "pwd", "Software Engineer")
app_user_one.get_user_info()

app_user_two = User("yt@h.co", "Carl Smith", "pwd", "DevOps Engineer")
app_user_two.get_user_info()

book_one = Post("Kevin is sick", "Ben Simmons")
book_one.get_post_info()
