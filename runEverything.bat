C:
@start "" xampp\apache\bin\httpd.exe
set url="localhost"
start chrome %url%
E:
python "E:\Google Drive\Streaming Materials\public_html\chatListener\listenerPythonServer.py"
