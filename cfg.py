import os

from dotenv import load_dotenv

import logging

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
techspec_api_id = os.getenv("TECHSPEC_API_ID")
techspec_api_key = os.getenv("TECHSPEC_API_KEY")

logging.basicConfig(
    filename="chatbot_logs.txt",
    format='%(asctime)s %(message)s',
    filemode='w',
    level=logging.INFO
)

logger = logging.getLogger()