REM Set the base path for Chrome user data
set baseDir=%LOCALAPPDATA%\Google\Chrome\User Data

REM Check if the base directory exists
if exist "%baseDir%" (
    echo Found Chrome User Data directory: %baseDir%
    
    REM Loop through all profile folders (Default, Profile 1, Profile 2, etc.)
    for /d %%p in ("%baseDir%\*") do (
        set "profileDir=%%p"
        call :deleteCache "%%p"
    )

    echo All Chrome profiles' cache deleted.
) else (
    echo Chrome User Data directory not found at: %baseDir%
)

:deleteCache
REM Function to delete cache in each profile
set profilePath=%~1
set cacheDir=%profilePath%\Cache

if exist "%cacheDir%" (
    echo Deleting cache in: %profilePath%
    del /q /s /f "%cacheDir%\*.*"
    rd /s /q "%cacheDir%"
    echo Cache deleted for: %profilePath%
) else (
    echo No cache found for: %profilePath%
)
exit /b