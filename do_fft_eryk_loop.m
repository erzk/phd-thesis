% Runs the FFT (doFFT from Helen) on responses, prints out the first and last X percent, then saves the output
% EW: 22 August 2014

for k = 1:6
    fprintf('==========Starting subject %d: %s\n', k,'===============');
    try
    % First load a txt file into a workspace:
    subject = num2str(k);
    % Specify the condition
    condition = 'perc'; %{perc, shad, sil, self}
    % Specify the tone
    tone = 'rise'; %{fall, rise}
    full_name = strcat('0',subject,'-',condition,'-',tone);
    % Specify the file name to load
    fileName = (strcat('0',num2str(k),'-',condition,'-',tone,'_rerefEXG2_70to2000_epoch(2to250)_average.txt'));
   
    responsef = textread(fileName);

    % Then run the FFT script; txt file is give the name ‘ans’ in the workspace
    resultFFT = doFFT(responsef, length(responsef), 16384);
    print(full_name, '-dpng');
    
    % Calculate the value of the first section (percentage) 
    
    % Define the percentage
    percentage = 10;
    % Append the name
    full_name_beg = strcat(full_name,'_',int2str(percentage),'_percent_beginning');
    response_beg = responsef(1:((length(responsef)/100)*percentage),:);
    resultFFT = doFFT10(response_beg, length(response_beg), 16384);
    print(full_name_beg, '-dpng');
    
    % Calculate the value of the middle section (percentage)
    % Calculate the middle
    middle_point = (length(responsef)/2);
    one_percent = length(responsef)/100;
    % Calculate the lower and higher boundary of the middle section
    middle_low = middle_point - ((percentage/2)*one_percent);
    middle_high = middle_point + (((percentage/2)*one_percent)-1);
    full_name_mid = strcat(full_name,'_',int2str(percentage),'_percent_mid');
    response_mid = responsef(middle_low:middle_high,:);
    % new function (doFFT) to change the colour - not the best way but it works
    resultFFT = doFFT10m(response_mid, length(response_mid), 16384);
    print(full_name_mid, '-dpng');
   
    
    %Calculate the value of the last section (percentage) 
    full_name_end = strcat(full_name,'_',int2str(percentage),'_percent_end');
    response_end = responsef(end-(((length(responsef)/100)*percentage)-1):end,:);
    resultFFT = doFFT10e(response_end, length(response_end), 16384);
    print(full_name_end, '-dpng');
    
    close(all);
    catch err %if error is caught then the loop won't stop but will continue running
        continue
    end
end;

close all;
