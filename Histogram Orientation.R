survey_2023_data <- read.csv("2023-06-13-survey.csv")
num_survey_results <- nrow(survey_2023_data)
hist(survey_2023_data$RAM..in.GB., col = "cadetblue", border = "darkslategray", xlab = "RAM (in GB)", ylab = "Count of Students' Computers", ylim = c(0, num_survey_results), main = "Computer Hardware Survey Results June 2023", labels = TRUE)

     