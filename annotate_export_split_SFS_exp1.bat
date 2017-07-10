REM define the working directory
set location=%cd%
REM define the trial
set trial=01
REM define the condition
set condition=fall
REM define the file name, e.g. 01-NAME-self-fall
set filename=%trial%-shad-%condition%
REM transform wav files into sfs
cnv2sfs -i 1 %filename%.wav %filename%.sfs
REM create annotations http://www.phon.ucl.ac.uk/resource/sfs/help/man/npoint.htm
npoint -n 1500 -b -0.05 -l da-%trial%-%condition% %filename%.sfs
REM export annotations to a csv file
anlist %filename%.sfs -C > %filename%.csv
REM split the continuous wav file into short wav files based on the delimiters created by npoint
wordchop -d %location%\%trial%\ %filename%.sfs
REM transform all split sfs files in the specified folder into wav files and delete sfs files
FOR /R %location%\%trial%\ %%A IN (*.sfs) DO (
sfs2wav "%%A"
del "%%A")
