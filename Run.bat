@set VRTransferBomb=D:\gitWork\DevelopSocialGame\SeriesGames\TransferBomb\Assets
@set PythonConfig=D:\work\NcyWarIIProtobuf\PythonConfigure

@set CSVPath=%VRTransferBomb%\DesignData\
@set ProtoPath=%PythonConfig%\War2Scheme\
@set CSharpPath=D:\gitWork\DevelopSocialGame\SeriesGames\TransferBomb\TransferBombDLL\
@set PythonClassPath=%PythonConfig%\PythonPb2
@set ProtoDataPath=%VRTransferBomb%\transferbomb\Self\Resources\ProtoBytes\

@set ProtogenPath=%PythonConfig%\protobuf-net\ProtoGen\protogen
@set ProtocPath=%PythonConfig%\protoc


@echo %CSVDir%

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

@Rem �𲽼�鹦���Ƿ���ȷ.
@Rem @pause

@Rem ����Proto->CS
@python ./PythonCSV/ConvertProto2CS.py %ProtogenPath% %ProtoPath% %CSharpPath% %PythonClassPath% %ProtocPath%

@Rem ����CSV ͨ��Proto��CSV���л�ΪBytes.
@python ./PythonCSV/SeriData.py %CSVPath% %PythonClassPath% %ProtoDataPath% 

@pause