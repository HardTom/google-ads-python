# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/errors/change_status_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/errors/change_status_error.proto',
  package='google.ads.googleads.v6.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.errorsB\026ChangeStatusErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Errors\312\002\036Google\\Ads\\GoogleAds\\V6\\Errors\352\002\"Google::Ads::GoogleAds::V6::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads_v6/proto/errors/change_status_error.proto\x12\x1egoogle.ads.googleads.v6.errors\x1a\x1cgoogle/api/annotations.proto\"\xd6\x01\n\x15\x43hangeStatusErrorEnum\"\xbc\x01\n\x11\x43hangeStatusError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12START_DATE_TOO_OLD\x10\x03\x12\x1e\n\x1a\x43HANGE_DATE_RANGE_INFINITE\x10\x04\x12\x1e\n\x1a\x43HANGE_DATE_RANGE_NEGATIVE\x10\x05\x12\x17\n\x13LIMIT_NOT_SPECIFIED\x10\x06\x12\x18\n\x14INVALID_LIMIT_CLAUSE\x10\x07\x42\xf1\x01\n\"com.google.ads.googleads.v6.errorsB\x16\x43hangeStatusErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Errors\xea\x02\"Google::Ads::GoogleAds::V6::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CHANGESTATUSERRORENUM_CHANGESTATUSERROR = _descriptor.EnumDescriptor(
  name='ChangeStatusError',
  full_name='google.ads.googleads.v6.errors.ChangeStatusErrorEnum.ChangeStatusError',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='START_DATE_TOO_OLD', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_DATE_RANGE_INFINITE', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHANGE_DATE_RANGE_NEGATIVE', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIMIT_NOT_SPECIFIED', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LIMIT_CLAUSE', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_CHANGESTATUSERRORENUM_CHANGESTATUSERROR)


_CHANGESTATUSERRORENUM = _descriptor.Descriptor(
  name='ChangeStatusErrorEnum',
  full_name='google.ads.googleads.v6.errors.ChangeStatusErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHANGESTATUSERRORENUM_CHANGESTATUSERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=343,
)

_CHANGESTATUSERRORENUM_CHANGESTATUSERROR.containing_type = _CHANGESTATUSERRORENUM
DESCRIPTOR.message_types_by_name['ChangeStatusErrorEnum'] = _CHANGESTATUSERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeStatusErrorEnum = _reflection.GeneratedProtocolMessageType('ChangeStatusErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CHANGESTATUSERRORENUM,
  '__module__' : 'google.ads.googleads_v6.proto.errors.change_status_error_pb2'
  ,
  '__doc__': """Container for enum describing possible change status errors.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.errors.ChangeStatusErrorEnum)
  })
_sym_db.RegisterMessage(ChangeStatusErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)