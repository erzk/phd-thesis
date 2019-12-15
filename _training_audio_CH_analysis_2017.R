# training study - audio CH 
library(BayesFactor)
library(car)
library(dplyr)
library(ggplot2)
library(ggpubr)
library(gridExtra)
library(lsr)
library(modelr)
library(texreg)
library(xtable)

# load
df <- read.csv("/media/eub/MyPassport/ABR-Training/RESULTS/Audio_CH/test_audio/both_150_300Hz_0.15sil.csv",
               stringsAsFactors = FALSE)

# rename columns
names(df)[names(df) == 'participant'] <- 'Native'
names(df)[names(df) == 'session'] <- 'Session'

clean_df <- df[complete.cases(df),]

# total utterances - complete cases
clean_df %>% group_by(Native) %>% count()

# cleaned - in the expected range
clean_df %>% filter(minimumPitch >= 150, maximumPitch <= 300) %>% count()
clean_df %>% filter(minimumPitch >= 150, maximumPitch <= 300) %>% group_by(Native) %>% count()

# trim
clean_df <- clean_df %>% filter(minimumPitch >= 150, maximumPitch <= 300)

# real duration
clean_df <- clean_df %>% mutate(RealDuration =  timeMinimumPitch - timeMaximumPitch)

# slope / range
# all references to 'slope' were replaced with 'range' as suggest by the reviewer
clean_df <- clean_df %>% mutate(Range = maximumPitch - minimumPitch)

# density: file duration
ggplot(data = clean_df, aes(x = duration, fill = Native)) +
  geom_density(alpha = 0.5) +
  xlim(0, 1.5) +
  xlab("Duration (s)") +
  ylab("Density") +
  theme_bw() +
  theme(legend.position = "top")

# save
# ggsave("/media/eub/MyPassport/ABR-Training/Images/exp2_audio_duration_distribution.png",
#        width = 4, height = 4)

# pitch duration
ggplot(data = clean_df, aes(x = RealDuration, fill = Native)) +
  geom_density(alpha = 0.5) +
  xlim(-0.5, 0.5) +
  xlab("Duration (s)") +
  ylab("Density") +
  theme_bw() +
  theme(legend.position = "top")

# save
# ggsave("/media/eub/MyPassport/ABR-Training/Images/exp2_audio_real_pitch_duration_distribution.png",
#        width = 4, height = 4)

# facets with violins
# ggviolin(clean_df, x = "Session", y = "RealDuration",
#           facet.by = "Native",
#           #panel.labs = list(condition = c("Shadowing", "Self-production")),
#           fill = "Session",
#           xlab = "Session", ylab = "Pitch duration (s)",
#           ylim = c(-0.5, 0.5),
#           add = "mean",
#           ggtheme = theme_bw())

# used in the thesis
# manual save, filename "exp2_audio_real_pitch_duration_boxplots_session.png"
# 650 x 578 px
ggboxplot(clean_df, x = "Session", y = "RealDuration",
         facet.by = "Native",
         #panel.labs = list(condition = c("Shadowing", "Self-production")),
         fill = "Session",
         xlab = "Session", ylab = "Pitch duration (s)",
         ylim = c(-0.4, 0.4),
         legend = "none",
         ggtheme = theme_bw())

# used in the thesis
# manual save, filename "exp2_audio_min_max_pitch_boxplots_by_session_participant.png"
# 750 x

# facets with boxplots
boxMin <- ggboxplot(clean_df, x = "Session", y = "minimumPitch",
                    facet.by = "Native",
                    #panel.labs = list(condition = c("Shadowing", "Self-production")),
                    fill = "Session",
                    xlab = "", ylab = "Minimum pitch (Hz)",
                    ylim = c(150, 300),
                    legend = "none",
                    ggtheme = theme_bw())
  #+ geom_smooth(method = "lm", se = FALSE, color = "red", aes(group = 1))

boxMax <- ggboxplot(clean_df, x = "Session", y = "maximumPitch",
                    facet.by = "Native",
                    #panel.labs = list(condition = c("Shadowing", "Self-production")),
                    fill = "Session",
                    xlab = "Session", ylab = "Maximum pitch (Hz)",
                    ylim = c(150, 300),
                    legend = "none",
                    ggtheme = theme_bw())
#+ theme(legend.position = "none")
#+ geom_smooth(method = "lm", se = FALSE, color = "red", aes(group = 1))

grid.arrange(boxMax, boxMin, ncol = 1)

# used in the thesis
# manual save, filename "exp2_audio_pitch_slope_boxplots_by_session_participant.png"
# 750 x 500
# slope chart
ggboxplot(clean_df, x = "Session", y = "Range",
          facet.by = "Native",
          #panel.labs = list(condition = c("Shadowing", "Self-production")),
          fill = "Session",
          xlab = "", ylab = "Range (Hz)",
          ylim = c(0, 150),
          legend = "none",
          ggtheme = theme_bw()) +
  geom_smooth(method = "lm", se = FALSE, color = "darkgrey", aes(group = 1))

ggsave("exp2_audio_pitch_slope_boxplots_by_session_participant.pdf",
       width = 6, height = 6)
################# INFERENTIAL STATS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# https://rpubs.com/ibecav/308410
df_16 <- clean_df %>% filter(Session %in% c(1, 6))
df_16$Session <- as.character(df_16$Session)

# Range ~ day and language
model1 <- aov(Range ~ Session + Native + Session*Native, data = df_16) #same as: Range ~ Session*Native
model2 <- aov(Range ~ Session, data = df_16)
model3 <- aov(Range ~ Native, data = df_16)
model4 <- aov(Range ~ Session*Native, data = df_16)

# descriptives
df_16 %>% group_by(Session) %>% summarise(Mean = mean(Range), Median = median(Range), SD = sd(Range))
df_16 %>% group_by(Native) %>% summarise(Mean = mean(Range), Median = median(Range), SD = sd(Range))
df_16 %>% group_by(Session, Native) %>% summarise(Mean = mean(Range), Median = median(Range), SD = sd(Range))

# check the RMSE
rmse(model1, df_16)
rmse(model2, df_16)
rmse(model3, df_16)
rmse(model4, df_16)
# model 1 and 4 are the same at 14.78502 vs  RMSE > 21 for model 2 and 3. I choose the simplest - model4

summary(model1)
summary(model4)

# change types
df_16$Native <- as.factor(df_16$Native)
df_16$Native <- as.character(df_16$Native)
# a qqplot showed the violation of normality - the distribution exceeds the central line

# post-hoc tests
# Two-way ANOVA with interaction effect = model1 is the same as model4
# http://www.sthda.com/english/wiki/two-way-anova-test-in-r
tukey_m1 <- TukeyHSD(model1, conf.level = 0.99)

# https://rpubs.com/ibecav/308410
par(oma = c(0,5,0,0)) # fits the factor names
# used in the thesis
# manual save, filename "exp2_audio_tukey_m1.png"
# 650 x 600
plot(tukey_m1, las = 1, col = "red")
# the largest difference is between the English participant



### Effect size
# https://rpubs.com/ibecav/308410
etaSquared(model1)

################ UNDERNEATH: not in the thesis - not used - tests

# check the assumptions
par(mfrow = c(1,1))
plot(model1)

par(mfrow = c(2,2))
plot(model1)

#########
# outliers detected in the plots = c(911, 1053, 3113, 4602)
# removing slopes over 110 to have less than 5000 records to run the shapiro.test
df_16_under110Hz_slope <- df_16 %>% filter(Range < 110)
model110 <- aov(Range ~ Session + Native + Session*Native, data = df_16_under110Hz_slope)

# Extract the residuals
aov_residuals <- residuals(object = model110)
# Run Shapiro-Wilk test
shapiro.test(x = aov_residuals )
# shapiro test shows that normality was violated so I should use ANOVA for unbalanced design (?)
##########

# unbalanced ANOVA - I think this should be run but then how to run Tukey's HSD? :/
# http://www.sthda.com/english/wiki/two-way-anova-test-in-r
model1unbal <- aov(Range ~ Session*Native, data = df_16)
m1un3 <- Anova(model1unbal, type = "III")

# tukey fails:
#tukey_m1un3 <- TukeyHSD(m1un3, conf.level = 0.99)


### bayesian anova
df_16$Native <- as.factor(df_16$Native)
df_16$Session <- as.factor(df_16$Session)

# TODO add a random factor
model4_bf <- anovaBF(Range ~ Session*Native, data = df_16)
summary(model4_bf)
# plot(model4_bf) # can't plot :/

##### other potential models - not necessary
# min
model5_min <- aov(minimumPitch ~ Session + Native + Session*Native, data = df_16)
summary(model5_min)

# max
model6_max <- aov(maximumPitch ~ Session + Native + Session*Native, data = df_16)
summary(model6_max)

### %%%%%%%%%%%%% 2019 correctins (December) LMMs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clean_df$Session <- as.factor(clean_df$Session)
clean_df$Native <- as.factor(clean_df$Native)
str(clean_df)

# audio Model 1 - min
tic()
min_lmm_m00_with_session <-
  lmer(minimumPitch ~ Native * Session +
         (1 + Session | Native),
       data = clean_df, REML = FALSE)
toc()

summary(min_lmm_m00_with_session)
aov_min <- anova(min_lmm_m00_with_session)
plot(ls_means(min_lmm_m00_with_session))

# audio Model 2 - max 2
tic()
max_lmm_m00_with_session <-
  lmer(maximumPitch ~ Native * Session +
         (1 + Session | Native),
       data = clean_df, REML = FALSE)
toc()

summary(max_lmm_m00_with_session)
aov_max <- anova(max_lmm_m00_with_session)
plot(ls_means(max_lmm_m00_with_session))

# latex
minmax_list <- list(min_lmm_m00_with_session, max_lmm_m00_with_session)
texreg(minmax_list, booktabs = TRUE, digits = 3)

# anovas
xtable(aov_min)
xtable(aov_max)
