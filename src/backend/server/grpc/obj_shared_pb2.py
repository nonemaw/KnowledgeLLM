# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: obj_shared.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10obj_shared.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"D\n\nLibInfoObj\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\".\n\x10ListOfLibInfoObj\x12\x1a\n\x05value\x18\x01 \x03(\x0b\x32\x0b.LibInfoObj\"W\n\x13LibGetReadyParamObj\x12\x12\n\nforce_init\x18\x01 \x01(\x08\x12\x15\n\rrelative_path\x18\x02 \x01(\t\x12\x15\n\rprovider_type\x18\x03 \x01(\t\"\xff\x01\n\x0bTaskInfoObj\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x13\n\x0bphase_count\x18\x03 \x01(\x05\x12\x12\n\nphase_name\x18\x04 \x01(\t\x12\x15\n\rcurrent_phase\x18\x05 \x01(\x05\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12\r\n\x05\x65rror\x18\x07 \x01(\t\x12\x30\n\x0csubmitted_on\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x63ompleted_on\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x64uration\x18\n \x01(\x05\"=\n\x0e\x44ocLibQueryObj\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05top_k\x18\x02 \x01(\x05\x12\x0e\n\x06rerank\x18\x03 \x01(\x08\"\xa1\x01\n\x16\x44ocLibQueryResponseObj\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x10\n\x08reply_to\x18\x05 \x01(\t\x12\x17\n\x0freplied_message\x18\x06 \x01(\t\"F\n\x1cListOfDocLibQueryResponseObj\x12&\n\x05value\x18\x01 \x03(\x0b\x32\x17.DocLibQueryResponseObj\"C\n\x10ImageLibQueryObj\x12\x12\n\nimage_data\x18\x01 \x01(\t\x12\r\n\x05top_k\x18\x02 \x01(\x05\x12\x0c\n\x04text\x18\x03 \x01(\t\"H\n\x18ImageLibQueryResponseObj\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\"J\n\x1eListOfImageLibQueryResponseObj\x12(\n\x05value\x18\x01 \x03(\x0b\x32\x19.ImageLibQueryResponseObj\".\n\x0bImageTagObj\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\"0\n\x11ListOfImageTagObj\x12\x1b\n\x05value\x18\x01 \x03(\x0b\x32\x0c.ImageTagObjb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'obj_shared_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LIBINFOOBJ']._serialized_start=53
  _globals['_LIBINFOOBJ']._serialized_end=121
  _globals['_LISTOFLIBINFOOBJ']._serialized_start=123
  _globals['_LISTOFLIBINFOOBJ']._serialized_end=169
  _globals['_LIBGETREADYPARAMOBJ']._serialized_start=171
  _globals['_LIBGETREADYPARAMOBJ']._serialized_end=258
  _globals['_TASKINFOOBJ']._serialized_start=261
  _globals['_TASKINFOOBJ']._serialized_end=516
  _globals['_DOCLIBQUERYOBJ']._serialized_start=518
  _globals['_DOCLIBQUERYOBJ']._serialized_end=579
  _globals['_DOCLIBQUERYRESPONSEOBJ']._serialized_start=582
  _globals['_DOCLIBQUERYRESPONSEOBJ']._serialized_end=743
  _globals['_LISTOFDOCLIBQUERYRESPONSEOBJ']._serialized_start=745
  _globals['_LISTOFDOCLIBQUERYRESPONSEOBJ']._serialized_end=815
  _globals['_IMAGELIBQUERYOBJ']._serialized_start=817
  _globals['_IMAGELIBQUERYOBJ']._serialized_end=884
  _globals['_IMAGELIBQUERYRESPONSEOBJ']._serialized_start=886
  _globals['_IMAGELIBQUERYRESPONSEOBJ']._serialized_end=958
  _globals['_LISTOFIMAGELIBQUERYRESPONSEOBJ']._serialized_start=960
  _globals['_LISTOFIMAGELIBQUERYRESPONSEOBJ']._serialized_end=1034
  _globals['_IMAGETAGOBJ']._serialized_start=1036
  _globals['_IMAGETAGOBJ']._serialized_end=1082
  _globals['_LISTOFIMAGETAGOBJ']._serialized_start=1084
  _globals['_LISTOFIMAGETAGOBJ']._serialized_end=1132
# @@protoc_insertion_point(module_scope)
