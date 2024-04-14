import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Get the secrets from environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Set the environment variables
os.environ['GOOGLE_API_KEY'] = google_api_key
os.environ['OPENAI_API_KEY'] = openai_api_key