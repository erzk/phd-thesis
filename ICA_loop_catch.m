% generated from EEGLAB history
% made by eryk.walczak.11 [at] ucl DOT ac DOT uk

% this script runs the ICA analysis in the loop for all conditions

% the script expects the following namimg conventions:
% data: 01-PARTICIPANT-CONDITION_elist_be_filt .fdt .set
% e.g.: 01-name-self_elist_be_filt .fdt .set

% ------------------------------------------------

%specify the subject numbers
subject_list = {'01', '02', '03', '04', '05', '06'};
%specify which condition to analyse
condition = '-sil';
%specify which participant to analysee
participant = '-NAME';

numsubjects = length(subject_list);

%specifies the folder where bdf (data), ced (channel location), and txt
%(event list) files are located; the output will also be saved there
parentfolder = 'H:\ABR-Training\_DATA\Deci_Reduced';

for s=2:numsubjects
    subject = subject_list{s};
    fprintf('==========Starting subject %d: %s%s%s==========\n', s, subject_list{s}, participant, condition);
    try %try to catch errors
        InputFile = [subject participant condition '_elist_be_filt.set'];
        OutputFile = [subject participant condition '_ICA_done.set'];
        EEG = pop_loadset('filename',InputFile,'filepath',parentfolder); %specifies the path where the input files are located
        EEG = eeg_checkset( EEG );
        %Start diary
        diary
        diaryName = [subject participant condition '_relative_variance.txt'];
        diary(diaryName)
        %Run ICA
        EEG = pop_runica(EEG, 'extended',1,'interupt','on'); % characteristics of ICA
        EEG = eeg_checkset( EEG );
        %draw and save a figure
        figure; pop_spectopo(EEG, 0, [-150.3906      347.6563], 'EEG' , 'freq', [10], 'plotchan', 0, 'percent', 20, 'icacomps', [1:9], 'nicamaps', 10, 'freqrange',[2 25],'electrodes','off');
        PlotInputFile = [subject condition participant '_ICA_done.png'];
        print('-dpng', PlotInputFile);
        close;
        diary off
        EEG = eeg_checkset( EEG );
        EEG = pop_saveset( EEG, 'filename',OutputFile,'filepath',parentfolder); %specifies the path where the output files are located
        EEG = eeg_checkset( EEG );
    catch err %if error is caught then the loop won't stop but will continue running
        continue
    end
end;
