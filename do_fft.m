% developed by Dr Helen Nuttall (h.nuttall AT ucl DOT ac DOT uk)

function [Y,f] = doFFT(y,L,Fs) 
% This function computes an FFT of a signal and plots it
% Input arguments: y = FFR; L = the length of the FFR; FS = sampling frequency on FFR

NFFT = 2^nextpow2(L); % Next power of 2 from length of FFR
Y = fft(y,NFFT)/L;
f = Fs/2*linspace(0,1,NFFT/2+1);

% Plot single-sided amplitude spectrum.
figure()
plot(f,2*abs(Y(1:NFFT/2+1)))

% Delete the line below to remove the limit on the x-axis 
xlim([0,1000])
ylim([0,0.25])
title('Single-Sided Amplitude Spectrum of y(t)')
xlabel('Frequency (Hz)')
ylabel('|Y(f)|')
