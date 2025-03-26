@echo off
echo Removing __pycache__ directories...

:: Remove __pycache__ directories recursively
:: Remove all __pycache__ directories recursively from the entire project
for /d /r %%i in (__pycache__) do if exist "%%i" rd /s /q "%%i"

:: Remove all .pytest_cache directories recursively from the entire project
for /d /r %%i in (.pytest_cache) do if exist "%%i" rd /s /q "%%i"

echo __pycache__ directories removed.

:: Now run pytest
echo Running pytest...
pytest

