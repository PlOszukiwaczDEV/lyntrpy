__version__ == "1.0.0"

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Load cookies from environment variables
cookies = {
    '_TOKEN__DO_NOT_SHARE': os.getenv('TOKEN'),
    'temp-discord-token': os.getenv('temp-discord_token'),
    'cf_clearance': os.getenv('cf_clearance'),
}