@echo off
rem Thin launcher for the installer: kur.cmd [setup.py options]   (all options: kur.cmd --help)
rem Double-click: first prints the dry run (--dry-run: writes nothing, downloads nothing), waits for a key, then installs.
rem From a terminal it passes your options straight to scripts\setup.py, like generate.cmd does for generate.py.
setlocal
set "DBL="
echo %cmdcmdline% | "%SystemRoot%\System32\find.exe" /i "/c" >nul && set "DBL=1"
set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY where python >nul 2>nul && set "PY=python"
if not defined PY (
  echo ERROR: Python 3.10 or newer was not found. Fix: install it with  winget install Python.Python.3.12  and open a new window.
  if defined DBL pause
  exit /b 2
)
if defined DBL if "%~1"=="" (
  %PY% "%~dp0scripts\setup.py" --dry-run
  if errorlevel 1 (
    echo.
    echo The dry run found a problem; nothing was installed. Read the lines above.
    pause
    exit /b 1
  )
  echo.
  echo Nothing has been downloaded yet. Press any key to install, or close this window to stop.
  pause >nul
)
%PY% "%~dp0scripts\setup.py" %*
set "RC=%errorlevel%"
if defined DBL pause
exit /b %RC%
