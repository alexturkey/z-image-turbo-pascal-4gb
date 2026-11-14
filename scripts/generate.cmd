@echo off
rem Thin wrapper: generate.cmd --prompt "a red fox in snow"   (all options: generate.cmd --help)
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%~dp0generate.py" %*
) else (
  python "%~dp0generate.py" %*
)
exit /b %errorlevel%
