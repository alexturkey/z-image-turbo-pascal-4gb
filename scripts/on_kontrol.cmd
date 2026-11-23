@echo off
rem Check before a pull request: scripts\on_kontrol.cmd   (quick gates, a few seconds, no GPU, no network)
rem Add  --tam  to run the unit tests as well.
setlocal
set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY where python >nul 2>nul && set "PY=python"
if not defined PY (
  echo ERROR: Python 3.10 or newer was not found. Fix: install it with  winget install Python.Python.3.12  and open a new window.
  exit /b 3
)
if "%~1"=="" (
  %PY% -I -X utf8 "%~dp0denetim.py" --hizli
) else (
  %PY% -I -X utf8 "%~dp0denetim.py" %*
)
exit /b %errorlevel%
