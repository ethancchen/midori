# Load necessary libraries
library(tidyverse)
library(stringr)

setwd("midori")
# Read the CSV file with explicit encoding specification
file_path <- "csv/AI EarthHack Dataset.csv"
init_data <- read.csv(file_path, stringsAsFactors = FALSE, fileEncoding = "UTF-8")

# Process the data, removing short problem and solutions.
result_data <- init_data %>%
  mutate(solution = iconv(solution, to = "UTF-8", sub = "byte"),  # Convert to UTF-8
         res_sent_cnt = sapply(str_extract_all(solution, "[^.!?]+[.!?]"), length),
         r_char_cnt = sapply(solution, nchar),
         p_char_cnt = sapply(problem, nchar)) %>%
  filter((res_sent_cnt > 10 | r_char_cnt >= 250) & p_char_cnt > 42)
  #select(c(problem, id, solution))

result_data |> max(result_data$r_char_cnt)


view(result_data)

# Write the processed data to a new CSV file.
write.csv(result_data, "clean_data.csv", row.names = FALSE)


# Create random data.
size <- 1000
industry <- c("Manufacturing", "Apparel", "Other")
ten_R <- c("Refuse", "Rethink", "Reduce", "Reuse",
           "Repair", "Refurbish", "Remanufacture",
           "Repurpose", "Recycle", "Recover")
area_focus <- c("Climate Change", "Biodiversity Loss",
                "Deforestation", "Air Pollution", "Water Pollution",
                "Plastic Pollution", "Resource Depletion",
                "Ocean Acidification", "Waste Management", "Land Degradation",
                "Loss of Freshwater Resources")
applicable <- c("Yes", "No")
heavy_investment <- c("Yes", "No", "Not Known")
monetary_benefits <- c("Yes", "No", "Not Known")
scalable <- c("Yes", "No", "Not Known")
payback_period <- c("Yes", "No", "Not Known")

rand_industry <- sample(industry, size, replace = T)
rand_ten_R <- sample(ten_R, size, replace = T)
rand_area_focus <- sample(area_focus, size, replace = T)
rand_applicable <- sample(applicable, size, replace = T)
rand_heavy_investment <- sample(heavy_investment, size, replace = T)
rand_monetary_benefits <- sample(monetary_benefits, size, replace = T)
rand_scalable <- sample(scalable, size, replace = T)
rand_payback_period <- sample(scalable, size, replace = T)

rand_response_df <- data.frame(rand_industry, rand_ten_R, rand_area_focus,
           rand_applicable, rand_heavy_investment, rand_monetary_benefits,
           rand_scalable, rand_payback_period)
colnames(rand_response_df) = c("industry", "ten_R", "area_focus",
                               "applicable", "heavy_investment", "monetary_benefits",
                               "scalable", "payback_period")
write.csv(rand_response_df, "random_response_data_frame.csv", row.names = FALSE)
