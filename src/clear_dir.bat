@echo off

REM Code To Clear Working Directory
REM From Useless Files

rmdir "./dist" /s /q
rmdir "./build" /s /q
del "./snip.png" 2>nul
del "*.spec" 2>nul