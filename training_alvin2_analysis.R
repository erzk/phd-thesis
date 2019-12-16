# Training study
# Alvin2 behavioural results 

library(ggpubr)
library(readxl)
library(scales)
library(dplyr)
library(lme4)
# show ggplot2 colours
show_col(hue_pal()(2))

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
#ggsave("exp2_training_tone_discrimination.pdf",
#       width = 6, height = 4)

### Anova
model_beh <- aov(Correct ~ Tone*Session,
                 df %>% filter(Native == "English"))
summary(model_beh)
plot(model_beh)

# descriptives
df %>% filter(Native == "English") %>% group_by(Tone) %>% summarise(mean(Correct))
df %>% filter(Native == "English") %>% group_by(Tone, Session) %>% summarise(mean(Correct))

# GLMM
df_with_blank$Native <- as.factor(df_with_blank$Native)
df_with_blank$Tone <- as.factor(df_with_blank$Tone)
df_with_blank$Session <- as.factor(df_with_blank$Session)
df_with_blank$Stimulus <- as.factor(df_with_blank$Stimulus)

# fit the models
library(lmerTest)

t1_beh_m1 <-
  glmer(Correct ~ Native + Session + Tone +
          (1 | Native),
        #(1 + Stimulus | Native) # would not converge
        family = "binomial",
        data = df_with_blank %>% filter(Session != "2"))

summary(t1_beh_m1)
anova(t1_beh_m1)

# model 2
t1_beh_m2 <-
  glmer(Correct ~ Native + Session +
          (1 | Native),
        family = "binomial",
        data = df_with_blank %>% filter(Session != "2"))

# model 3
t1_beh_m3 <-
  glmer(Correct ~ Native + Tone +
          (1 | Native),
        family = "binomial",
        data = df_with_blank %>% filter(Session != "2"))

summary(t1_beh_m3)
anova(t1_beh_m3)

# compare two models
anova(t1_beh_m1, t1_beh_m2) # tone
anova(t1_beh_m1, t1_beh_m3) # session
