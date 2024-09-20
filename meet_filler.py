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
      # print(f"\nrow {count} is now {row}\n")
      count += 1


# Extract the data from the CSV
athlete_name = data[0]
for fullname in athlete_name:
   athlete_first_last_name = fullname.split()
athlete_id = data[1]
athelete_link = f"https://www.athletic.net/athlete/{athlete_id[0]}/cross-country/high-school"

athlete_grade = ""
for row in data:
   # skip the header
   if len(row) < 3:
      continue
   if row[0] == "Name":
      continue

   if (row[2]).isdigit():
      athlete_grade = row[2]
   

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


# records
# 4 max seasons so index from 3 to 0
for season in season_records:
   try:
      data_2024 = season_records[3]
      records_2024 = {}
      records_2024["Year"] = data_2024[0]
      records_2024["Grade"] = data_2024[1]
      records_2024["Time"] = data_2024[2]
   except:
      pass
   
   try:
      data_2023 = season_records[2]
      records_2023 = {}
      records_2023["Year"] = data_2023[0]
      records_2023["Grade"] = data_2023[1]
      records_2023["Time"] = data_2023[2]
   except:
      pass
   
   try:
      data_2022 = season_records[1]
      records_2022 = {}
      records_2022["Year"] = data_2022[0]
      records_2022["Grade"] = data_2022[1]
      records_2022["Time"] = data_2022[2]
   except:
      pass
   
   try:
      data_2021 = season_records[0]
      records_2021 = {}
      records_2021["Year"] = data_2021[0]
      records_2021["Grade"] = data_2021[1]
      records_2021["Time"] = data_2021[2]
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
      rowdict = dict(Place = row[1], Time = row[3], Date = row[4], Meet = row[5])
      # , Comments = row[6], Photo = row[7])
      races.append(rowdict)
# print(f"races list is {races}")

# compare dates
races_2024 = []
for race in races:
   if "Aug" in race["Date"][0:3]:
      break
   races_2024.append(race)

def table_maker(list_dicts):
   # https://chatgpt.com/share/66edc722-06f0-8003-906c-20fbadf39016
   # Create the header row (assuming all dictionaries have the same keys)
   html_table = "<table>\n"
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
races_2024_table = table_maker(races_2024)

# haven't yet created a way to compare multiple athlete times yet
# for now, we will use a single time and placeholders
mens_top10 = [{"Rank": 1, "Name": "Alex Nemecek", "Time": "19:21.4 SR"}]
for repeats in range(9):
   mens_top10.append({"Rank": "Lorem Ipsum", "Name": "Dolor Sit", "Time": "amet"})
womens_top10 = [{"Rank": 1, "Name": "Adrienne Stewart", "Time": "23:31.1 SR"}]
for repeats in range(9):
   womens_top10.append({"Rank": "Lorem Ipsum", "Name": "Dolor Sit", "Time": "amet"})

mens_top10_table = table_maker(mens_top10)
womens_top10_table = table_maker(womens_top10)

def season_records_table(*dicts):
    # https://chatgpt.com/share/66edd8a9-3a90-8003-b533-7b54d73996f1
    if not dicts:
        return None
    
    # Extract the table headers from the first dictionary
    headers = dicts[0].keys()
    
    # Create the HTML table structure
    html = '<table>\n'
    
    # Add the table headers
    html += "  <tr>\n"
    for header in headers:
        html += f"    <th>{header}</th>\n"
    html += "  </tr>\n"
    
    # Add the table rows for each dictionary
    for d in dicts:
        html += "  <tr>\n"
        for key in headers:
            html += f"    <td>{d[key]}</td>\n"
        html += "  </tr>\n"
    
    html += "</table>"
    
    return html
all_records_table = season_records_table(records_2024, records_2023, records_2022, records_2021)





# Start building the HTML structure
PAGENAME = "test page"

# html_content = f'''<!DOCTYPE html>
# <html lang="en">
# <head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <link rel = "stylesheet" href = "css/reset.css">
#    <link rel = "stylesheet" href = "css/style.css">
#    <title>{athlete_name[0]} Statistics</title>
# </head>

# <body>
#    <main>

#       <header>
#          <h1>{athlete_name[0]} Cross Country Statistics</h1>
#          <a href={athelete_link}>{athlete_first_last_name[0]}'s Athletic.net Profile</a>
#          <nav>
#             <ul>
#                <li><a href="<{PAGENAME}>">PAGENAME</a></li>
#                <li><a href="<{PAGENAME}>">PAGENAME</a></li>
#                <li><a href="<{PAGENAME}>">PAGENAME</a></li>
#                <li><a href="<{PAGENAME}>">PAGENAME</a></li>
#             </ul>
#          </nav>
#       </header>

#       <section class="season_records">
#          {year_4_records}
#          {year_3_records}
#          {year_2_records}
#          {year_1_records}
#       </section>

#       <section>
#          {races_2024_formatted}
#       </section>
#    <main>
# '''

index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="css/reset.css">
   <link rel="stylesheet" href="css/style.css">
   <title>Kaelyn.cc</title>
   <!-- Include Font Awesome for search icon -->
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>

<body>
    <header>
        <a href="index.html" class="nav-home-button">HOME</a>
        <form action="#" method="get" class="search-form">
            <button type="submit">
                <i class="fas fa-search"></i> <!-- Search icon from Font Awesome -->
            </button>
            <input type="text" placeholder="Search Athlete" name="q">
        </form>
    </header>

    <main>
        <h1>Top 10 Overall Rankings for Men and Women</h1>

        <section class="meet-results">
            <!-- Men's Rankings -->
            <div class="season-box">
                <h3>Top 10 Men</h3>
                {mens_top10_table}
            </div>

            <!-- Women's Rankings -->
            <div class="season-box">
                <h3>Top 10 Women</h3>
                {womens_top10_table}
            </div>
        </section>
    </main>
</body>
</html>

'''

athlete_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Athlete Profile</title>
</head>
<body>

    <header>
        <a href="index.html" class="nav-home-button">HOME</a>
        <form action="#" method="get" class="search-form">
            <button type="submit">
                <i class="fas fa-search"></i> <!-- Search icon from Font Awesome -->
            </button>
            <input type="text" placeholder="Search Athlete" name="q">
        </form>
    </header>
    
    <!-- Include Font Awesome in the head section of your HTML -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">      

<main>
    <section class="profile-header">
        <div class="profile-picture">
            <!-- Placeholder for profile image -->
            <img src="img/profile-placeholder.png" alt="Profile picture">
        </div>
        <div class="profile-details">
            <h2>{athlete_name}</h2>
            <p>{athlete_grade}th Grade, Ann Arbor Skyline</p>
            <button class="photos-button">Photos</button>
        </div>
    </section>

    <section class="meet-results">
        <div class="meet-year season-box">
            <h3>2024 Races</h3>
            {races_2024_table}
        </div>
        <div class="season-records season-box">
            <h3>Season Records</h3>
            {all_records_table}
        </div>
        <div class="season-notes season-box">
            <h3>Season Notes</h3>
            <ul>
                <li>2021: Lorem ipsum ...</li>
                <li>2022: Lorem ipsum ...</li>
                <li>2023: Lorem ipsum ...</li>
            </ul>
        </div>
    </section>

</main>

</body>
</html>
'''




filename = "index-filled"
filename += ".html"
with open(filename, "w") as f:
   f.write(f"{index_content}")
print(f"\nIndex file is now written!\n\n\n")

filename = "athlete-filled"
filename += ".html"
with open(filename, "w") as f:
   f.write(f"{athlete_content}")
print(f"\nAthlete file is now written!\n\n\n")