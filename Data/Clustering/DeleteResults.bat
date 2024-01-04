@ECHO OFF
ECHO  Script to delete *.png in sub directories
for /R %%f in (*.png) do echo %%f
for /R %%f in (*.png) do del "%%f"
ECHO Done
PAUSE