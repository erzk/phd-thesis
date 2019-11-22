% files to use
erp_files = {'0-AM.erp', '0-CS.erp', '0-EB.erp', '0-ED.erp', '0-JR.erp', '0-KGcombined.erp', '0-KW.erp', '0-LW.erp',...
 '0-SH.erp', '100-AM.erp', '100-CS.erp', '100-EB.erp', '100-ED.erp', '100-JR.erp', '100-KG.erp', '100-KW.erp', '100-LW.erp', '100-SH.erp',...
 '200-AM.erp', '200-CS.erp', '200-EB.erp', '200-ED.erp', '200-JR.erp', '200-KG.erp', '200-KW.erp', '200-LW.erp', '200-SH.erp', 'perc-AM.erp',...
 'perc-CS.erp', 'perc-EB.erp', 'perc-ED.erp', 'perc-JR.erp', 'perc-KG.erp', 'perc-KW.erp', 'perc-LW.erp', 'perc-SH.erp', 'sil-AM.erp',...
 'sil-CS.erp', 'sil-EB.erp', 'sil-ED.erp', 'sil-JR.erp', 'sil-KG.erp', 'sil-KW.erp', 'sil-LW.erp', 'sil-SH.erp'}

% print numbers
for i = 1:numel(erp_files)
    disp(i)
end

% loop through ERPs - extract txt forms and measurements
for i = erp_files
    disp(i);
    % load all .erp files
    ERP = pop_loaderp( 'filename', i, 'filepath', '/media/eub/MyPassport/ABR-Jamie masters data/DATA/AllData/ERPsets/EW_renamed/' );
    % create a txt file name
    folder_path = '/media/eub/MyPassport/ABR-Jamie masters data/DATA/AllData/ERPsets/EW_renamed/ERPtxt/';
    txt_filepath = char(strcat(folder_path, strcat(i, '.txt')));
    % save the ERPs to text
    pop_export2text( ERP, txt_filepath,  1, 'electrodes',... 
        'on', 'precision',  4, 'time', 'on', 'timeunit',  0.001 );
    pop_export2text( ERP, char(txt_filepath),  2, 'electrodes',...
 'on', 'precision',  4, 'time', 'on', 'timeunit',  0.001 );
% range filename
amp_130_180_filepath = char(strcat(folder_path, strcat('amp_', i, '_130-180','.txt')));
amp_200_250_filepath = char(strcat(folder_path, strcat('amp_', i, '_200-250','.txt')));
% get average ERP values between the ranges
% N1 = 130-180; P2 = 200-250; ERP's time has been manually adjusted by JS;
% see MSc thesis page 26
ALLERP = pop_geterpvalues( ERP, [ 130 180], [ 1 2],  1:9 , 'Baseline', 'pre', 'Binlabel', 'on', 'FileFormat', 'long', 'Filename',...
 amp_130_180_filepath, 'Fracreplace', 'NaN', 'IncludeLat', 'yes',...
 'InterpFactor',  1, 'Measure', 'meanbl', 'Resolution',  3 );
ALLERP = pop_geterpvalues( ERP, [ 200 250], [ 1 2],  1:9 , 'Baseline', 'pre', 'Binlabel', 'on', 'FileFormat', 'long', 'Filename',...
 amp_200_250_filepath, 'Fracreplace', 'NaN', 'IncludeLat', 'yes',...
 'InterpFactor',  1, 'Measure', 'meanbl', 'Resolution',  3 );
end