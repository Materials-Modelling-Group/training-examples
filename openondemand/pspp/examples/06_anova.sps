* ANOVA in PSPP
* One-way Analysis of Variance with post-hoc tests

* Sample data with three groups
DATA LIST LIST /id group score.
BEGIN DATA.
1 1 85
2 1 92
3 1 78
4 1 88
5 1 95
6 2 72
7 2 79
8 2 68
9 2 75
10 2 81
11 3 90
12 3 95
13 3 88
14 3 92
15 3 97
END DATA.

VARIABLE LABELS
id 'Participant ID'
group 'Treatment Group'
score 'Test Score'.

VALUE LABELS group
1 'Control'
2 'Treatment A'
3 'Treatment B'.

* === Descriptive Statistics by Group ===

MEANS TABLES=score BY group
/CELLS=MEAN STDDEV COUNT MIN MAX.

* === One-Way ANOVA ===

ONEWAY score BY group
/STATISTICS=DESCRIPTIVES HOMOGENEITY
/POSTHOC=TUKEY BONFERRONI.

* === Alternative: ANOVA Command ===

* More detailed ANOVA output
* ANOVA score BY group.

* === Interpretation Notes ===

* Look for:
* 1. F-statistic and p-value
* 2. Levene's test for homogeneity of variance
* 3. Post-hoc tests show which groups differ

* === Non-parametric Alternative ===

* If assumptions violated, use Kruskal-Wallis
NPAR TESTS
/K-W=score BY group(1,3).

* End of ANOVA examples
