# Training study
# Alvin2 behavioural results 

library(ggpubr)
library(readxl)
library(scales)

# show ggplot2 colours
show_col(hue_pal()(2))

# df <- read_excel("E:\\ABR-Training\\RESULTS\\Behavioural_Alvin2\\training_both_alvin2_results_cleaned.xlsx") - 1000 x 500
df <- read_excel("/media/eub/MyPassport/ABR-Training/RESULTS/Behavioural_Alvin2/training_both_alvin2_results_cleaned.xlsx")

# filename: "exp2_training_tone_discrimination.png"
# png("/media/eub/MyPassport/ABR-Training/Images/exp2_training_tone_discrimination.png",
#     width = 1200, height = 600, units = "px")

ggline(df, x = "Session", y = "Correct",
       color = "Native",
       palette = c("#00BFC4", "#F8766D"),
       facet.by = "Tone",
       add = "mean") + 
  scale_y_continuous(labels = percent) + 
  labs(title = "Performance in tone discrimination tests",
       x = "Session", y = "Correct responses")

#dev.off()

# plot discontinuous line
df_blank2 <-
  structure(
    list(
      Stimulus = c(NA, NA),
      Button = c(NA, NA),
      Time = c(NA, NA),
      `T/F_even/odd` = c(NA, NA),
      Tone = c("Fall", "Rise"),
      Result = c(NA, NA),
      Correct = c(NA, NA),
      Session = c(2, 2),
      Native = c("English", "English")
    ),
    row.names = c(NA,-2L),
    class = c("tbl_df",
              "tbl", "data.frame"))
df_with_blank <- bind_rows(df, df_blank2)

# use in the thesis (after correction)
# shows discontinuity in English participant's data
ggline(df_with_blank, x = "Session", y = "Correct",
       color = "Native",
       palette = c("#00BFC4", "#F8766D"),
       facet.by = "Tone",
       add = "mean") + 
  scale_y_continuous(labels = percent) + 
  labs(title = "Performance in tone discrimination tests",
       x = "Session", y = "Correct responses")

# export
ggsave("exp2_training_tone_discrimination.pdf",
       width = 6, height = 4)

### Anova
library(dplyr)

model_beh <- aov(Correct ~ Tone*Session,
                 df %>% filter(Native == "English"))
summary(model_beh)
plot(model_beh)

# descriptives
df %>% filter(Native == "English") %>% group_by(Tone) %>% summarise(mean(Correct))
df %>% filter(Native == "English") %>% group_by(Tone, Session) %>% summarise(mean(Correct))
