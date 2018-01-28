% eryk.walczak.11 [at] ucl DOT ac DOT uk

% this script runs the EEG analysis, shows the plots
% and saves the cleaned continuous and ERP files

% the script expects the following namimg conventions:
% data: 01-perc-NAME-DeciR.bdf
% event: _EventList-perc-Fall_9_3ext.txt

% ------------------------------------------------

%%% specify the subject numbers

subject_list = {'01-NAME', '02-NAME', '03-NAME', '04-NAME'} % trigger code: 127
%subject_list = {'05-NAME', '06-NAME', '07-NAME', '08-NAME'}; % trigger code: 255

%%% specify which condition to analyse
condition = '-shad'; % check pop_geterpvalues() TODO ifelse

%%% specify which session to analyse
day = '-01';
numsubjects = length(subject_list);

%specifies the folder where bdf (data), ced (channel location), and txt
%(event list) files are located; the output will also be saved there
parentfolder = '/media/___/MyPassport/ABR-Training2/DATA/CH/Processed/Deci_Reduced/';

for s=1:numsubjects
subject = subject_list{s};
% subjectfolder = [parentfolder subject '\'];%use this line if the files are stored in separate folders
fprintf('==========Starting subject %d: %s%s%s==========\n', s, subject_list{s}, condition);
    EEG = pop_biosig([parentfolder subject day condition '-DeciR.bdf'], 'ref',[11 12] );%ref - mastoids EX3 and EX4
    EEG.setname=[subject condition day];
    EEG = eeg_checkset( EEG );
    %loads the default channel location, then loads the custom location and
    %autodetects locations 
    EEG  = pop_chanedit(EEG, 'lookup','/media/___/MyPassport/eeglab13_4_3b/plugins/dipfit2.3/standard_BESA/standard-10-5-cap385.elp','load',{[parentfolder '_Biosemi_9_3ext.ced'] 'filetype' 'autodetect'});
    EEG = eeg_checkset( EEG );
    %loads the event list; TO DO: remove the pop-up
    % 58 events in participants 5-8; triggers were set to '255'
    EEG = pop_editeventlist( EEG , 'BoundaryNumeric', {-99}, 'BoundaryString', { 'boundary' }, 'ExportEL', 'none', 'List', [parentfolder '_EventList' condition '58_9_3ext.txt'], 'SendEL2', 'EEG', 'UpdateEEG', 'on' );
    EEG = eeg_checkset( EEG );
    %specify the epoch values
    %if condition == '-self'
    if strcmp('-self', condition) == 1
        %use baseline [-150 0] for self-prod
        EEG = pop_epochbin( EEG , [-150.0  350.0],  [-150 0]);
    else
        %use baseline [-150 100] for other conditions
        EEG = pop_epochbin( EEG , [-150.0  350.0],  [-50 100]);
        %EEG = pop_epochbin( EEG , [-50.0  450.0],  [ -50 100]);
    end
    EEG = eeg_checkset( EEG );
    %filter settings: filters channels 1:12, high-pass 0.5, low-pass 30,
    %uses IIR Butterworth filter, the rest is default
    EEG  = pop_basicfilter( EEG, 1:10 , 'Cutoff', [0.5 30], 'Design', 'butter', 'Filter', 'bandpass', 'Order', 2);
    EEG = eeg_checkset( EEG );
    %draw the plot
    %pop_eegplot( EEG, 1, 1, 1);
    EEG = eeg_checkset( EEG );
    %EEG = pop_saveset( EEG, 'filename',[subject condition '_elist_be_filt'],'filepath', parentfolder); % save before running ICA
    EEG = pop_artmwppth( EEG , 'Channel', 1:10, 'Flag', 1, 'Review', 'on', 'Threshold', 50, 'Twindow', [-150 350], 'Windowsize', 20);
    EEG = pop_artstep( EEG , 'Channel', 1:10, 'Flag', 1, 'Review', 'on', 'Threshold', 15, 'Twindow', [-150 350], 'Windowsize', 400, 'Windowstep', 10);
    pop_summary_AR_eeg_detection(EEG, [parentfolder subject day condition '_AR_summary_ad.txt']);
    eeglab redraw;
    EEG = pop_saveset( EEG, 'filename',[subject day condition '_cleaned'],'filepath', parentfolder);
    % MAKE ERPs
    EEG = eeg_checkset( EEG );
    ERP = pop_averager( EEG , 'Criterion', 'good', 'DSindex', 1, 'SEM', 'on' );
    ERP = pop_savemyerp(ERP, 'erpname', [subject day condition], 'filename', [subject day condition '.erp'], 'filepath', parentfolder, 'warning', 'on');
    EEG = eeg_checkset( EEG );
    ERP = pop_export2text( ERP, [parentfolder subject day condition '-ERP.txt'],  1, 'electrodes', 'on',...
 'precision',  4, 'time', 'on', 'timeunit',  0.001 );
    % TODO: ifelse statement to control for the 100 ms delay in self
    ALLERP = pop_geterpvalues( ERP, [130 180],  1,  1:9 , 'Baseline', 'pre', 'Binlabel', 'on', 'FileFormat', 'long', 'Filename',...
 [parentfolder subject day condition '-ERP-mean_amplitude_two_auto_detected_latencies-130-180.txt'], 'Fracreplace',...
 'NaN', 'IncludeLat', 'yes', 'InterpFactor',  1, 'Measure', 'meanbl', 'Resolution',  3 );
    EEG = eeg_checkset(EEG);
    ALLERP = pop_geterpvalues( ERP, [200 249],  1,  1:9 , 'Baseline', 'pre', 'Binlabel', 'on', 'FileFormat', 'long', 'Filename',...
 [parentfolder subject day condition '-ERP-mean_amplitude_two_auto_detected_latencies-200-249.txt'], 'Fracreplace',...
 'NaN', 'IncludeLat', 'yes', 'InterpFactor',  1, 'Measure', 'meanbl', 'Resolution',  3 );
    EEG = eeg_checkset(EEG);
end;

close all;
