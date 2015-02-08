#' ---
#' title: "Pitch data analysis"
#' author: "Eryk Walczak"
#' ---

library(ggplot2)
library(gridExtra)

# Load pitch data 
# set the working directory
workingDirectory <- file.path("C:", "Users", "E", "Desktop", "test_audio")
setwd(workingDirectory)

NatCh <- read.csv("all_natCH_pitch.csv")
NatEn <- read.csv("all_natEN_pitch.csv")

# TO DO(?): merge two DFs?

# TO DO: count NAs/ make histograms

# remove NAs
cleanNatCh <- NatCh[complete.cases(NatCh),]
cleanNatEn <- NatEn[complete.cases(NatEn),]

# print out the summary
summary(cleanNatCh)
summary(cleanNatEn)

# duration based on the means of time of min-max pitch
durationPitchTimesCh <- mean(cleanNatCh$timeMinimumPitch)-mean(cleanNatCh$timeMaximumPitch)
print(durationPitchTimesCh)

durationPitchTimesEn <- mean(cleanNatEn$timeMinimumPitch)-mean(cleanNatEn$timeMaximumPitch)
print(durationPitchTimesEn)

# difference between duration and duration of pitch times
# Ch
mean(cleanNatCh$duration)-durationPitchTimesCh
# En
mean(cleanNatEn$duration)-durationPitchTimesEn

# transform into characters; use for data in DF without stringsAsFactors=F
cleanNatCh$trial <- as.character(cleanNatCh$trial)
cleanNatEn$trial <- as.character(cleanNatEn$trial)

# plot min/max pitch
plot1C <- 
  qplot(minimumPitch, maximumPitch, data = cleanNatCh, colour = trial) + 
  ggtitle("Pitch Chinese")

plot1E <- 
  qplot(minimumPitch, maximumPitch, data = cleanNatEn, colour = trial) + 
  ggtitle("Pitch English")

grid.arrange(plot1C, plot1E, ncol=2)

# boxplots
boxMinC <- 
  qplot(trial, minimumPitch, data = cleanNatCh, geom="boxplot", colour = trial, ylim=c(0,600)) + 
  ggtitle("Minimum pitch Chinese")
boxMaxC <- 
  qplot(trial, maximumPitch, data = cleanNatCh, geom="boxplot", colour = trial, ylim=c(0,600)) + 
  ggtitle("Maximum pitch Chinese")

boxMinE <- 
  qplot(trial, minimumPitch, data = cleanNatEn, geom="boxplot", colour = trial, ylim=c(0,600)) + 
  ggtitle("Minimum pitch English")
boxMaxE <- 
  qplot(trial, maximumPitch, data = cleanNatEn, geom="boxplot", colour = trial, ylim=c(0,600)) + 
  ggtitle("Maximum pitch English")

# print out
# png("foo.png")
grid.arrange(boxMinC, boxMinE, boxMaxC, boxMaxE, ncol=2)
# dev.off()
