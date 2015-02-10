% by dr Helen Nuttall ( h.nuttall (at) ucl.ac.uk )
function makeGA

% sets the Matlab path to your current working directory
path=cd;
% looks for a folder called 'FFRs\Condition' in your current working directory (note: you will need to create this folder and put your FFR .txt files in there). 
% Maybe just put perception files in there for now or modify the script to create subfolders 
FFRpath = fullfile(path,'\FFRs\70_2000\K_sil');
% you need to create another folder called GA_FFRs: this is where the script will save your FFR grand average files 
FFRGApath = fullfile(path, '\GA_FFRs\'); 

% get directory info, looks for the .txt files
fnam=dir(fullfile(FFRpath, ['*.txt']));
% gets filenames 
fnams=arrayfun(@(x)(x.name(1:end)),fnam,'UniformOutput',false); 

% calls the function stored below called 'getGA' using already defined FFRpath and the filenames of txt files in FFRpath (fnams) as function arguments  
GA = getGA(fnams,FFRpath); 
mnam = ['GA.mat']; % creates name for the grand average file

[mnam, pathnam] = uiputfile(fullfile(FFRGApath,'*.mat'),'Save data as: '); % specifies where the data will be saved
save(fullfile(FFRGApath, mnam),'GA');display(['Saved as ' mnam]);  % saves the data

end


function GA = getGA(fnams,FFRpath) % function to make GA
YGA = 0; % initialises YGA variable, to which FFRs will be added with each loop iteration
NParts= length(fnams); % gets the number of files
    for I = 1:NParts % loops through the txt files, loads them in and adds them to the originally empty GA with every loop iteration
        indaverage=load(fullfile(FFRpath,fnams{I})); 
        fnams{I}=fnams{I};
        Yavgk=indaverage;
        YGA=Yavgk+YGA;
        YIndAvg(:,I)=Yavgk; % stores all the individual FFR files in YIndAvg should you ever need them
    end;
YGA = YGA/NParts;  % divides the summed FFRs stored in YGA by the number of files to create the GA
GA.Yavg=YGA; GA.fnams=fnams; GA.YIndAvg=YIndAvg; % save variables to GA structure
end
