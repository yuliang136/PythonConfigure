# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Buff.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Buff.proto',
  package='',
  serialized_pb=_b('\n\nBuff.proto\"\x94\x01\n\x04\x42uff\x12\x1d\n\x05items\x18\x01 \x03(\x0b\x32\x0e.Buff.BuffItem\x1am\n\x08\x42uffItem\x12\n\n\x02Id\x18\x01 \x02(\x05\x12\x0c\n\x04type\x18\x02 \x02(\x05\x12\x0e\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x02(\t\x12\x0f\n\x07percent\x18\x04 \x02(\x05\x12\x0c\n\x04time\x18\x05 \x02(\x05\x12\x0b\n\x03get\x18\x06 \x02(\x05\x12\x0b\n\x03use\x18\x07 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BUFF_BUFFITEM = _descriptor.Descriptor(
  name='BuffItem',
  full_name='Buff.BuffItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='Buff.BuffItem.Id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Buff.BuffItem.type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effect', full_name='Buff.BuffItem.effect', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percent', full_name='Buff.BuffItem.percent', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='Buff.BuffItem.time', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get', full_name='Buff.BuffItem.get', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use', full_name='Buff.BuffItem.use', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=163,
)

_BUFF = _descriptor.Descriptor(
  name='Buff',
  full_name='Buff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='Buff.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BUFF_BUFFITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=163,
)

_BUFF_BUFFITEM.containing_type = _BUFF
_BUFF.fields_by_name['items'].message_type = _BUFF_BUFFITEM
DESCRIPTOR.message_types_by_name['Buff'] = _BUFF

Buff = _reflection.GeneratedProtocolMessageType('Buff', (_message.Message,), dict(

  BuffItem = _reflection.GeneratedProtocolMessageType('BuffItem', (_message.Message,), dict(
    DESCRIPTOR = _BUFF_BUFFITEM,
    __module__ = 'Buff_pb2'
    # @@protoc_insertion_point(class_scope:Buff.BuffItem)
    ))
  ,
  DESCRIPTOR = _BUFF,
  __module__ = 'Buff_pb2'
  # @@protoc_insertion_point(class_scope:Buff)
  ))
_sym_db.RegisterMessage(Buff)
_sym_db.RegisterMessage(Buff.BuffItem)


# @@protoc_insertion_point(module_scope)
