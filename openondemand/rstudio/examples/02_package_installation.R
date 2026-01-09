# Package Installation Guide for RStudio on HPC
# This script shows how to install and manage R packages

cat("R Package Installation Guide\n")
cat("============================\n\n")

# Check current library paths
cat("Current library paths:\n")
print(.libPaths())

# Your user library should be first in the list
# Packages install here by default

# === Installing from CRAN ===

# Install single package
# install.packages("ggplot2")

# Install multiple packages
# install.packages(c("dplyr", "tidyr", "readr"))

# Install with dependencies
# install.packages("tidyverse", dependencies = TRUE)

# === Installing from Bioconductor ===

# First install BiocManager if not already installed
if (!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager")
}

# Install Bioconductor packages
# BiocManager::install("DESeq2")
# BiocManager::install(c("GenomicRanges", "SummarizedExperiment"))

# === Installing from GitHub ===

# First install devtools
# install.packages("devtools")

# Install from GitHub
# devtools::install_github("username/repository")

# === Checking installed packages ===

# List all installed packages
installed_pkgs <- installed.packages()[, c("Package", "Version")]
cat("\nTotal installed packages:", nrow(installed_pkgs), "\n")

# Check if specific package is installed
check_package <- function(pkg_name) {
  if (requireNamespace(pkg_name, quietly = TRUE)) {
    version <- as.character(packageVersion(pkg_name))
    cat(pkg_name, "is installed (version", version, ")\n")
    return(TRUE)
  } else {
    cat(pkg_name, "is NOT installed\n")
    return(FALSE)
  }
}

# Example usage
check_package("ggplot2")
check_package("dplyr")

# === Loading packages ===

# Load package
library(ggplot2)

# Load multiple packages
packages <- c("dplyr", "tidyr", "readr")
lapply(packages, library, character.only = TRUE)

# === Updating packages ===

# Update all packages (uncomment to run)
# update.packages(ask = FALSE)

# Update specific package
# update.packages("ggplot2")

# === Removing packages ===

# Remove a package (uncomment to run)
# remove.packages("package_name")

# === Useful package management tips ===

cat("\nUseful commands:\n")
cat("  installed.packages()  - List all installed packages\n")
cat("  old.packages()        - List packages that can be updated\n")
cat("  packageVersion('pkg') - Get package version\n")
cat("  citation('pkg')       - Get citation for package\n")
cat("  help(package='pkg')   - Get package help\n")

# === Session information ===
cat("\nCurrent R session information:\n")
sessionInfo()
