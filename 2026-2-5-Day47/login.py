class User:
  def __init__(self,username):
    self.username = username
    self.logged_in = False

  
  def login(self):
    self.logged_in = True
    print(self.username,"logged in")

  def logout(self):
    self.logged_in = False
    print(self.username,"logged out")

u = User("Ken")
u.login()
u.logout()    
