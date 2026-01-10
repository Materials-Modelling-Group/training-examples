* Crosstabulation and Chi-Square Tests in PSPP

* Sample survey data
DATA LIST LIST /id gender (A1) agegroup (A1) satisfied (A1).
BEGIN DATA.
1 M Y Y
2 F Y N
3 M O Y
4 F Y Y
5 M O N
6 F O Y
7 M Y N
8 F O Y
9 M Y Y
10 F Y N
11 M O Y
12 F O N
13 M Y Y
14 F Y Y
15 M O N
END DATA.

VARIABLE LABELS
id 'Respondent ID'
gender 'Gender'
agegroup 'Age Group'
satisfied 'Satisfied with Service'.

VALUE LABELS
gender 'M' 'Male' 'F' 'Female'
/agegroup 'Y' 'Young' 'O' 'Older'
/satisfied 'Y' 'Yes' 'N' 'No'.

* === Simple Crosstabulation ===

CROSSTABS
/TABLES=gender BY satisfied.

* === With Percentages ===

CROSSTABS
/TABLES=gender BY satisfied
/CELLS=COUNT ROW COLUMN TOTAL.

* === With Chi-Square Test ===

CROSSTABS
/TABLES=gender BY satisfied
/STATISTICS=CHISQ PHI.

* === Three-Way Table ===

CROSSTABS
/TABLES=gender BY satisfied BY agegroup.

* === Multiple Tables ===

CROSSTABS
/TABLES=gender agegroup BY satisfied
/STATISTICS=CHISQ
/CELLS=COUNT EXPECTED ROW.

* === Interpretation ===

* Chi-square tests association between variables
* Phi coefficient shows strength of association
* Expected counts should be > 5 for valid chi-square

* End of crosstabulation examples
