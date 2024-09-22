import csv
from jinja2 import Environment, FileSystemLoader

# Load Jinja2 environment and templates directory
env = Environment(loader=FileSystemLoader('templates'))

# Paths to the CSV files for Adrienne Stewart and Alex Nemecek
adrienne_csv = "athletes/womens_team/Adrienne Stewart21142907.csv"
alex_csv = "athletes/mens_team/Alex Nemecek18820260.csv"

# Function to load and clean CSV data
def load_csv_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader if row]  # Remove empty rows
    return data

# Extract athlete info from CSV
def extract_athlete_info(data):
    athlete_name = data[0][0] if len(data[0]) > 0 else "Unknown"
    athlete_id = data[1][0] if len(data) > 1 else "Unknown"
    athlete_link = f"https://www.athletic.net/athlete/{athlete_id}/cross-country/high-school"
    athlete_grade = next((row[2] for row in data if len(row) > 2 and row[2].isdigit()), "N/A")
    return athlete_name, athlete_id, athlete_link, athlete_grade

# Load CSV data for both athletes
adrienne_data = load_csv_data(adrienne_csv)
alex_data = load_csv_data(alex_csv)

# Extract athlete info
adrienne_name, adrienne_id, adrienne_link, adrienne_grade = extract_athlete_info(adrienne_data)
alex_name, alex_id, alex_link, alex_grade = extract_athlete_info(alex_data)

# Generate season records
def extract_season_records(data):
    return [
        {"Year": int(row[1]), "Grade": int(row[2]), "Time": row[3]}
        for row in data if len(row) > 3 and row[1].isdigit() and int(row[1]) > 1999
    ]

# Extract season records for each athlete
adrienne_records = extract_season_records(adrienne_data)
alex_records = extract_season_records(alex_data)

# Generate dynamic HTML table from data
def table_maker(list_dicts):
    if not list_dicts:
        return "<p>No data available</p>"
    
    # Create the HTML table
    html_table = "<table>\n<tr>\n"
    for key in list_dicts[0].keys():
        html_table += f"<th>{key}</th>\n"
    html_table += "</tr>\n"
    
    # Add rows
    for entry in list_dicts:
        html_table += "<tr>\n"
        for value in entry.values():
            html_table += f"<td>{value}</td>\n"
        html_table += "</tr>\n"
    
    html_table += "</table>\n"
    return html_table

# Generate tables for season records
adrienne_table = table_maker(adrienne_records)
alex_table = table_maker(alex_records)

# Top 10 for index page
mens_top10 = [{"Rank": 1, "Name": "Alex Nemecek", "Time": "19:21.4 SR"}]
womens_top10 = [{"Rank": 1, "Name": "Adrienne Stewart", "Time": "23:31.1 SR"}]

mens_top10_table = table_maker(mens_top10)
womens_top10_table = table_maker(womens_top10)

# Render the index.html template (for both men and women)
index_template = env.get_template('index.html')
index_html = index_template.render(
    site_title="Men's and Women's Top 10 XC Times",
    page_heading="Top 10 Overall Rankings for Men and Women",
    mens_top10_table=mens_top10_table,
    womens_top10_table=womens_top10_table
)

# Save the generated index.html
with open("index.html", "w") as f:
    f.write(index_html)

# Render and save athlete pages
athlete_template = env.get_template('athlete.html')

# Adrienne Stewart's page
athlete_html_adrienne = athlete_template.render(
    athlete_name=adrienne_name,
    athlete_grade=adrienne_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=adrienne_table,
    all_records_table=adrienne_table,
    season_notes="<li>2024: Best season performance</li>"
)
with open("athlete-adrienne.html", "w") as f:
    f.write(athlete_html_adrienne)

# Alex Nemecek's page
athlete_html_alex = athlete_template.render(
    athlete_name=alex_name,
    athlete_grade=alex_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=alex_table,
    all_records_table=alex_table,
    season_notes="<li>2024: Best season performance</li>"
)
with open("athlete-alex.html", "w") as f:
    f.write(athlete_html_alex)

# Confirm completion
print('HTML pages generated for index, Adrienne Stewart, and Alex Nemecek')