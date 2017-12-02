txt2praat <- function(x, filename) {
  # Appends the Praat header to enable txt vector to be read in Praat.
  #
  # Args:
  #   x: A path to the txt file (vector) that the header attached will be attached to.
  #   Example:
  #   >x <- file.choose()
  #
  #   filename: Optional argument specifying the output file name
  #
  # Returns:
  #   Text file that can be loaded into Praat.
  
  # assign the output file name
  if(missing(filename)) {
    # use the original file name
    filename <- basename(file.path(x))
  } else {
    filename <- paste(deparse(substitute(filename)),
                      ".txt",
                      sep = ""
    )
  }
  
  # read as a vector
  #x <- as.character(scan(x))  
  
  # header needed to read txt into Praat
  praat_header <- c('File type = "ooTextFile"',
                    'Object class = "Sound 2"',
                    '',
                    '0', 
                    '0.41', 
                    '6536', 
                    '0.0000610221205187', 
                    '0.0000305110602593', 
                    '1', 
                    '1', 
                    '1', 
                    '1', 
                    '1')
  
  # add the header to loaded file
  pf <- append(praat_header, x)
  
  # save the output
  write.table(pf, 
              file=filename, 
              quote=FALSE, 
              row.names=FALSE, 
              col.names=FALSE)
  
}
