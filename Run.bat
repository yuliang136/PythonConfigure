@set VRTransferBomb=D:\gitWork\DevelopSocialGame\SeriesGames\TransferBomb\Assets
@set PythonConfig=F:\GitHubProjects\PythonConfigure

@set CSVPath=F:\GitHubProjects\PythonConfigure\CSVExam\
@set ProtoPath=F:\GitHubProjects\PythonConfigure\ProtoExam\
@set CSharpPath=F:\GitHubProjects\PythonConfigure\CSharpExam\
@set PythonClassPath=%PythonConfig%\PythonPb2
@set ProtoDataPath=%VRTransferBomb%\transferbomb\Self\Resources\ProtoBytes\

@set ProtogenPath=%PythonConfig%\protobuf-net\ProtoGen\protogen
@set ProtocPath=%PythonConfig%\protoc


chcp 65001
set PYTHONIOENCODING=utf-8




@em @echo %CSVDir%

@Rem ���ProtoĿ¼.
@Rem @rd /S/Q %ProtoPath%
@Rem @md %ProtoPath% 

@Rem ���CSharpĿ¼
@Rem @rd /S/Q %CSharpPath%
@Rem @md %CSharpPath%

@Rem ���PythonPb2Ŀ¼
@Rem @rd /S/Q %PythonClassPath%
@Rem @md %PythonClassPath%

@Rem @pause

@Rem ��Ҫ����Ŀ¼.

@Rem CSV->Proto
@python ./PythonCSV/OperateCSV.py %CSVPath% %ProtoPath%

@rem @Rem �𲽼�鹦���Ƿ���ȷ.
@rem @Rem @pause

@rem Proto->CS
@python ./PythonCSV/ConvertProto2CS.py %ProtogenPath% %ProtoPath% %CSharpPath% %PythonClassPath% %ProtocPath%

@rem @Rem ����CSV ͨ��Proto��CSV���л�ΪBytes.
@rem @python ./PythonCSV/SeriData.py %CSVPath% %PythonClassPath% %ProtoDataPath% 

pause