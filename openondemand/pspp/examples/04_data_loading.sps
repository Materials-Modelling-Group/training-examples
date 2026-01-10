* Data Loading Examples in PSPP

* === Method 1: CSV File ===

* Load from CSV with comma delimiter
DATA LIST FILE='/home/username/data.csv' free (',')
/id gender (A1) age score.

* Specify column types explicitly
* DATA LIST FILE='/home/username/data.csv' free (',')
* /id (F5.0) gender (A10) age (F3.0) score (F5.2).

* === Method 2: Tab-delimited File ===

* Load from tab-delimited file
* DATA LIST FILE='/home/username/data.txt' free
* /id gender (A1) age score.

* === Method 3: Fixed-width Format ===

* For fixed-width text files
* DATA LIST FILE='/home/username/data.dat' fixed
* /id 1-5 gender 7 age 9-10 score 12-16(2).

* === Method 4: SPSS .sav File ===

* Load SPSS data file
* GET FILE='/home/username/data.sav'.

* === Method 5: Inline Data ===

* Small datasets can be entered directly
DATA LIST LIST /id age group (A1) value.
BEGIN DATA.
1 25 A 85.5
2 30 B 92.3
3 22 A 78.9
4 28 B 88.1
5 26 A 91.2
END DATA.

* === Add Variable and Value Labels ===

VARIABLE LABELS
id 'Participant ID'
age 'Age in years'
group 'Experimental Group'
value 'Outcome Score'.

VALUE LABELS
group 'A' 'Control' 'B' 'Treatment'.

* === Handle Missing Values ===

* Define what constitutes missing data
MISSING VALUES age value (-99, -98, -97).

* System missing uses just period: .

* === Display Data ===

* List first 10 cases
LIST /CASES FROM 1 TO 10.

* List all cases (use with caution on large datasets)
* LIST.

* === Summary of Data ===

DISPLAY DICTIONARY.

* End of data loading examples
