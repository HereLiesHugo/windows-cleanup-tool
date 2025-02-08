REM Set the base path for Edge user data
set baseDir=%LOCALAPPDATA%\Microsoft\Edge\User Data

REM Check if the base directory exists
if exist "%baseDir%" (
    echo Found Edge User Data directory: %baseDir%
    
    REM Loop through all profile folders (Default, Profile 1, Profile 2, etc.)
    for /d %%p in ("%baseDir%\*") do (
        set "profileDir=%%p"
        call :deleteCache "%%p"
    )

    echo All Microsoft Edge profiles' cache deleted.
) else (
    echo Edge User Data directory not found at: %baseDir%
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