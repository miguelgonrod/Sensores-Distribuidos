# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aspersor.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61spersor.proto\x12\tmyservice\"#\n\x10\x41\x63tivarSolicitud\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x10\x41\x63tivarRespuesta\x12\x0f\n\x07message\x18\x02 \x01(\t\"&\n\x13\x44\x65sactivarSolicitud\x12\x0f\n\x07message\x18\x03 \x01(\t\"&\n\x13\x44\x65sactivarRespuesta\x12\x0f\n\x07message\x18\x04 \x01(\t2\xb5\x01\n\x0f\x41spersorService\x12N\n\x10\x45ncenderAspersor\x12\x1b.myservice.ActivarSolicitud\x1a\x1b.myservice.ActivarRespuesta\"\x00\x12R\n\x0e\x41pagarAspersor\x12\x1e.myservice.DesactivarSolicitud\x1a\x1e.myservice.DesactivarRespuesta\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aspersor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ACTIVARSOLICITUD']._serialized_start=29
  _globals['_ACTIVARSOLICITUD']._serialized_end=64
  _globals['_ACTIVARRESPUESTA']._serialized_start=66
  _globals['_ACTIVARRESPUESTA']._serialized_end=101
  _globals['_DESACTIVARSOLICITUD']._serialized_start=103
  _globals['_DESACTIVARSOLICITUD']._serialized_end=141
  _globals['_DESACTIVARRESPUESTA']._serialized_start=143
  _globals['_DESACTIVARRESPUESTA']._serialized_end=181
  _globals['_ASPERSORSERVICE']._serialized_start=184
  _globals['_ASPERSORSERVICE']._serialized_end=365
# @@protoc_insertion_point(module_scope)
