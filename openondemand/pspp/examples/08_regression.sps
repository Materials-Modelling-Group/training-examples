* Regression Analysis in PSPP
* Linear and Logistic Regression

* Sample data
DATA LIST LIST /id age education income satisfaction.
BEGIN DATA.
1 25 12 35000 6
2 30 16 45000 7
3 22 12 28000 5
4 35 18 55000 8
5 28 14 40000 7
6 32 16 48000 7
7 26 12 32000 6
8 40 20 65000 9
9 29 16 42000 7
10 33 18 52000 8
END DATA.

VARIABLE LABELS
id 'Employee ID'
age 'Age in years'
education 'Years of Education'
income 'Annual Income'
satisfaction 'Job Satisfaction (1-10)'.

* === Simple Linear Regression ===

* Predict satisfaction from income
REGRESSION
/DEPENDENT=satisfaction
/METHOD=ENTER income.

* === Multiple Linear Regression ===

* Predict satisfaction from multiple predictors
REGRESSION
/DEPENDENT=satisfaction
/METHOD=ENTER age education income.

* === Stepwise Regression ===

* Let PSPP select best predictors
REGRESSION
/DEPENDENT=satisfaction
/METHOD=STEPWISE age education income.

* === Regression with Diagnostics ===

REGRESSION
/DEPENDENT=satisfaction
/METHOD=ENTER age education income
/SAVE=PRED RESID.

* This creates predicted values and residuals

* === Interpretation Notes ===

* Look for:
* 1. R-squared (variance explained)
* 2. F-statistic (overall model significance)
* 3. Coefficients and their p-values
* 4. Standardized coefficients (beta weights)

* === Correlation Matrix ===

* View correlations between all variables
CORRELATIONS
/VARIABLES=age education income satisfaction.

* === For Logistic Regression ===

* First create binary outcome
COMPUTE outcome = 0.
IF (satisfaction >= 7) outcome = 1.
EXECUTE.

VALUE LABELS outcome
0 'Low Satisfaction'
1 'High Satisfaction'.

* Logistic regression
LOGISTIC REGRESSION outcome WITH age education income.

* End of regression examples
