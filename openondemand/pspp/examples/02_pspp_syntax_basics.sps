* PSPP Syntax Basics
* This file demonstrates fundamental PSPP syntax structure

* Comments start with asterisk and end with period.

* === DATA INPUT ===

* Method 1: Inline data
DATA LIST LIST /id age gender (A1) score.
BEGIN DATA.
1 25 M 85
2 30 F 92
3 22 M 78
4 28 F 88
END DATA.

* Method 2: From CSV file
* DATA LIST FILE='/home/username/data.csv' free (',')
* /id age gender (A1) score.

* Method 3: From SPSS file
* GET FILE='/home/username/data.sav'.

* === VARIABLE LABELS ===

VARIABLE LABELS
id 'Participant ID'
age 'Age in years'
gender 'Gender'
score 'Test Score'.

* === VALUE LABELS ===

VALUE LABELS
gender 'M' 'Male' 'F' 'Female'.

* === MISSING VALUES ===

* Define missing values
MISSING VALUES score (-99, -98).

* === DATA TRANSFORMATION ===

* Compute new variable
COMPUTE age_group = 1.
IF (age >= 25) age_group = 2.
EXECUTE.

VALUE LABELS age_group
1 'Under 25'
2 '25 and over'.

* Recode variable
RECODE score (0 THRU 70=1) (71 THRU 85=2) (86 THRU 100=3)
INTO performance.

VALUE LABELS performance
1 'Low'
2 'Medium'
3 'High'.

* === DESCRIPTIVE STATISTICS ===

* Summary statistics
DESCRIPTIVES VARIABLES=age score
/STATISTICS=MEAN STDDEV MIN MAX MEDIAN.

* Frequency tables
FREQUENCIES VARIABLES=gender age_group performance
/STATISTICS=MODE.

* Crosstabulation
CROSSTABS
/TABLES=gender BY age_group
/STATISTICS=CHISQ.

* === EXPORT OUTPUT ===

* Export to text file
* OUTPUT EXPORT /CONTENTS EXPORT=ALL
* /TXT DOCUMENTFILE='/home/username/output.txt'.

* End of syntax
