#' ---
#' title: "PraatR Pitch Analysis Loop"
#' author: "Eryk Walczak"
#' ---

# Documentation: http://www.aaronalbin.com/praatr/tutorial.html
# loop through all the files in a directory
library("PraatR")
library("phonTools")

# define the participant/folder/output file name
participant <- "testLoop"
trial <- "01"

# output files are appended
outputFileName <- paste(participant, "_append", ".csv", sep="")
# output files are separate
# outputFileName <- paste(participant, "_", trial, ".csv", sep="")

# define output directory
dirOutput <- file.path("C:", "Users", "E", "Desktop", "test_audio")

# set the working directory
workingDirectory <- file.path("C:", "Users", "E", "Desktop", "test_audio", participant, trial)
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
quantileNumeric <- vector()
wavFilename <- vector()

# measure processing time
ptm <- proc.time()

# TO DO use a vector instead of the for loop
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
    quantileNumeric <- append(quantileNumeric, NA)
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
#     print(wavDuration)
    duration <- append(duration, wavDuration)
    # create the pitch track
    # http://www.fon.hum.uva.nl/praat/manual/Sound__To_Pitch___.html
    praat("To Pitch (ac)...", 
          arguments=list(0, # time step (s)
                         150, # pitch floor (Hz) - default 75
                         15, # max number of candidates
                         "no", # very accurate
                         0.15, # silence threshold - default 0.03
                         0.45, # voicing threshold
                         0.01, # octave cost
                         0.35, # octave-jump cost
                         0.14, # voiced/unvoiced cost 
                         300), # pitch ceiling (Hz) - default 600
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
#     print(minPitch)
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
#     print(maxPitch)
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
#     print(timeMinPitch)
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
#     print(timeMaxPitch)
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
    # quantileInt is a string 'nnn dB'. Here it's changed into a numeric.
    quantileInt <- as.numeric(
      # sub removes the last word
      sub(
        quantileInt, pattern = " [[:alpha:]]*$", replacement = ""
      )
    )
#     print(quantileInt)
    quantileNumeric <- append(quantileNumeric, quantileInt)
  }
  
}

results <- data.frame(wavFilename,
                      duration, 
                      minimumPitch, 
                      maximumPitch, 
                      timeMinimumPitch, 
                      timeMaximumPitch,
                      quantileNumeric,
                      participant,
                      trial,
                      stringsAsFactors = FALSE)
                      
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
# write.csv(results, file = file.path(dirOutput, outputFileName))
write.table(results, 
            file = file.path(dirOutput, outputFileName), 
            sep=",", 
            append = TRUE, 
            row.names = FALSE,
            # don't append column names if the file exists
            col.names=!file.exists(file.path
                                   (dirOutput, outputFileName)
                                   )
            )

# processing time
proc.time() - ptm

# Praat will not compute F0 values in the first or last 20 ms (or so) of each piece. 
# This is because the analysis requires a window of 40 ms (or so) for every pitch frame. 
