import sqlite3
import os
import pandas as pd
import requests

#Getting Values from Online Tables

url = 'https://en.wikipedia.org/wiki/List_of_Formula_One_drivers'
response = requests.get(url)

arr = pd.read_html(response.content)[2].values[:-1]

url = "https://en.wikipedia.org/wiki/List_of_Formula_One_circuits"
response = requests.get(url)

arr_track = pd.read_html(response.content)[2].values[:-1]

url = "https://en.wikipedia.org/wiki/List_of_Formula_One_constructors"
response = requests.get(url)

arr_con = pd.read_html(response.content)[1].values[:-1]


url = "https://en.wikipedia.org/wiki/List_of_Formula_One_constructors"
response = requests.get(url)

arr_con2 = pd.read_html(response.content)[2].values[:-1]



#Starting the Table 

os.remove("F1.db")
con = sqlite3.connect("F1.db")

cur = con.cursor()

#Creation of the Tables

cur.execute("""
        CREATE TABLE drivers(
            idDriver INTEGER PRIMARY KEY,
            name VARCHAR(64), 
            nationality VARCHAR(64)
            )
        """)
cur.execute("""
        CREATE TABLE tracks(
            idTracks INTEGER PRIMARY KEY,
            name_track VARCHAR(64),
            country VARCHAR(64),
            gps_held DECIMAL(3),
            length DECIMAL(4,4)
            )
        """)
cur.execute("""
        CREATE TABLE years(
            idYears INTEGER PRIMARY KEY,
            year DECIMAL(4),
            constructor_champion INTEGER,
            driver_champion INTEGER,
            runner_up INTEGER
            )
        """)
cur.execute("""
        CREATE TABLE constructors( 
            idConstructors INTEGER PRIMARY KEY,
            name_cons VARCHAR(64),
            licensed_in VARCHAR(64),
            gp_ent INTEGER,
            gp_start INTEGER,
            con_wins INTEGER,
            con_points DECIMAL(4,4)
            )
        """)


#Giving the Tables Values

data = map(lambda r: [r[0].replace("*","").replace("^","").replace("~",""), r[1]],arr) 
data_track = map(lambda k: [k[0].replace("✔",""),k[4].split(", ")[1],float(k[5].split("(")[0].split("km")[0]),k[8]],arr_track)
data_con = map(lambda r: [r[0], r[2].split("[")[0], r[5], r[6], r[9], r[10]],arr_con)
data_con2 = map(lambda r: [r[0].split("[")[0].split(" (")[0],r[1].split("[")[0],r[3],r[4],r[7],0 if pd.isna(r[8]) else r[8]], arr_con2)

cur.executemany('INSERT INTO drivers (name, nationality) VALUES (?,?)', data)
cur.executemany('INSERT INTO tracks (name_track, country, length, gps_held) VALUES (?,?,?,?)', data_track)
cur.executemany('INSERT INTO constructors (name_cons, licensed_in, gp_ent, gp_start, con_wins, con_points) VALUES (?,?,?,?,?,?)', data_con2)
cur.executemany('INSERT INTO constructors (name_cons, licensed_in, gp_ent, gp_start, con_wins, con_points) VALUES (?,?,?,?,?,?)', data_con)
cur.execute('INSERT INTO constructors (name_cons, licensed_in, gp_ent, gp_start, con_wins, con_points) VALUES ("Williams", "United Kingdom", 779, 777, 114, 3592)')

cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2022, 142, 810, NULL)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2021, 141, 810, 339)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2020, 141, 339, 101)')

cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2019, 141, 339, 101)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2018, 141, 339, 811)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2017, 141, 339, 811)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2016, 141, 670, 339)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2015, 141, 339, 670)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2014, 141, 339, 670)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2013, 142, 811, 18)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2012, 142, 811, 18)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2011, 142, 811, 136)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2010, 142, 811, 18)')

cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2009, 19, 136, 811)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2008, 138, 339, 502)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2007, 138, 635, 339)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2006, 101, 18, 709)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2005, 101, 18, 635)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2004, 138, 709, 55)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2003, 138, 709, 635)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2002, 138, 709, 55)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2001, 138, 709, 180)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (2000, 138, 709, 335)')


cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1999, 138, 335, 386)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1998, 140, 335, 709)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1997, 143, 813, 271)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1996, 143, 364, 813)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1995, 16, 709, 364)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1994, 143, 709, 364)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1993, 143, 628, 719)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1992, 143, 490, 591)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1991, 140, 719, 490)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1990, 140, 719, 628)')


cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1989, 140, 628, 719)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1988, 140, 719, 628)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1987, 143, 612, 490)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1986, 143, 628, 490)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1985, 140, 628, 13)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1984, 140, 443, 628)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1983, 138, 612, 628)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1982, 138, 669, 615)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1981, 143, 612, 648)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1980, 143, 398, 612)')


cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1979, 138, 697, 812)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1978, 72, 26, 601)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1977, 138, 443, 697)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1976, 138, 378, 443)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1975, 138, 443, 251)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1974, 140, 251, 646)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1973, 72, 747, 251)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1972, 72, 251, 747)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1971, 127, 747, 601)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1970, 72, 657, 381)')


cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1969, 82, 747, 381)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1968, 72, 365, 747)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1967, 18, 377, 108)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1966, 18, 108, 758)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1965, 72, 170, 365)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1964, 138, 758, 365)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1963, 72, 170, 365)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1962, 20, 365, 170)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1961, 138, 366, 795)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1960, 28, 108, 515)')


cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1959, 28, 108, 120)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1958, 128, 352, 543)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1957, NULL, 239, 543)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1956, NULL, 239, 543)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1955, NULL, 239, 543)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1954, NULL, 239, 311)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1953, NULL, 36, 239)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1952, NULL, 36, 240)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1951, NULL, 239, 36)')
cur.execute('INSERT INTO years (year, constructor_champion, driver_champion, runner_up) Values (1950, NULL, 240, 239)')



con.commit()
