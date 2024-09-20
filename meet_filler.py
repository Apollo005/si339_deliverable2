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
   print(f"\n\n\n\ndata is now {data}")


# Extract the data from the CSV
athlete_name = data[0]
for fullname in athlete_name:
   athlete_first_last_name = fullname.split()
athlete_id = data[1]
athelete_link = f"https://www.athletic.net/athlete/{athlete_id}/cross-country/high-school"

# get header names
header = data[2]
for index in range(len(header)):
   if index == 0:
      pass
   if index == 1:
      column_title_place = header[index]
   if index == 2:
      column_title_grade = header[index]
   if index == 3:
      column_title_time = header[index]
   if index == 4:
      column_title_date = header[index]
   if index == 5:
      column_title_meet = header[index]
   if index == 6:
      column_title_comments = header[index]
   # if index == 7:
   #    column_title_photo = header[index]


# season records
season_records = []
for row in data:
   # skip the header
   if len(row) < 3:
      continue
   if row[0] == "Name":
      continue
   print(f"row is {row}")

   # only work through it if it's a year
   # append season, grade, time to season list
   if int(row[1]) > 1999:
      season_info = []
      season_info.append(int(row[1]))
      season_info.append(int(row[2]))
      season_info.append(row[3])

      # append season data
      season_records.append(season_info)


print(f"season records is {season_records}")




# print(f"meet name {meet_name}")
# print(f"meet_date {meet_date}")
# print(f"folder_name {folder_name}")
# print(f"race_comments{race_comments}")


# Athlete details start from row 2 (index 1)
athletes = data[1:]


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
         <a href={athelete_link[0]}>{athlete_first_last_name[0]}'s Athletic.net Profile</a>
         <nav>
            <ul>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
               <li><a href="<{PAGENAME}>">PAGENAME</a></li>
            </ul>
         </nav>
      </header>

      <section>
         team_results_link
      </section>
   <main>
'''

filename = "test_html"
filename += ".html"
with open(filename, "w") as f:
   f.write(f"{html_content}")