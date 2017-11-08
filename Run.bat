@set VRTransferBomb=D:\gitWork\DevelopSocialGame\SeriesGames\TransferBomb\Assets
@set PythonConfig=D:\work\NcyWarIIProtobuf\PythonConfigure

@set CSVPath=F:\GitHubProjects\PythonConfigure\CSVExam\
@set ProtoPath=F:\GitHubProjects\PythonConfigure\ProtoExam\
@set CSharpPath=D:\gitWork\DevelopSocialGame\SeriesGames\TransferBomb\TransferBombDLL\
@set PythonClassPath=%PythonConfig%\PythonPb2
@set ProtoDataPath=%VRTransferBomb%\transferbomb\Self\Resources\ProtoBytes\

@set ProtogenPath=%PythonConfig%\protobuf-net\ProtoGen\protogen
@set ProtocPath=%PythonConfig%\protoc


@echo %CSVDir%

@Rem 清空Proto目录.
@Rem @rd /S/Q %ProtoPath%
@Rem @md %ProtoPath% 

@Rem 清空CSharp目录
@Rem @rd /S/Q %CSharpPath%
@Rem @md %CSharpPath%

@Rem 清空PythonPb2目录
@Rem @rd /S/Q %PythonClassPath%
@Rem @md %PythonClassPath%

@Rem @pause

@Rem 需要进入目录.

@Rem CSV->Proto
@python ./PythonCSV/OperateCSV.py %CSVPath% %ProtoPath%

rem @Rem 逐步检查功能是否正确.
rem @Rem @pause

rem @Rem 处理Proto->CS
rem @python ./PythonCSV/ConvertProto2CS.py %ProtogenPath% %ProtoPath% %CSharpPath% %PythonClassPath% %ProtocPath%

rem @Rem 处理CSV 通过Proto把CSV序列化为Bytes.
rem @python ./PythonCSV/SeriData.py %CSVPath% %PythonClassPath% %ProtoDataPath% 

pause