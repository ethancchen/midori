# Load necessary libraries
library(tidyverse)
library(stringr)

# Read the CSV file with explicit encoding specification
file_path <- "midori/csv/AI EarthHack Dataset.csv"
init_data <- read.csv(file_path, stringsAsFactors = FALSE, fileEncoding = "UTF-8")

# Process the data, removing short problem and solutions.
result_data <- init_data %>%
  mutate(solution = iconv(solution, to = "UTF-8", sub = "byte"),  # Convert to UTF-8
         res_sent_cnt = sapply(str_extract_all(solution, "[^.!?]+[.!?]"), length),
         r_char_cnt = sapply(solution, nchar),
         p_char_cnt = sapply(problem, nchar)) %>%
  filter((res_sent_cnt > 10 | r_char_cnt >= 250) & p_char_cnt > 42) %>%
  select(c(problem, id, solution))

view(result_data)

# Write the processed data to a new CSV file
write.csv(result_data, "clean_data.csv", row.names = FALSE)
