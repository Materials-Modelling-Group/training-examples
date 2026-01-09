# Statistical Analysis in R
# Demonstrates common statistical tests and procedures

cat("Statistical Analysis Examples\n")
cat("=============================\n\n")

# Use built-in datasets
data(mtcars)
data(iris)

# === Descriptive Statistics ===

cat("=== Descriptive Statistics ===\n")

# Summary statistics
cat("\nSummary of mpg:\n")
summary(mtcars$mpg)

# More detailed statistics
cat("\nDetailed statistics for mpg:\n")
cat("  Mean:", mean(mtcars$mpg), "\n")
cat("  Median:", median(mtcars$mpg), "\n")
cat("  SD:", sd(mtcars$mpg), "\n")
cat("  Variance:", var(mtcars$mpg), "\n")
cat("  Min:", min(mtcars$mpg), "\n")
cat("  Max:", max(mtcars$mpg), "\n")
cat("  Range:", range(mtcars$mpg), "\n")
cat("  IQR:", IQR(mtcars$mpg), "\n")

# === T-Tests ===

cat("\n=== T-Tests ===\n")

# One-sample t-test
# Test if mean mpg is different from 20
t_one <- t.test(mtcars$mpg, mu = 20)
cat("\nOne-sample t-test (H0: mean = 20):\n")
print(t_one)

# Two-sample t-test
# Compare mpg between automatic and manual transmission
auto <- mtcars$mpg[mtcars$am == 0]
manual <- mtcars$mpg[mtcars$am == 1]

t_two <- t.test(auto, manual)
cat("\nTwo-sample t-test (automatic vs manual):\n")
print(t_two)

# Paired t-test (example with made-up data)
before <- rnorm(20, mean = 100, sd = 15)
after <- before + rnorm(20, mean = 5, sd = 10)
t_paired <- t.test(before, after, paired = TRUE)
cat("\nPaired t-test:\n")
print(t_paired)

# === ANOVA ===

cat("\n=== Analysis of Variance ===\n")

# One-way ANOVA
# Test if mpg differs by number of cylinders
anova_result <- aov(mpg ~ factor(cyl), data = mtcars)
cat("\nOne-way ANOVA (mpg by cylinders):\n")
print(summary(anova_result))

# Post-hoc test (Tukey HSD)
cat("\nTukey HSD post-hoc test:\n")
print(TukeyHSD(anova_result))

# === Linear Regression ===

cat("\n=== Linear Regression ===\n")

# Simple linear regression
model_simple <- lm(mpg ~ wt, data = mtcars)
cat("\nSimple linear regression (mpg ~ weight):\n")
print(summary(model_simple))

# Multiple linear regression
model_multiple <- lm(mpg ~ wt + hp + cyl, data = mtcars)
cat("\nMultiple linear regression:\n")
print(summary(model_multiple))

# Model diagnostics
cat("\nChecking regression assumptions:\n")
par(mfrow = c(2, 2))
plot(model_multiple)
par(mfrow = c(1, 1))

# === Correlation ===

cat("\n=== Correlation Analysis ===\n")

# Pearson correlation
cor_test <- cor.test(mtcars$mpg, mtcars$wt)
cat("\nPearson correlation (mpg vs weight):\n")
print(cor_test)

# Correlation matrix
numeric_cols <- mtcars[, sapply(mtcars, is.numeric)]
cor_matrix <- cor(numeric_cols)
cat("\nCorrelation matrix:\n")
print(round(cor_matrix, 2))

# === Chi-Square Test ===

cat("\n=== Chi-Square Test ===\n")

# Create contingency table
table_data <- table(mtcars$cyl, mtcars$am)
cat("\nContingency table (cylinders vs transmission):\n")
print(table_data)

# Chi-square test
chi_test <- chisq.test(table_data)
cat("\nChi-square test:\n")
print(chi_test)

# === Non-parametric Tests ===

cat("\n=== Non-parametric Tests ===\n")

# Wilcoxon rank-sum test (Mann-Whitney U)
wilcox_test <- wilcox.test(auto, manual)
cat("\nWilcoxon rank-sum test:\n")
print(wilcox_test)

# Kruskal-Wallis test (non-parametric ANOVA)
kruskal_test <- kruskal.test(mpg ~ factor(cyl), data = mtcars)
cat("\nKruskal-Wallis test:\n")
print(kruskal_test)

cat("\nStatistical analysis complete!\n")
