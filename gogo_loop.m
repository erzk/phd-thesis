% Runs the loop on all gogo folders

% Baseline -49 1 (self-prod); 50 101 (all the rest)
% A32-Cz; A31-Fz

% Specify the folder where L0n folders are located
path = 'H:\';

for k = 1:6
    fprintf('========== Starting subject %d: %s\n', k, '===============');
    folder = strcat('L0',int2str(k),'-self');
    disp(folder);
    % eeglab_ABR(fileDirectory, listener, Active, Reference, Lcut_off, Hcut_off, artifact,s_epoch, e_epoch, s_baseline, e_baseline, s_avg, e_avg)
    eeglab_ABR(path, folder, 'A32', 'EXG2', 70, 2000, 35, -49, 350, -49, 1, -49, 350);
    close all;
end;

close all;
