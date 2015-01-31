#' ---
#' title: "PraatR Pitch Loop"
#' author: "Eryk Walczak"
#' date: "January 29th, 2015"
#' ---

# Documentation: http://www.aaronalbin.com/praatr/tutorial.html
# loop through all the files in a directory
library("PraatR")
library("phonTools")

participant <- "NAME"
trial <- "01"
outputFileName <- paste(participant, "_", trial, ".csv", sep="")

workingDirectory <- "C:/Users/E/Desktop/test_audio/NAME/01"
setwd(workingDirectory)
# define a function to paste dir and filename
FullPath <- function(FileName){ return( paste(workingDirectory, "/", FileName, sep="") ) }

# find all wav files
filenames <- list.files(path = workingDirectory, pattern = "*.wav$")

# create anempty vector
duration <- vector()
minimumPitch <- vector()
maximumPitch <- vector()

for (i in filenames) {
  wavFile <- loadsound(i)
  # create plots
  plot(wavFile)
  #pitchtrack (wavFile)
  spectrogram (wavFile)
  pitchtrack (wavFile, addtospect = TRUE)
  wavDuration <- as.numeric( praat("Get total duration", input=FullPath(i), simplify=TRUE ) )
  print(wavDuration)
  duration <- append(duration, wavDuration)
  # create the pitch track
  praat("To Pitch...", arguments=list(0, 75, 600), input=FullPath(i), output=FullPath("pitch_track"), overwrite=TRUE)
  # get the minimum pitch
  minPitch <- as.numeric(praat("Get minimum...", arguments=list(0, 0, "Hertz", "Parabolic"), input=FullPath("pitch_track"), simplify=TRUE))
  print(minPitch)
  minimumPitch <- append(minimumPitch, minPitch)
  # get the maximum pitch
  maxPitch <- as.numeric(praat("Get maximum...", arguments=list(0, 0, "Hertz", "Parabolic"), input=FullPath("pitch_track"), simplify=TRUE))
  print(maxPitch)
  maximumPitch <- append(maximumPitch, maxPitch)
}

results <- data.frame(duration, minimumPitch, maximumPitch)
# print out the summary
summary(results)

# save to a csv
write.csv(results, file = outputFileName)

# TO DO: Add tryCatch()
# crashes at 06-723 - blank file
# Error in ts(sound, frequency = fs, start = 0) : 
#   'ts' object must have one or more observations
# In addition: There were 50 or more warnings (use warnings() to see the first 50)
