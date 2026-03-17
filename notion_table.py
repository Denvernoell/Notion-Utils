import tomli
import pandas as pd
from notion_client import Client
from pathlib import Path
# secrets_path = Path(__file__).parent.parent.parent.parent / '.streamlit' / 'secrets.toml'
secrets_path = Path(r"I:\Project Resources\Ag Water\apps\district_management\.streamlit\secrets.toml")


with open(
	# r"I:\Project Resources\Ag Water\apps\district_management\.streamlit\secrets.toml",
	secrets_path,
	'rb') as f:

	config = tomli.load(f)

notion = Client(auth=config['Notion']['token'])
def add_row_to_data_entry(row):
	table_id = "70297de1fd984a7eb010d9a7f3108a19"
	row['Grower'] = row['Grower'].replace(',','')
	try:
		notion.pages.create(
			parent={"database_id": table_id},
			properties={
				"Name": {
					"title": [
						{
							"text": {
								"content": row['path']
							}
						}
					]
				},
				"Category": {
					"select": {
						"name": row['category']
					}
				},
				"Year": {
					"select": {
						"name": row['year']
					}
				},
				"Grower": {
					"select": {
						"name": row['Grower']
					}
				},

			},
		)
	except Exception as e:
		print(e)