# create a script that calculates the averages and plots them

# set the working directory
workingDirectory <- file.path("C:", "Users", "E", "Desktop", "test_FFRs", "FFRs")
setwd(workingDirectory)

perc <- file.path("C:", "Users", "E", "Desktop", "test_FFRs", "FFRs", "70_2000", "D_perc")

#file_list <- list.files(perc)
participant_perc1 <- ts(scan(paste(perc, "/", "01-participant_-perc_rerefEXG2_70to2000_epoch(-49to350)_average.txt", sep=""))) 
participant_perc2 <- ts(scan(paste(perc, "/", "02-participant_-perc_rerefEXG2_70to2000_epoch(-49to350)_average.txt", sep=""))) 
participant_perc3 <- ts(scan(paste(perc, "/", "03-participant_-perc_rerefEXG2_70to2000_epoch(-49to350)_average.txt", sep=""))) 

avg_participant_Perc70 <- plot(ts((participant_perc1 + participant_perc2 + participant_perc3)/3))
