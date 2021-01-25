import json
from rich.console import Console
from rich.table import Table
from rich.theme import Theme







with open('job_data.json') as json_data:
    jsonData = json.load(json_data)

    table = Table(title= 'Job Search Results')
    table.add_column('Job Title', justify= 'right', style='cyan on white', no_wrap=True)
    table.add_column('Location', style='red on white')
    table.add_column('Company', style='green on white')
    table.add_column('Links', justify='right', style='purple on white')
    for job in jsonData:
        table.add_row(job['Job Titles'], job['Locations'], job['Companies'], job['Links'])
    console = Console()
    console.print(table) 





    