# crud.py
from sqlalchemy.orm import Session
from models.user import User
from models.post import Post
from database import SessionLocal

def create_user(email: str, name: str):
   with SessionLocal() as db:
       user = User(email=email, name=name)
       db.add(user)
       db.commit()
       db.refresh(user)
       return user

def create_post(title: str, content: str, author_id: int):
   with SessionLocal() as db:
       post = Post(title=title, content=content, author_id=author_id)
       db.add(post)
       db.commit()
       db.refresh(post)
       return post

def get_users():
   with SessionLocal() as db:
       return db.query(User).all()

def get_user_posts(user_id: int):
   with SessionLocal() as db:
       return db.query(Post).filter(Post.author_id == user_id).all()

# Usage example:
if __name__ == "__main__":
   # Create user
   user = create_user("test1@example.com", "Test User")
   
   # Create post
   post = create_post("My First Post", "Hello World!", user.id)
   
   # Get all users
   users = get_users()
   print(users)
   print(users[0].email)
   
   # Get user's posts
   posts = get_user_posts(user.id)
   print(posts)