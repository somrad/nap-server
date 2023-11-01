# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server_to_client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server_to_client.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16server_to_client.proto\"G\n\x11\x46ileHostingClient\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x13\n\x0bport_number\x18\x02 \x01(\x05\x12\x11\n\tfile_name\x18\x03 \x01(\t\" \n\x0b\x46ileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"<\n\x0c\x46ileResponse\x12,\n\x10\x61vailableClients\x18\x01 \x03(\x0b\x32\x12.FileHostingClient\"V\n\x13RegisterPeerRequest\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x13\n\x0bport_number\x18\x02 \x01(\x05\x12\x1e\n\x16\x66ile_available_with_me\x18\x03 \x03(\t\"U\n\x14RegisterPeerResponse\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x13\n\x0bport_number\x18\x02 \x01(\x05\x12\x1c\n\x14registration_success\x18\x03 \x01(\t2\x89\x01\n\rNapsterServer\x12;\n\x0cRegisterPeer\x12\x14.RegisterPeerRequest\x1a\x15.RegisterPeerResponse\x12;\n\x1cGetPeersServingRequestedFile\x12\x0c.FileRequest\x1a\r.FileResponseb\x06proto3'
)




_FILEHOSTINGCLIENT = _descriptor.Descriptor(
  name='FileHostingClient',
  full_name='FileHostingClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='FileHostingClient.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_number', full_name='FileHostingClient.port_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='FileHostingClient.file_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=97,
)


_FILEREQUEST = _descriptor.Descriptor(
  name='FileRequest',
  full_name='FileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='FileRequest.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=131,
)


_FILERESPONSE = _descriptor.Descriptor(
  name='FileResponse',
  full_name='FileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='availableClients', full_name='FileResponse.availableClients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=193,
)


_REGISTERPEERREQUEST = _descriptor.Descriptor(
  name='RegisterPeerRequest',
  full_name='RegisterPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='RegisterPeerRequest.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_number', full_name='RegisterPeerRequest.port_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_available_with_me', full_name='RegisterPeerRequest.file_available_with_me', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=281,
)


_REGISTERPEERRESPONSE = _descriptor.Descriptor(
  name='RegisterPeerResponse',
  full_name='RegisterPeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='RegisterPeerResponse.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_number', full_name='RegisterPeerResponse.port_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registration_success', full_name='RegisterPeerResponse.registration_success', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=368,
)

_FILERESPONSE.fields_by_name['availableClients'].message_type = _FILEHOSTINGCLIENT
DESCRIPTOR.message_types_by_name['FileHostingClient'] = _FILEHOSTINGCLIENT
DESCRIPTOR.message_types_by_name['FileRequest'] = _FILEREQUEST
DESCRIPTOR.message_types_by_name['FileResponse'] = _FILERESPONSE
DESCRIPTOR.message_types_by_name['RegisterPeerRequest'] = _REGISTERPEERREQUEST
DESCRIPTOR.message_types_by_name['RegisterPeerResponse'] = _REGISTERPEERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileHostingClient = _reflection.GeneratedProtocolMessageType('FileHostingClient', (_message.Message,), {
  'DESCRIPTOR' : _FILEHOSTINGCLIENT,
  '__module__' : 'server_to_client_pb2'
  # @@protoc_insertion_point(class_scope:FileHostingClient)
  })
_sym_db.RegisterMessage(FileHostingClient)

FileRequest = _reflection.GeneratedProtocolMessageType('FileRequest', (_message.Message,), {
  'DESCRIPTOR' : _FILEREQUEST,
  '__module__' : 'server_to_client_pb2'
  # @@protoc_insertion_point(class_scope:FileRequest)
  })
_sym_db.RegisterMessage(FileRequest)

FileResponse = _reflection.GeneratedProtocolMessageType('FileResponse', (_message.Message,), {
  'DESCRIPTOR' : _FILERESPONSE,
  '__module__' : 'server_to_client_pb2'
  # @@protoc_insertion_point(class_scope:FileResponse)
  })
_sym_db.RegisterMessage(FileResponse)

RegisterPeerRequest = _reflection.GeneratedProtocolMessageType('RegisterPeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPEERREQUEST,
  '__module__' : 'server_to_client_pb2'
  # @@protoc_insertion_point(class_scope:RegisterPeerRequest)
  })
_sym_db.RegisterMessage(RegisterPeerRequest)

RegisterPeerResponse = _reflection.GeneratedProtocolMessageType('RegisterPeerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPEERRESPONSE,
  '__module__' : 'server_to_client_pb2'
  # @@protoc_insertion_point(class_scope:RegisterPeerResponse)
  })
_sym_db.RegisterMessage(RegisterPeerResponse)



_NAPSTERSERVER = _descriptor.ServiceDescriptor(
  name='NapsterServer',
  full_name='NapsterServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=371,
  serialized_end=508,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterPeer',
    full_name='NapsterServer.RegisterPeer',
    index=0,
    containing_service=None,
    input_type=_REGISTERPEERREQUEST,
    output_type=_REGISTERPEERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPeersServingRequestedFile',
    full_name='NapsterServer.GetPeersServingRequestedFile',
    index=1,
    containing_service=None,
    input_type=_FILEREQUEST,
    output_type=_FILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NAPSTERSERVER)

DESCRIPTOR.services_by_name['NapsterServer'] = _NAPSTERSERVER

# @@protoc_insertion_point(module_scope)