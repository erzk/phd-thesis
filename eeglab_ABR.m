function eeglab_ABR(fileDirectory, listener, Active, Reference, Lcut_off, Hcut_off, artifact,s_epoch, e_epoch, s_baseline, e_baseline, s_avg, e_avg)

%% parameters
% fileDirectory - folder with files to be processed
% Active - active electrode (EXG1, EXG2, or EXG3)
% Reference - reference electrode (EXG2, EXG3, or EXG4)
% Lcut_off - lower bound bandpass filter
% Hcut_off - upper bound bandpass filter
% s_epoch - start time (in ms) of epoch
% e_epoch - end time (in ms) of epoch
% s_baseline - start time (in ms) of pre-stim 
% e_baseline - end time (in ms) of pre-stim
% s_avg - start time (in ms) of response for avg file (note: pre-stim has to be
%       negative)
% e_avg - end time (in ms) of response for avg file (note: pre-stim has to be
%       negative)

%% Based on EEGLAB history file generated on the 04-Jun-2012
% Version 1.0 - June 2012
%       Assumes a 32-set of empty electrode is imported. EXG electrodes start at 33.
%
% Version 1.1 - June 2012
%       Extracts only the active and reference channels. Only works with 2
%       channels. 
%       Also changed pop_biosig
% Version 1.2 - March 2013
%     Can read in files from other directories (no longer necessary to copy BDF files into eeglab folder)
%     Still writes output files into eeglab folder
%
% created by: Tim Schoof - t.schoof [at] ucl.ac.uk
% modified by EW
% ------------------------------------------------

%% some starting values
order = 2;
% Lcut_off = 100; % click ABR
% Hcut_off= 3000; % click ABR
% Lcut_off = 70; % speech ABR
% Hcut_off= 2000; % speech ABR
% Active = EXG1; % Cz
% Reference = EXG2; % Right earlobe

%%
fileDirectory = [fileDirectory '\' listener];
% get a list of files
Files = dir(fullfile(fileDirectory, '*.bdf'));
nFiles = size(Files);

% create output directory
OutputDir = ['Output_' listener ];
mkdir(OutputDir)

% create output file for number of rejected and accepted sweeps
OutFile = [OutputDir '\' listener  '_rejected_sweeps' '_' Active '_' Reference '.csv'];
% write some headings and preliminary information to the output file
WriteHeader = exist(OutFile);
fTrackOut = fopen(OutFile, 'at');
if ~WriteHeader
       fprintf(fTrackOut, 'listener,response,accepted,rejected,active,reference'); 
       fclose(fTrackOut);
end

for i=1:nFiles
    fileName = Files(i).name;
    [pathstr, name, ext] = fileparts(fileName);
    
    % specify required channels
    if strcmp(Active, 'EXG1')
        Act = 33;
    elseif strcmp(Active, 'EXG2')
        Act = 34;
    elseif strcmp(Active, 'EXG3')
        Act = 35;
    elseif strcmp(Active, 'A32')
        Act = 32;
    elseif strcmp(Active, 'A31')
        Act = 31;
    elseif strcmp(Active, 'A5')
        Act = 5;
    elseif strcmp(Active, 'A13')
        Act = 13;
    else
        error('ERROR: Your active electrode should be EXG1, EXG2, EXG3, or A32')
    end

    if strcmp(Reference, 'EXG1')
        Ref = 33;
    elseif strcmp(Reference,'EXG2')
        Ref = 34;
    elseif strcmp(Reference, 'EXG3')
        Ref = 35;
    elseif strcmp(Reference, 'EXG4')
        Ref = 36;
    else
        error('ERROR: Your reference electrode should be EXG2, EXG3, or EXG4')
    end

    if Act == Ref
        error('ERROR: Your reference electrode and active electrode cannot be the same')
    end

    % start eeglab
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    
    % load bdf file, extract only active and reference channel, and save as EEG data set
    EEG = pop_biosig_TS((fullfile(fileDirectory,fileName)), 'channels', [Act Ref],'ref',Ref,'blockepoch','off');
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % re-code channels (only 2 channels remain)
    Act = 1;
    Ref = 2;
    
    % re-reference the data to EXG2 (34) and save as new EEG data set
    EEG = pop_reref( EEG, Ref);
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % filter based on filtfilt (so effectively zero phase shift)
    fprintf('%s', 'Filtering...')
    [EEG.data b a] = butter_filtfilt(EEG.data, Lcut_off, Hcut_off, order);
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);    
    EEG = eeg_checkset( EEG );

    % epoch
    % convert epoch start and end times to seconds
    s_epoch_s = s_epoch/1000;
    e_epoch_s = e_epoch/1000;
    % epoch
    [EEG, indices] = pop_epoch( EEG, {'255' }, [s_epoch_s     e_epoch_s], 'newname', ['', name, '_reref', Reference, '_', num2str(Lcut_off), 'to', num2str(Hcut_off), '_epoch(', num2str(s_epoch), 'to', num2str(e_epoch), ')', ''], 'epochinfo', 'yes');
    % determine number of epochs
    totalsweeps = length(indices);
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % baseline correction 
    EEG = pop_rmbase( EEG, [s_baseline      e_baseline]);
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % artifact rejection
    [EEG Indexes] = pop_eegthresh(EEG,1,Act,-1*artifact,artifact,s_epoch_s,e_epoch_s,0,1);
    rejected = length(Indexes);
    accepted = totalsweeps - rejected;
    % save indexes of rejected sweeps in text file
    dlmwrite(['', OutputDir, '\', name, '_reref', Reference '_', num2str(Lcut_off), 'to', num2str(Hcut_off), '_epoch(', num2str(s_epoch), 'to', num2str(e_epoch), ')', '_rejected_sweeps.txt', ''],Indexes);
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);    
    EEG = eeg_checkset( EEG );

    % plot averaged response
    [avg] = pop_comperp( ALLEEG, 1, 4,[],'addavg','on','addstd','off','diffavg','off','diffstd','off','chans',Act,'tplotopt',{'ydir' -1});
    saveas(gcf,['', OutputDir, '\', name, '_reref', Reference, '_', num2str(Lcut_off), 'to', num2str(Hcut_off), '_epoch(', num2str(s_epoch), 'to', num2str(e_epoch), ')', '_average', ''],'fig');
    [ALLEEG EEG] = eeg_store(ALLEEG, EEG, CURRENTSET);
    EEG = eeg_checkset( EEG );

    % save averaged EEG to txt and avg files
    % select correct channel
    Active_chan = avg(Act,:);
    Active_chan = Active_chan';
    % write to txt and avg
    dlmwrite(['', OutputDir, '\', name, '_reref', Reference, '_', num2str(Lcut_off), 'to', num2str(Hcut_off), '_epoch(', num2str(s_epoch), 'to', num2str(e_epoch), ')', '_average.txt', ''],Active_chan);
    bt_txt2avg(['', OutputDir, '\', name, '_reref', Reference, '_', num2str(Lcut_off), 'to', num2str(Hcut_off), '_epoch(', num2str(s_epoch), 'to', num2str(e_epoch), ')', '_average.txt', ''],16384,s_avg,e_avg);
 
    % print out relevant information to csv file
    fTrackOut = fopen(OutFile, 'at');
    fprintf(fTrackOut, '\n%s,%s,%d,%d,%s,%s', ...
    OutputDir,name,accepted,rejected,Active,Reference);
    
    fclose(fTrackOut);
    
   % clear all
    ALLEEG = pop_delset(ALLEEG,1:5);
end
    
fprintf('%s', 'Finished!')
