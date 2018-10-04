# PhD thesis - analysis guidelines

## Audio analysis
1. Run `annotate_export_split_SFS.bat` to annotate, extract durations of annotated utterances to a csv file, and split the annotated continuous file into short wav files based on delimeters of annotations.
2. Split wav files will be used in [PraatR](http://www.aaronalbin.com/praatr/index.htm) to extract pitch values: `praatrPitchLoop.R`
3. Run `praatr_analyse.R` to summarise and plot acquired values.

## Filter raw bdf files:
1.	Run `gogo_loop.m` – use different baseline for self-production (-49 1) than other conditions (50 101). Epoch -49 350 is fine.
2.	Matlab script (`gogo_loop.m`) has to be located in the EEGLab folder - C:\eeglab13_0_1b – EEGLab folders have to be in the Matlab path
3.	The files are saved in the L0n folders in the current Matlab folder.

## Create Grand Averages:
### In R:
1. Use `ffr_averages.R`

### In Matlab:
1.	Create new folders with the relevant txt files - use `copy_all_type.bat`
2.	Run `makeGA.m` (modify the source folder) - type `makeGA` on the command line

## Run FFT
1. Basic version: `doFFT.m`
2. Loop: `doFFT_eryk_loop.m`
3. Extracts 10% at the beginning, middle, and end of each file: `doFFT_eryk_loop_percentage_bme_onAVG.m`

## Transform .mat output to .txt files
1. Use `mat2txt.m`

## Plot Grand Averages:
1.	Plot the averages from .mat files using `load_and_plot_GAs.m`

## Create plots for individual FFRs:
1.	Plot individual files using .avg files (created with Tim’s script) using `ffr_plot_ind_loop.R`

## Create .avg files from .txt (Response in Brainstem Toolbox):
1.	Use `bt_txt2avg.m` in BT2013
```
bt_txt2avg('filename.txt', 6855, -15.8, 58.89)
```
where filename.txt is the exported brainstem data file, 6855 is the sampling rate, -15.8 corresponds to the start time (ms) of the response epoch and 58.89 corresponds to the time at the end the response epoch. (In this example, the recording window is 74.69 ms)
e.g.
```
bt_txt2avg('perc-fall.txt', 16384, -49, 350)
```
Use the script: `txt2avg_script.m`

## Create .avg files from .wav (Stimulus in Brainstem Toolbox):
1.	BT2013 must be the current Matlab folder
2.	Use the command 
```
wav2avg('xxxxxxx_self_01.wav', 16384)
```
The sampling rate of stimulus and response avg file has to be the same.

## Use Butterworth band pass filter on the wav files and save the filtered data to an avg file:
1. Run the script `wavButter.m`

## Create .wav files from .txt (FFRs):
1. In R:
```
library(seewave)

savewav(FFR_vector, f = 16384)
```

## Prepare txt files to be loaded into Praat:
1. Find the output of `gogo_loop.m`
2. Use `txt2praat.R`

## Brainstem Toolbox:
[Download BT](http://www.brainvolts.northwestern.edu/form/freeware.php)

1.	Start the GUI by typing `bt_ptgui` in Matlab
2.	Load the response (avg), stimulus (avg), and adjust the settings.
3.	Excel output is saved in /output_files

## Cortical analysis
1. Make ERPs (without ICA) using `makeERPs.m`
2. Run ICA on filtered/epoched data using `ICA_loop_catch.m`
3. Average ERPs and append them
4. Channel order for plotting ERPs:  1 5 6 2 7 8 3 4 9

## fNIRS analysis
1. Select software OpenGL rendering in Matlab (to enable plotting in Homer2):

`matlab -softwareopengl`
