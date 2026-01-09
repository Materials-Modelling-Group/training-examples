# Loading and Exploring Data in R
# Demonstrates various methods for reading data on HPC cluster

library(readr)      # Fast CSV reading
library(data.table) # Very fast for large data
library(haven)      # SPSS, Stata, SAS files

cat("Data Loading Examples\n")
cat("====================\n\n")

# === Reading CSV files ===

# Method 1: Base R
# data1 <- read.csv("/home/username/data/dataset.csv")

# Method 2: readr (tidyverse) - faster and better defaults
# data2 <- read_csv("/home/username/data/dataset.csv")

# Method 3: data.table - fastest for very large files
# data3 <- fread("/home/username/data/dataset.csv")

# === Reading from scratch directory (faster I/O) ===

# scratch_path <- "/scratch/username/large_dataset.csv"
# large_data <- fread(scratch_path)

# === Reading Excel files ===

# Install: install.packages("readxl")
# library(readxl)
# excel_data <- read_excel("/home/username/data/data.xlsx", sheet = 1)

# === Reading from URLs ===

# url <- "https://example.com/data.csv"
# web_data <- read_csv(url)

# === Reading specific columns ===

# Only read specific columns (saves memory)
# data_subset <- fread("file.csv", select = c("col1", "col2", "col3"))

# === Reading with custom options ===

# Custom delimiter, missing values, etc.
# custom_data <- read_csv(
#   "file.csv",
#   delim = ";",
#   na = c("", "NA", "missing"),
#   col_types = cols(
#     id = col_integer(),
#     date = col_date(format = "%Y-%m-%d"),
#     value = col_double()
#   )
# )

# === Reading multiple files ===

# Read all CSV files in a directory
# library(purrr)
# files <- list.files("/home/username/data", pattern = "*.csv", full.names = TRUE)
# all_data <- map_dfr(files, read_csv)

# === Example with built-in data ===

# Use mtcars dataset for demonstration
data <- mtcars
cat("\nLoaded mtcars dataset\n")
cat("Rows:", nrow(data), "\n")
cat("Columns:", ncol(data), "\n\n")

# === Initial data exploration ===

cat("Data Structure:\n")
str(data)

cat("\nFirst few rows:\n")
print(head(data))

cat("\nSummary statistics:\n")
print(summary(data))

cat("\nColumn names:\n")
print(names(data))

# === Checking for missing values ===

cat("\nMissing values per column:\n")
missing_counts <- colSums(is.na(data))
print(missing_counts)

cat("\nTotal missing values:", sum(is.na(data)), "\n")

# === Data dimensions ===

cat("\nDataset dimensions:\n")
cat("  Rows:", nrow(data), "\n")
cat("  Columns:", ncol(data), "\n")
cat("  Total cells:", nrow(data) * ncol(data), "\n")

# === Quick data preview ===

cat("\nColumn types:\n")
print(sapply(data, class))

cat("\nNumeric column summary:\n")
numeric_cols <- sapply(data, is.numeric)
print(summary(data[, numeric_cols]))

# === Saving data ===

# Save as RDS (R binary format - preserves data types)
# saveRDS(data, "/home/username/data_processed.rds")

# Read RDS file
# data <- readRDS("/home/username/data_processed.rds")

# Save as CSV
# write_csv(data, "/home/username/data_processed.csv")

# Save for Stata, SPSS, SAS
# library(haven)
# write_dta(data, "data.dta")  # Stata
# write_sav(data, "data.sav")  # SPSS
# write_sas(data, "data.sas7bdat")  # SAS

cat("\nData loading complete!\n")
