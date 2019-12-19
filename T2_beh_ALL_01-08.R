# training 2 - behavioural tests - data
# works when run line-by-line, not when knitting, due to potential plyr/dplyr conflict
library(broom)
library(dplyr)
library(ggplot2)
library(lme4)
library(lmerTest)
library(plyr)
library(readxl)
library(scales)
library(texreg)
###################
######### helper function
## http://www.cookbook-r.com/Graphs/Plotting_means_and_error_bars_(ggplot2)/#Helper%20functions
## Gives count, mean, standard deviation, standard error of the mean, and confidence interval (default 95%).
##   data: a data frame.
##   measurevar: the name of a column that contains the variable to be summariezed
##   groupvars: a vector containing names of columns that contain grouping variables
##   na.rm: a boolean that indicates whether to ignore NA's
##   conf.interval: the percent range of the confidence interval (default is 95%)
summarySE <-
  function(data = NULL,
           measurevar,
           groupvars = NULL,
           na.rm = FALSE,
           conf.interval = .95,
           .drop = TRUE) {
    # New version of length which can handle NA's: if na.rm==T, don't count them
    length2 <- function(x, na.rm = FALSE) {
      if (na.rm)
        sum(!is.na(x))
      else
        length(x)
    }
    
    # This does the summary. For each group's data frame, return a vector with
    # N, mean, and sd
    datac <- ddply(
      data,
      groupvars,
      .drop = .drop,
      .fun = function(xx, col) {
        c(
          N    = length2(xx[[col]], na.rm = na.rm),
          mean = mean(xx[[col]], na.rm = na.rm),
          sd   = s(xx[[col]], na.rm = na.rm)
        )
      },
      measurevar
    )
    
    # Rename the "mean" column
    datac <- plyr::rename(datac, c("mean" = measurevar))
    
    datac$se <-
      datac$sd / sqrt(datac$N)  # Calculate standard error of the mean
    
    # Confidence interval multiplier for standard error
    # Calculate t-statistic for confidence interval:
    # e.g., if conf.interval is .95, use .975 (above/below), and use df=N-1
    ciMult <- qt(conf.interval / 2 + .5, datac$N - 1)
    datac$ci <- datac$se * ciMult
    
    return(datac)
  }

##############
#setwd("E:\\ABR-Training2\\RESULTS\\Behavioral_Test")

t2_beh_raw <- read_xlsx("./Behavioral_Test/T2_beh_ALL_01-08.xlsx")

# summary of all responses - P3/post has 166 trials
t2_beh_raw %>% group_by(Day, Participant) %>% summarise(vol = n())
# identify sounds played too often: stimuli 6, 7, 8, 11, 12, 14 were played 11. the first occurence was removed.
t2_beh_raw %>%
  filter(Participant == "P03", Day == "Post") %>%
  group_by(Stimulus) %>%
  summarise(Vol = n())

# load the cleaned file
t2_beh <- read_excel("./Behavioral_Test/T2_beh_ALL_01-08_P03_cleaned.xlsx")
t2_beh %>% group_by(Day, Participant) %>% summarise(vol = n())

t2_beh$Day <- factor(t2_beh$Day, levels = c("Pre", "Post"))
t2_beh$Tone <- factor(t2_beh$Tone, levels = c("Rise", "Fall"))
str(t2_beh)

#
# # total trials - sanity check
ggplot(data = t2_beh, aes(Participant, Correct)) +
  geom_bar(stat = "identity", aes(fill = Participant)) +
  facet_grid(.~Day) +
  theme_bw()

ggplot(data = t2_beh, aes(Tone, Correct)) +
  geom_bar(stat = "identity", aes(fill = Tone)) +
  facet_grid(.~Day) +
  theme_bw()

ggplot(data = t2_beh, aes(Day, Correct)) +
  geom_bar(stat = "identity", aes(fill = Day)) +
  theme_bw()

###

# palettes
tones_palette <- c("olivedrab3", "orchid3")
# based on ggplot2 - 5 colours - Condition colours like on page 133
vocalisation_conditions_palette <- c("#00B0F6", "#A3A500")

# with error bars - participant
correct_by_participant <- summarySE(t2_beh,
                                    measurevar = "Correct",
                                    groupvars = c("Day", "Participant"))

# error bars represent standard error of the mean
ggplot(data = correct_by_participant, aes(Participant, Correct)) +
  geom_bar(stat = "identity", aes(fill = Participant)) +
  #coord_flip() +
  geom_errorbar(aes(ymin = Correct - se, ymax = Correct + se),
                size = .3,    # Thinner lines
                width = .2) +
  ylab("Correct responses") +
  scale_y_continuous(labels = percent) +
  facet_grid(~Day) +
  theme_bw()

# save as exp3_perceptual_correct.png
# 950x650

# with error bars - tone # tends to break when dplyr/plyr is loaded, needs ::
correct_by_tone <- summarySE(t2_beh,
                             measurevar = "Correct",
                             groupvars = c("Day", "Tone"))

# error bars represent standard error of the mean
# TODO add colours - like in figure 2.19 Exp1
ggplot(data = correct_by_tone, aes(Tone, Correct)) +
  geom_bar(stat = "identity", aes(fill = Tone)) +
  #coord_flip() +
  geom_errorbar(aes(ymin = Correct - se, ymax = Correct + se),
                size = .3,    # Thinner lines
                width = .2) +
  ylab("Correct responses") +
  scale_y_continuous(labels = percent) +
  scale_fill_manual(values = tones_palette) +
  facet_grid(~Day) +
  theme_bw() +
  theme(legend.position = "top")

# save
# save
#ggsave('/media/eub/MyPassport/ABR-Training2/Images/exp3_perceptual_tone_by_day.png',
#       width = 15, height = 10, units = "cm")

# ANOVA within-subjects
# http://www.cookbook-r.com/Statistical_analysis/ANOVA/

str(t2_beh)
# make a safety copy
t2_behA <- t2_beh
t2_behA$Participant <- as.factor(t2_behA$Participant)

# original: aov_model1 <- aov(Correct ~ Day*Tone + Error(Participant/Day), data = t2_behA)
aov_model1 <- aov(Correct ~ Day + Tone + Day*Tone + Error(Participant/Day), data = t2_behA)
summary(aov_model1)

# high level overview
t2_beh %>% group_by(Day) %>% summarise(PercCorrect = sum(Correct)/n(),
                                       Volume = sum(Correct)/8)

# simpler model
# adding "+ Error(Participant)" doesn't change the significance
aov_model2 <- aov(Correct ~ Day + Tone + Day*Tone, data = t2_behA)
summary(aov_model2)

model2_tidy <- tidy(aov_model2)
model2_tidy$hochberg <- p.adjust(model2_tidy$p.value, "hochberg")

#%%%%%%%%%%%%%%% CORRECTIONS %%%%%%%%%%%%%%%%%%%%%%%%
# GLMM
t2_behA$Stimulus <- as.factor(t2_behA$Stimulus)

# same as T1
# adding Simulus to RE or interaction in the FE doesn't change the result
# current formula used for consistency with the first training study  
glmmT2_beh0 <-
  glmer(Correct ~ Participant + Day + Tone +
       (1|Participant),
        family = "binomial",
        data = t2_behA)

summary(glmmT2_beh0)
anova(glmmT2_beh0)

# check the effect of day
glmmT2_beh1 <-
  glmer(Correct ~ Participant + Tone +
        (1|Participant),
        family = "binomial",
        data = t2_behA)
summary(glmmT2_beh1)
anova(glmmT2_beh1)

# check the effect of tone
glmmT2_beh2 <-
  glmer(Correct ~ Participant + Day +
        (1|Participant),
        family = "binomial",
        data = t2_behA)
summary(glmmT2_beh2)
anova(glmmT2_beh2)

# REPORT:
# Day is significant
anova(glmmT2_beh0, glmmT2_beh1)

# Tone is significant
anova(glmmT2_beh0, glmmT2_beh2)
