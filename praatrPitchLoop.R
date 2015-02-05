#' ---
#' title: "PraatR Pitch Loop"
#' author: "Eryk Walczak"
#' date: "February 5th, 2015"
#' ---

# Documentation: http://www.aaronalbin.com/praatr/tutorial.html
# loop through all the files in a directory to extract duration, minimum/maximum pitch values, save to a csv
library("PraatR")
library("phonTools")

participant <- "NAME"
trial <- "01"
outputFileName <- paste(participant, "_", trial, ".csv", sep="")

workingDirectory <- "C:/Users/E/Desktop/test_audio/NAME/01"
setwd(workingDirectory)
# define a function to paste dir and filename
FullPath <- function(FileName){ 
  return( paste(workingDirectory, "/", FileName, sep="") ) 
}

# find all wav files
filenames <- list.files(path = workingDirectory, pattern = "*.wav$")

# create empty vectors
duration <- vector()
minimumPitch <- vector()
maximumPitch <- vector()
timeMinimumPitch <- vector()
timeMaximumPitch <- vector()
quantileInteger <- vector()
wavFilename <- vector()

for (i in filenames) {
  # Try the wavFile for errors (e.g. empty wav file)
  tryit <- try(wavFile <- loadsound(i))
  if(inherits(tryit, "try-error")){
    print(paste("Error in", i))
    # uncomment the lines below to add NAs to the data frame
    wavFilename <- append(wavFilename, i)
    duration <- append(duration, NA)
    minimumPitch <- append(minimumPitch, NA)
    maximumPitch <- append(maximumPitch, NA)
    timeMinimumPitch <- append(timeMinimumPitch, NA)
    timeMaximumPitch <- append(timeMaximumPitch, NA)
    quantileInteger <- append(quantileInteger, NA)
  } else {
    # create plots
#     plot(wavFile)
#     #pitchtrack (wavFile)
#     spectrogram (wavFile)
#     pitchtrack (wavFile, addtospect = TRUE)
    # save the file name
    wavFilename <- append(wavFilename, i)
    wavDuration <- as.numeric(praat("Get total duration", 
                                    input=FullPath(i), 
                                    simplify=TRUE 
    ) 
    )
    print(wavDuration)
    duration <- append(duration, wavDuration)
    # create the pitch track
    # http://www.fon.hum.uva.nl/praat/manual/Sound__To_Pitch___.html
    praat("To Pitch (ac)...", 
          arguments=list(0, # time step (s)
                         75, # pitch floor (Hz)
                         15, # max number of candidates
                         "no", # very accurate
                         0.03, # silence threshold
                         0.45, # voicing threshold
                         0.01, # octave cost
                         0.35, # octave-jump cost
                         0.14, # voiced/unvoiced cost 
                         600), # pitch ceiling (Hz)
          input=FullPath(i), 
          output=FullPath("pitch_track"), 
          overwrite=TRUE
    )
    # get the minimum pitch
    minPitch <- as.numeric(praat("Get minimum...", 
                                 arguments=list(0, # time range (s) start (0 = all)
                                                0, # time range (s) end (0 = all)
                                                "Hertz", # unit
                                                "Parabolic"), # interpolation
                                 input=FullPath("pitch_track"), 
                                 simplify=TRUE
    )
    )
    print(minPitch)
    minimumPitch <- append(minimumPitch, minPitch)
    # get the maximum pitch
    maxPitch <- as.numeric(praat("Get maximum...", 
                                 arguments=list(0, 
                                                0, 
                                                "Hertz", 
                                                "Parabolic"), 
                                 input=FullPath("pitch_track"), 
                                 simplify=TRUE
    )
    )
    print(maxPitch)
    maximumPitch <- append(maximumPitch, maxPitch)
    # get the time of minimum pitch
    timeMinPitch <- as.numeric(praat("Get time of minimum...", 
                                     arguments=list(0, # time range (s) start (0 = all)
                                                    0, # time range (s) end (0 = all)
                                                    "Hertz", # unit
                                                    "Parabolic"), # interpolation
                                     input=FullPath("pitch_track"), 
                                     simplify=TRUE
    )
    )
    print(timeMinPitch)
    timeMinimumPitch <- append(timeMinimumPitch, timeMinPitch)
    # get the time of maximum pitch
    timeMaxPitch <- as.numeric(praat("Get time of maximum...", 
                                     arguments=list(0, 
                                                    0, 
                                                    "Hertz", 
                                                    "Parabolic"), 
                                     input=FullPath("pitch_track"), 
                                     simplify=TRUE
    )
    )
    print(timeMaxPitch)
    timeMaximumPitch <- append(timeMaximumPitch, timeMaxPitch)
    # create the intensity
    praat("To Intensity...", 
          list(100, # minimum pitch (Hz)
               0, # time step (s)
               "yes"), # subtract mean
          input=FullPath(i), 
          output = FullPath("intensity"), 
          overwrite=TRUE
    )
    # get 25th quantile
    quantileInt <- praat("Get quantile...", 
                         list(0, # time range (s) start 
                              0, # time range (s) end
                              0.25), # quantile (0-1)
                         input=FullPath("intensity")
    )
    # quantileInt is a string 'nnn dB'. Here it's changed into numeric.
    quantileInt <- as.numeric(
      #sub removes the last word
      sub(
        quantileInt, pattern = " [[:alpha:]]*$", replacement = ""
      )
    )
    print(quantileInt)
    quantileInteger <- append(quantileInteger, quantileInt)
  }
  
}

results <- data.frame(wavFilename,
                      duration, 
                      minimumPitch, 
                      maximumPitch, 
                      timeMinimumPitch, 
                      timeMaximumPitch,
                      quantileInteger,
                      participant,
                      trial)

# remove NAs
cleanResults <- results[complete.cases(results),]

# print out the summary
summary(cleanResults)

# duration based on the means of time of min-max pitch
durationPitchTimes <- mean(cleanResults$timeMinimumPitch)-mean(cleanResults$timeMaximumPitch)
print(durationPitchTimes)

# difference between duration and duration of pitch times
mean(cleanResults$duration)-durationPitchTimes

# save to a csv
write.csv(results, file = outputFileName)
