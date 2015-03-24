% Running Butterworth band pass filter on a wav file
% Use the same settings as for filtering the FFRs (in eeglab_ABR.m)

% https://stackoverflow.com/questions/17340198/what-is-the-command-for-butterworth-bandpass-filter

filename = 'CH01.wav';
% load the wav file to transform
wavStimulus = wavread(filename);
fs = 16384; % sampling frequency (Hz)

% run the butterworth filter on normalised values
% 2nd order; 70 low cut-off and 2000 high cut-off are used for filtering
% in in eeglab_ABR.m
[b,a] = butter(2, [70 2000]/(fs/2), 'bandpass');
% apply the filter to the loaded wav file
wavStimulusFilt = filter(b,a,wavStimulus);
% append the name of the new file
prefix = 'filtered';
outputFilename = strcat(prefix, filename);
wavwrite(wavStimulusFilt, fs, outputFilename);
