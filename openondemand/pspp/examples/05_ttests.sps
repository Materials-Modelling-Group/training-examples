* T-Tests in PSPP
* Demonstrates various t-test procedures

* Sample data
DATA LIST LIST /id group (A1) before after.
BEGIN DATA.
1 A 100 105
2 A 95 102
3 A 110 115
4 A 88 92
5 A 105 110
6 B 98 103
7 B 102 108
8 B 89 94
9 B 95 100
10 B 107 112
END DATA.

VARIABLE LABELS
id 'Participant ID'
group 'Group'
before 'Pre-test Score'
after 'Post-test Score'.

VALUE LABELS group 'A' 'Control' 'B' 'Treatment'.

* === One-Sample T-Test ===
* Test if mean of 'before' differs from 100

T-TEST /TESTVAL=100
/VARIABLES=before.

* === Independent Samples T-Test ===
* Compare 'before' scores between groups A and B

T-TEST GROUPS=group('A' 'B')
/VARIABLES=before after.

* === Paired Samples T-Test ===
* Compare before and after scores

T-TEST PAIRS=before WITH after (PAIRED).

* === Additional Options ===

* T-test with confidence interval
T-TEST GROUPS=group('A' 'B')
/VARIABLES=before
/CRITERIA=CIN(95).

* Multiple variables
T-TEST GROUPS=group('A' 'B')
/VARIABLES=before after.

* Display group statistics
MEANS TABLES=before after BY group
/CELLS=MEAN COUNT STDDEV.

* End of t-test examples
