import tomli
from notion_client import Client
from pathlib import Path
# secrets_path = Path(__file__).parent.parent.parent.parent / '.streamlit' / 'secrets.toml'
secrets_path = Path(r"I:\Project Resources\Coding\Credentials\denver.toml")


with open(
	# r"I:\Project Resources\Ag Water\apps\district_management\.streamlit\secrets.toml",
	secrets_path,
	'rb') as f:

	config = tomli.load(f)

notion = Client(auth=config['Notion']['notes_token'])