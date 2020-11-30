@echo off
for /L %%i in (1,1,100) do (
python generatepoints.py 20 2 %%i
)
pause