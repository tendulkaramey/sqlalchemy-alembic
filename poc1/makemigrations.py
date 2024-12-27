# makemigrations.py
# alembic revision --autogenerate -m "your message"  -- cli equvialent
from alembic import command
from alembic.config import Config

def make_migrations(message):
   try:
       alembic_cfg = Config("alembic.ini")
       command.revision(alembic_cfg, message=message, autogenerate=True)
       print("Migration file created successfully")
   except Exception as e:
       print(f"Failed to create migration: {e}")

if __name__ == "__main__":
   import sys
   if len(sys.argv) > 1:
       make_migrations(sys.argv[1])
   else:
       print("Please provide a migration message")
       print("Usage: python makemigrations.py 'your migration message'")