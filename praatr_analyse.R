#' ---
#' title: "Pitch data analysis"
#' author: "Eryk Walczak"
#' ---

library(dplyr)
library(ggplot2)
library(gridExtra)
library(pastecs)

# Load pitch data 
# set the working directory
workingDirectory <- file.path("C:", "Users", "E", "Desktop", "test_audio")
setwd(workingDirectory)

NatCh <- read.csv("all_natCH_pitch.csv")
NatEn <- read.csv("all_natEN_pitch.csv")

# count NAs
NAsCh <- length(which(is.na(NatCh$duration)))
NAsEn <- length(which(is.na(NatEn$duration)))

# print the table showing the number of NAs
NAsDF <- data.frame(nativeLanguage = c("Chinese", "English"), 
                 NAs = c(NAsCh, NAsEn))
print(NAsDF)

# remove NAs
cleanNatCh <- NatCh[complete.cases(NatCh),]
cleanNatEn <- NatEn[complete.cases(NatEn),]

# print out the summaries

# Chinese
summary(cleanNatCh)
stat.desc(cleanNatCh)

# English
summary(cleanNatEn)
stat.desc(cleanNatEn)

# merge both clean DFs
allCleanDF <- rbind(cleanNatCh, cleanNatEn) 
# TO DO: export to a csv

# duration plots - TO DO: ggplot, name,  , fill="red"
histDurCh <- qplot(duration, data=cleanNatCh, geom="histogram", binwidth = 0.05, xlim = c(0, 1.5), ylim = c(0, 1500))
histDurEn <- qplot(duration, data=cleanNatEn, geom="histogram", binwidth = 0.05, xlim = c(0, 1.5), ylim = c(0, 1500))

# overlaid histograms
ggplot(allCleanDF, aes(x=duration, fill=participant)) + 
  geom_histogram(binwidth=.05, alpha=.5, position="identity") + 
  xlim(0, 1.5)

# create a data frame - TO DO: uneven nrow
# durDF <- data.frame(nativeLanguage = factor(c("Chinese","English"), levels=c("Chinese","English")),
#                         durations = c(cleanNatCh$duration, cleanNatEn$duration))

grid.arrange(histDurCh, histDurEn, ncol=2)

# make line plots: min-max pitch
scatterMinMaxPitch <- 
  ggplot(allCleanDF, aes(x=minimumPitch, y=maximumPitch, color=participant)) + 
  geom_point(shape=1)

# duration based on the means of time of min-max pitch
durationPitchTimesCh <- 
  mean(cleanNatCh$timeMinimumPitch)-mean(cleanNatCh$timeMaximumPitch)

print(durationPitchTimesCh)

durationPitchTimesEn <- 
  mean(cleanNatEn$timeMinimumPitch)-mean(cleanNatEn$timeMaximumPitch)

print(durationPitchTimesEn)

# difference between duration and duration based on min-max pitch times
# Chinese
durDiffCh <- 
  mean(cleanNatCh$duration)-durationPitchTimesCh
# English
durDiffEn <- 
  mean(cleanNatEn$duration)-durationPitchTimesEn

# create a data frame
durDiffDF <- 
  data.frame(nativeLanguage = factor(c("Chinese","English"), levels=c("Chinese","English")),
                        diff_durations = c(durDiffCh, durDiffEn))

# make bar plots
ggplot(data=durDiffDF, aes(x=nativeLanguage, y=diff_durations, fill=nativeLanguage)) +
  geom_bar(colour="black", stat="identity") +
  guides(fill=FALSE) +
  xlab("Native language") + ylab("Difference between Duration and Duration of min/max pitch") +
  ggtitle("Duration differences")
# TO DO error bars http://docs.ggplot2.org/0.9.3.1/geom_errorbar.html

# transform into characters; use for data in DF without stringsAsFactors=F
cleanNatCh$session <- as.character(cleanNatCh$session)
cleanNatEn$session <- as.character(cleanNatEn$session)

# plot min/max pitch (smooth) - TO DO: how is 'smooth' calculated?
qplot(minimumPitch, maximumPitch, data = cleanNatCh, geom = c("point", "smooth"), colour = session) + 
  ggtitle("Pitch Chinese")
qplot(minimumPitch, maximumPitch, data = cleanNatEn, geom = c("point", "smooth"), colour = session) + 
  ggtitle("Pitch English")

# plot min/max pitch
plotPitchCh <- 
  ggplot(cleanNatCh, aes(minimumPitch, maximumPitch, color=session)) + 
  geom_point(shape=1) +
  labs(title="Native Chinese")

plotPitchEn <-
  ggplot(cleanNatEn, aes(minimumPitch, maximumPitch, color=session)) + 
  geom_point(shape=1) +
  labs(title="Native English")
#   qplot(minimumPitch, maximumPitch, data = cleanNatEn, colour = session) + 
#   ggtitle("Pitch English")

grid.arrange(plotPitchCh, plotPitchEn, ncol=2)

# boxplots
boxMinC <- 
  qplot(session, minimumPitch, data = cleanNatCh, geom="boxplot", colour = session, ylim=c(0,350)) + 
  ggtitle("Minimum pitch Chinese") +
  theme(legend.position="none")
boxMaxC <- 
  qplot(session, maximumPitch, data = cleanNatCh, geom="boxplot", colour = session, ylim=c(0,350)) + 
  ggtitle("Maximum pitch Chinese") +
  theme(legend.position="none")

boxMinE <- 
  qplot(session, minimumPitch, data = cleanNatEn, geom="boxplot", colour = session, ylim=c(0,350)) + 
  ggtitle("Minimum pitch English") +
  theme(legend.position="none")
boxMaxE <- 
  qplot(session, maximumPitch, data = cleanNatEn, geom="boxplot", colour = session, ylim=c(0,350)) + 
  ggtitle("Maximum pitch English") +
  theme(legend.position="none")

# print out
# png("foo.png")
grid.arrange(boxMinC, boxMinE, boxMaxC, boxMaxE, ncol=2)
# dev.off()
