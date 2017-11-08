@set VRTransferBomb=D:\gitWork\DevelopSocialGame\SeriesGames\TransferBomb\ASSETS
@set PythonConfig=F:\GitHubProjects\PythonConfigure

@set PythonClassPath=%PythonConfig%\PythonPb2
@set CSVPath=F:\GitHubProjects\PythonConfigure\CSVExam\
@set ProtoPath=F:\GitHubProjects\PythonConfigure\ProtoExam\
@set CSharpPath=F:\GitHubProjects\PythonConfigure\CSharpExam\
@set ProtoDataPath=F:\GitHubProjects\PythonConfigure\ProtoBytes\

@set ProtogenPath=%PythonConfig%\protobuf-net\ProtoGen\protogen
@set ProtocPath=%PythonConfig%\protoc


rem chcp 65001
rem set PYTHONIOENCODING=utf-8


@Rem CSV->Proto
@python ./PythonCSV/OperateCSV.py %CSVPath% %ProtoPath%

@rem Proto->CS
@python ./PythonCSV/ConvertProto2CS.py %ProtogenPath% %ProtoPath% %CSharpPath% %PythonClassPath% %ProtocPath%

@Rem CSV->Bytes.
@python ./PythonCSV/SeriData.py %CSVPath% %PythonClassPath% %ProtoDataPath% 

pause