# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csensor.proto\x12\x17panqueques.distribuidos\"\x1b\n\nSensorData\x12\r\n\x05value\x18\x01 \x01(\x02\"=\n\x0eSensorResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x61ta_sent_to_proxy\x18\x02 \x01(\t2k\n\rSensorService\x12Z\n\x08SendData\x12#.panqueques.distribuidos.SensorData\x1a\'.panqueques.distribuidos.SensorResponse\"\x00\x42\"Z panqueques.distribuidos.sensorpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z panqueques.distribuidos.sensorpb'
  _globals['_SENSORDATA']._serialized_start=41
  _globals['_SENSORDATA']._serialized_end=68
  _globals['_SENSORRESPONSE']._serialized_start=70
  _globals['_SENSORRESPONSE']._serialized_end=131
  _globals['_SENSORSERVICE']._serialized_start=133
  _globals['_SENSORSERVICE']._serialized_end=240
# @@protoc_insertion_point(module_scope)
