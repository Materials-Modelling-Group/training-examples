# Data Visualization with ggplot2
# Demonstrates creating publication-quality graphics

library(ggplot2)
library(dplyr)

cat("ggplot2 Visualization Examples\n")
cat("==============================\n\n")

# Use mtcars dataset for examples
data <- mtcars
data$cyl <- factor(data$cyl)  # Convert cylinders to factor
data$am <- factor(data$am, labels = c("Automatic", "Manual"))

# === Basic scatter plot ===

cat("Creating scatter plot...\n")
p1 <- ggplot(data, aes(x = wt, y = mpg)) +
  geom_point(aes(color = cyl), size = 3) +
  labs(
    title = "Fuel Efficiency vs Weight",
    x = "Weight (1000 lbs)",
    y = "Miles per Gallon",
    color = "Cylinders"
  ) +
  theme_minimal()

print(p1)

# === Line plot with smooth trend ===

cat("Creating line plot with trend...\n")
p2 <- ggplot(data, aes(x = wt, y = mpg)) +
  geom_point(aes(color = cyl)) +
  geom_smooth(method = "lm", se = TRUE, color = "blue") +
  labs(
    title = "MPG vs Weight with Linear Trend",
    x = "Weight",
    y = "MPG"
  ) +
  theme_bw()

print(p2)

# === Box plot ===

cat("Creating box plot...\n")
p3 <- ggplot(data, aes(x = cyl, y = mpg, fill = cyl)) +
  geom_boxplot() +
  labs(
    title = "MPG Distribution by Cylinder Count",
    x = "Number of Cylinders",
    y = "Miles per Gallon"
  ) +
  theme_classic() +
  theme(legend.position = "none")

print(p3)

# === Histogram ===

cat("Creating histogram...\n")
p4 <- ggplot(data, aes(x = mpg)) +
  geom_histogram(bins = 10, fill = "steelblue", color = "black") +
  labs(
    title = "Distribution of Fuel Efficiency",
    x = "Miles per Gallon",
    y = "Frequency"
  ) +
  theme_minimal()

print(p4)

# === Faceted plots ===

cat("Creating faceted plot...\n")
p5 <- ggplot(data, aes(x = wt, y = mpg)) +
  geom_point(aes(color = cyl)) +
  facet_wrap(~ am) +
  labs(
    title = "MPG vs Weight by Transmission Type",
    x = "Weight",
    y = "MPG"
  ) +
  theme_bw()

print(p5)

# === Bar plot ===

# Summarize data first
summary_data <- data %>%
  group_by(cyl) %>%
  summarise(
    mean_mpg = mean(mpg),
    sd_mpg = sd(mpg)
  )

cat("Creating bar plot...\n")
p6 <- ggplot(summary_data, aes(x = cyl, y = mean_mpg, fill = cyl)) +
  geom_bar(stat = "identity") +
  geom_errorbar(
    aes(ymin = mean_mpg - sd_mpg, ymax = mean_mpg + sd_mpg),
    width = 0.2
  ) +
  labs(
    title = "Average MPG by Cylinder Count",
    x = "Cylinders",
    y = "Mean MPG"
  ) +
  theme_minimal() +
  theme(legend.position = "none")

print(p6)

# === Saving plots ===

cat("\nSaving plots to files...\n")

# Save as PNG
# ggsave("plot1.png", p1, width = 8, height = 6, dpi = 300)

# Save as PDF (vector graphics)
# ggsave("plot1.pdf", p1, width = 8, height = 6)

# Save as SVG
# ggsave("plot1.svg", p1, width = 8, height = 6)

# Save multiple plots
# plots <- list(p1, p2, p3, p4, p5, p6)
# for (i in seq_along(plots)) {
#   ggsave(paste0("plot_", i, ".png"), plots[[i]], width = 8, height = 6)
# }

cat("\nVisualization examples complete!\n")
cat("Check the Plots pane to view all graphs\n")
