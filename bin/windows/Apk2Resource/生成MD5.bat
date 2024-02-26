
# 
set PrjName=Apk2Resource
# set DirName=配置文件
set UserName=joymeng
set AttachConfigUrl=https://raw.githubusercontent.com/joymeng/%PrjName%/master/MD5.txt
#

set MD5="%~dp0tools\getMD5.exe"
set MD5_TXT="%~dp0tools\MD5.txt"
set MD5_updateFiles="%~dp0tools\updateFiles.txt"
set ContentReplace="%~dp0tools\ContentReplace.exe"

# set channelPackages="%~dp0%DirName%"
set channelPackages=%~dp0

set updateFiles="%~dp0MD5.txt"
set APK_Base="%~dp0\"

if exist %updateFiles% del %updateFiles%

%MD5% %channelPackages%
%ContentReplace% %MD5_TXT% "%APK_Base%" ""
%ContentReplace% %MD5_TXT% \ /
%ContentReplace% %MD5_TXT% "[HeadAppend]" "服务器资源目录(https://raw.githubusercontent.com/%UserName%/%PrjName%/master/)\r\n本地资源目录(%APK_Base%)\r\n待更新资源目录(%AttachConfigUrl%)\r\n\r\n待更新文件(\r\n"
%ContentReplace% %MD5_TXT% "[TailAppend]" "\r\n\r\n)待更新文件\r\n"
if exist %MD5_updateFiles% del %MD5_updateFiles%

if exist %MD5_TXT% copy %MD5_TXT% %updateFiles%
if exist %MD5_TXT% del %MD5_TXT%

exit

