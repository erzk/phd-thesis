library(magrittr)

# set the working directory
workingDirectory <- file.path("C:", "Users", "E", "Desktop", "test_FFRs", "FFRs")
setwd(workingDirectory)

perc <- file.path("C:", "Users", "E", "Desktop", "test_FFRs", "FFRs", "70_2000", "D_perc")

filenames <- list.files(path = perc, pattern = "*.txt$")

for (i in filenames) {
  print(i)
    scan(paste(perc, "/", i, sep="")) %>%
    ts(., start=c(-49,350), frequency=16.384) %>%
    plot(., ylab="Amplitude (μV)", ylim=c(-2,2))
}
