REM copy recursively all files following a pattern to the specified folder
for /R FILEPATH %%f in (*sil*.txt) do copy %%f FILEPATH
REM example: for /R c:\txt %%f in (*sil*.txt) do copy %%f C:\Users\E\Desktop\test_FFRs\FFRs\70_2000\K_sil
