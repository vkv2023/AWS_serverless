@echo off

rem The sole purpose of this script is to make the command
rem
rem     source .venv/bin/activate
rem
rem (which activates a Python virtualenv on Linux or Mac OS X) work on Windows.
rem On Windows, this command just runs this batch file (the argument is ignored).
rem
rem Now we don't need to document a Windows command for activating a virtualenv.

echo Executing .venv\Scripts\activate.bat for you
.venv\Scripts\activate.bat
echo Setting up default account, Region, and Profile
set CDK_DEFAULT_ACCOUNT=632804446443
set CDK_DEFAULT_REGION=us-east-1
set AWS_PROFILE=cli-user
