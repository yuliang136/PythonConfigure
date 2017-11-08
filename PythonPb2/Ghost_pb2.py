# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Ghost.proto

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
  name='Ghost.proto',
  package='',
  serialized_pb=_b('\n\x0bGhost.proto\"\xd1\x01\n\x05Ghost\x12\x1f\n\x05items\x18\x01 \x03(\x0b\x32\x10.Ghost.GhostItem\x1a\xa6\x01\n\tGhostItem\x12\n\n\x02ID\x18\x01 \x02(\x05\x12\x0c\n\x04Name\x18\x02 \x02(\t\x12\r\n\x05place\x18\x03 \x02(\x05\x12\x0b\n\x03HEX\x18\x04 \x02(\t\x12\x12\n\nCreatureID\x18\x05 \x02(\t\x12\x0c\n\x04Icon\x18\x06 \x02(\t\x12\x0f\n\x07Winicon\x18\x07 \x02(\t\x12\x13\n\x0brecognition\x18\x08 \x02(\t\x12\r\n\x05light\x18\t \x02(\t\x12\x0c\n\x04\x62omb\x18\n \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GHOST_GHOSTITEM = _descriptor.Descriptor(
  name='GhostItem',
  full_name='Ghost.GhostItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='Ghost.GhostItem.ID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='Ghost.GhostItem.Name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='place', full_name='Ghost.GhostItem.place', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HEX', full_name='Ghost.GhostItem.HEX', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CreatureID', full_name='Ghost.GhostItem.CreatureID', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Icon', full_name='Ghost.GhostItem.Icon', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Winicon', full_name='Ghost.GhostItem.Winicon', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recognition', full_name='Ghost.GhostItem.recognition', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='light', full_name='Ghost.GhostItem.light', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bomb', full_name='Ghost.GhostItem.bomb', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=59,
  serialized_end=225,
)

_GHOST = _descriptor.Descriptor(
  name='Ghost',
  full_name='Ghost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='Ghost.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GHOST_GHOSTITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=225,
)

_GHOST_GHOSTITEM.containing_type = _GHOST
_GHOST.fields_by_name['items'].message_type = _GHOST_GHOSTITEM
DESCRIPTOR.message_types_by_name['Ghost'] = _GHOST

Ghost = _reflection.GeneratedProtocolMessageType('Ghost', (_message.Message,), dict(

  GhostItem = _reflection.GeneratedProtocolMessageType('GhostItem', (_message.Message,), dict(
    DESCRIPTOR = _GHOST_GHOSTITEM,
    __module__ = 'Ghost_pb2'
    # @@protoc_insertion_point(class_scope:Ghost.GhostItem)
    ))
  ,
  DESCRIPTOR = _GHOST,
  __module__ = 'Ghost_pb2'
  # @@protoc_insertion_point(class_scope:Ghost)
  ))
_sym_db.RegisterMessage(Ghost)
_sym_db.RegisterMessage(Ghost.GhostItem)


# @@protoc_insertion_point(module_scope)
