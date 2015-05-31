#' ---
#' title: "PraatR - Get mean pitch"
#' author: "Eryk Walczak"
#' ---

# Get mean pitch and duration
# Frequency altered feedback

# PraatR documentation: http://www.aaronalbin.com/praatr/tutorial.html
# loop through all the files in a directory
library("PraatR")
library("phonTools")

# define the partcipant/folder/output file name
participant <- "NAME"
condition <- "FAF" # frequency altered feedback
# condition <- "Speech" # own speech 
shift.direction <- "DOWN"

# output files are appended
# outputFileName <- paste("NAME", "_VALUES", ".csv", sep="")
# output files are separate
outputFileName <- paste(
  participant, "_", condition, "_", shift.direction, ".csv", 
  sep=""
  )

# define output directory
# file.path makes the path OS-agnostic
dirOutput <- file.path("C:", "Users", "E", "Desktop", "Chop", participant, condition)

# set the working directory
workingDirectory <- file.path(
  "C:", "Users", "E", "Desktop", "Chop", participant, condition, shift.direction
  )
setwd(workingDirectory)

# define a function to paste dir and filename
FullPath <- function(FileName){ 
  return( paste(workingDirectory, "/", FileName, sep="") ) 
}

# find all wav files in the working directory
filenames <- list.files(path = workingDirectory, pattern = "*.wav$")

# create empty vectors
duration <- vector()
meanPitch <- vector()
wavFilename <- vector()

# TODO: vectorise to increase the speed
for (i in filenames) {
  # Try the wavFile for errors (e.g. empty wav file)
  tryit <- try(wavFile <- loadsound(i))
  if(inherits(tryit, "try-error")){
    print(paste("Error in", i))
    # uncomment the lines below to add NAs to the data frame
    wavFilename <- append(wavFilename, i)
    duration <- append(duration, NA)
    meanPitch <- append(meanPitch, NA)
  } else {
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
                         50, # pitch floor (Hz) - default 75
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
    mnPitch <- as.numeric(praat("Get mean...", 
                                 arguments=list(0, # time range (s) start (0 = all)
                                                0, # time range (s) end (0 = all)
                                                "Hertz"), # unit
                                 input=FullPath("pitch_track"), 
                                 simplify=TRUE
    )
    )
    #     print(mnPitch)
    meanPitch <- append(meanPitch, mnPitch)
  }
  
}

results <- data.frame(wavFilename,
                      duration, 
                      meanPitch, 
                      participant,
                      condition,
                      shift.direction,
                      stringsAsFactors = FALSE)

# save to a csv
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
