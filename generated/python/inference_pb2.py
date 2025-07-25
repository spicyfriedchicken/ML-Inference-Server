# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: inference.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'inference.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finference.proto\x12\tinference\"\xe9\x01\n\x10InferenceRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12\x12\n\ninput_data\x18\x03 \x01(\x0c\x12;\n\x08metadata\x18\x04 \x03(\x0b\x32).inference.InferenceRequest.MetadataEntry\x12\x14\n\x0c\x63ontent_type\x18\x05 \x01(\t\x12\x19\n\x11request_timestamp\x18\x06 \x01(\x03\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8d\x02\n\x11InferenceResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x13\n\x0boutput_data\x18\x02 \x01(\x0c\x12\x41\n\x0boutput_meta\x18\x03 \x03(\x0b\x32,.inference.InferenceResponse.OutputMetaEntry\x12*\n\x0bstatus_code\x18\x04 \x01(\x0e\x32\x15.inference.StatusCode\x12\x15\n\rerror_message\x18\x05 \x01(\t\x12\x1a\n\x12response_timestamp\x18\x06 \x01(\x03\x1a\x31\n\x0fOutputMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*w\n\nStatusCode\x12\r\n\tSTATUS_OK\x10\x00\x12\x10\n\x0cSTATUS_ERROR\x10\x01\x12\x18\n\x14STATUS_INVALID_INPUT\x10\x02\x12\x1a\n\x16STATUS_MODEL_NOT_FOUND\x10\x03\x12\x12\n\x0eSTATUS_TIMEOUT\x10\x04\x32V\n\x10InferenceService\x12\x42\n\x05Infer\x12\x1b.inference.InferenceRequest\x1a\x1c.inference.InferenceResponseB\rZ\x0binferencepbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\013inferencepb'
  _globals['_INFERENCEREQUEST_METADATAENTRY']._loaded_options = None
  _globals['_INFERENCEREQUEST_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_INFERENCERESPONSE_OUTPUTMETAENTRY']._loaded_options = None
  _globals['_INFERENCERESPONSE_OUTPUTMETAENTRY']._serialized_options = b'8\001'
  _globals['_STATUSCODE']._serialized_start=538
  _globals['_STATUSCODE']._serialized_end=657
  _globals['_INFERENCEREQUEST']._serialized_start=31
  _globals['_INFERENCEREQUEST']._serialized_end=264
  _globals['_INFERENCEREQUEST_METADATAENTRY']._serialized_start=217
  _globals['_INFERENCEREQUEST_METADATAENTRY']._serialized_end=264
  _globals['_INFERENCERESPONSE']._serialized_start=267
  _globals['_INFERENCERESPONSE']._serialized_end=536
  _globals['_INFERENCERESPONSE_OUTPUTMETAENTRY']._serialized_start=487
  _globals['_INFERENCERESPONSE_OUTPUTMETAENTRY']._serialized_end=536
  _globals['_INFERENCESERVICE']._serialized_start=659
  _globals['_INFERENCESERVICE']._serialized_end=745
# @@protoc_insertion_point(module_scope)
