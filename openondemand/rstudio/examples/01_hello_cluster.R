# Hello Cluster - First R Script on KENET HPC
# This script demonstrates basic R commands and cluster information

cat("=" %R% rep("=", 60) %R% "\n")
cat("Hello from KENET HPC Cluster!\n")
cat("=" %R% rep("=", 60) %R% "\n\n")

# System Information
cat("System Information:\n")
cat("  R Version:", R.version.string, "\n")
cat("  Platform:", R.version$platform, "\n")
cat("  Hostname:", Sys.info()["nodename"], "\n")
cat("  OS:", Sys.info()["sysname"], Sys.info()["release"], "\n")

# User Information
cat("\nUser Information:\n")
cat("  Username:", Sys.info()["user"], "\n")
cat("  Home Directory:", Sys.getenv("HOME"), "\n")
cat("  Working Directory:", getwd(), "\n")

# Date and Time
cat("\nCurrent Time:", format(Sys.time(), "%Y-%m-%d %H:%M:%S"), "\n")

# Available CPU Cores
cat("\nComputational Resources:\n")
cat("  Available CPU Cores:", parallel::detectCores(), "\n")

# Memory Information
if (require(pryr, quietly = TRUE)) {
  cat("  Available Memory:", pryr::mem_used() / 1e9, "GB used\n")
} else {
  cat("  Install 'pryr' package for memory information\n")
}

# Check for common packages
cat("\nChecking installed packages:\n")
packages_to_check <- c("tidyverse", "ggplot2", "dplyr", "readr", 
                       "data.table", "rmarkdown", "knitr")

for (pkg in packages_to_check) {
  if (requireNamespace(pkg, quietly = TRUE)) {
    version <- as.character(packageVersion(pkg))
    cat("  ✓", pkg, version, "\n")
  } else {
    cat("  ✗", pkg, "not installed\n")
  }
}

# Simple calculation
cat("\nSimple Calculation:\n")
numbers <- 1:100
cat("  Sum of 1 to 100:", sum(numbers), "\n")
cat("  Mean:", mean(numbers), "\n")
cat("  Standard Deviation:", sd(numbers), "\n")

cat("\n" %R% rep("=", 60) %R% "\n")
cat("Script completed successfully!\n")
cat("=" %R% rep("=", 60) %R% "\n")
