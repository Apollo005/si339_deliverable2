import csv
csv_file = "athletes/mens_team/Alex Nemecek18820260.csv"

# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
   reader = csv.reader(file, delimiter=',')
   
   # grab all the data
   data = list(reader)
   # print(f"data is\n{data}")
   
   # remove empty objects
   for item in data:
      if item == []:
         data.remove(item)
   
   count = 0
   for row in data:
      print(f"\nrow {count} is now {row}\n")
      count += 1


# Extract the data from the CSV
athlete_name = data[0]
for fullname in athlete_name:
   athlete_first_last_name = fullname.split()
athlete_id = data[1]
athelete_link = f"https://www.athletic.net/athlete/{athlete_id[0]}/cross-country/high-school"


# season records
season_records = []
for row in data:
   # skip the header
   if len(row) < 3:
      continue
   if row[0] == "Name":
      continue
   # print(f"row is {row}")

   # only work through it if it's a year
   # append season, grade, time to season list
   if int(row[1]) > 1999:
      season_info = []
      season_info.append(int(row[1]))
      season_info.append(int(row[2]))
      season_info.append(row[3])

      # append season data
      season_records.append(season_info)
# print(f"season records is {season_records}")
# define fstring with data for each season
# 4 max seasons so index from 3 to 0
year_4_records = ""
year_3_records = ""
year_2_records = ""
year_1_records = ""
for season in season_records:
   try:
      year_4 = season_records[3]
      year_4_records = f"Year: {(season_records[3])[0]}   Grade: {(season_records[3])[1]}   Best Time: {(season_records[3])[2]}"
   except:
      pass
   
   try:
      year_3 = season_records[2]
      year_3_records = f"Year: {(season_records[2])[0]}   Grade: {(season_records[2])[1]}   Best Time: {(season_records[2])[2]}"
   except:
      pass
   
   try:
      year_2 = season_records[1]
      year_2_records = f"Year: {(season_records[1])[0]}   Grade: {(season_records[1])[1]}   Best Time: {(season_records[1])[2]}"
   except:
      pass
   
   try:
      year_1 = season_records[0]
      year_1_records = f"Year: {(season_records[0])[0]}   Grade: {(season_records[0])[1]}    Best Time: {(season_records[0])[2]}"
   except:
      pass

races = []
for row in data:
   # skip the header
   if len(row) < 3:
      continue   
   if row[0] == "Name":
      continue

   if int(row[1]) < 1999:
      rowdict = dict(place = row[1], time = row[3], date = row[4], meet = row[5], comments = row[6], photo = row[7])
      races.append(rowdict)
print(f"races list is {races}")

# compare dates
races_2024 = []
for race in races:
   if "Aug" in race["date"][0:3]:
      break
   races_2024.append(race)

def table_maker(list_dicts):
   # Create the header row (assuming all dictionaries have the same keys)
   html_table = "<table border='1'>\n"
   html_table += "  <tr>\n"
   for key in list_dicts[0].keys():
      html_table += f"    <th>{key}</th>\n"
   html_table += "  </tr>\n"

   # Create the data rows
   for entry in list_dicts:
      html_table += "  <tr>\n"
      for value in entry.values():
         html_table += f"    <td>{value}</td>\n"
      html_table += "  </tr>\n"

   html_table += "</table>"
   return html_table

races_2024_formatted = table_maker(races_2024)


# Start building the HTML structure
PAGENAME = "test page"

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel = "stylesheet" href = "css/reset.css">
   <link rel = "stylesheet" href = "css/style.css">
   <title>{athlete_name[0]} Statistics</title>
</head>

<body>
   <main>

      <header>
         <h1>{athlete_name[0]} Cross Country Statistics</h1>
         <a href={athelete_link}>{athlete_first_last_name[0]}'s Athletic.net Profile</a>
         <nav>
            <ul>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
            </ul>
         </nav>
      </header>

      <section class="season_records">
         {year_4_records}
         {year_3_records}
         {year_2_records}
         {year_1_records}
      </section>

      <section>
         {races_2024_formatted}
      </section>
   <main>
'''

filename = "test_html"
filename += ".html"
with open(filename, "w") as f:
   f.write(f"{html_content}")