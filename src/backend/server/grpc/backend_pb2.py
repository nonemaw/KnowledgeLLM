# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backend.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import obj_basic_pb2 as obj__basic__pb2
import obj_shared_pb2 as obj__shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbackend.proto\x1a\x0fobj_basic.proto\x1a\x10obj_shared.proto2\x83\x07\n\nGrpcServer\x12$\n\theartbeat\x12\x08.VoidObj\x1a\x0b.BooleanObj\"\x00\x12,\n\x0eget_task_state\x12\n.StringObj\x1a\x0c.TaskInfoObj\"\x00\x12)\n\x0cis_task_done\x12\n.StringObj\x1a\x0b.BooleanObj\"\x00\x12/\n\x12is_task_successful\x12\n.StringObj\x1a\x0b.BooleanObj\"\x00\x12(\n\x0b\x63\x61ncel_task\x12\n.StringObj\x1a\x0b.BooleanObj\"\x00\x12,\n\x0e\x63reate_library\x12\x0b.LibInfoObj\x1a\x0b.BooleanObj\"\x00\x12(\n\x0buse_library\x12\n.StringObj\x1a\x0b.BooleanObj\"\x00\x12+\n\x10\x64\x65molish_library\x12\x08.VoidObj\x1a\x0b.BooleanObj\"\x00\x12\x38\n\x12make_library_ready\x12\x14.LibGetReadyParamObj\x1a\n.StringObj\"\x00\x12/\n\x14get_current_lib_info\x12\x08.VoidObj\x1a\x0b.LibInfoObj\"\x00\x12\x31\n\x10get_library_list\x12\x08.VoidObj\x1a\x11.ListOfLibInfoObj\"\x00\x12\x35\n\x15get_library_path_list\x12\x08.VoidObj\x1a\x10.ListOfStringObj\"\x00\x12\'\n\nlib_exists\x12\n.StringObj\x1a\x0b.BooleanObj\"\x00\x12>\n\nquery_text\x12\x0f.DocLibQueryObj\x1a\x1d.ListOfDocLibQueryResponseObj\"\x00\x12N\n\x16image_for_image_search\x12\x11.ImageLibQueryObj\x1a\x1f.ListOfImageLibQueryResponseObj\"\x00\x12M\n\x15text_for_image_search\x12\x11.ImageLibQueryObj\x1a\x1f.ListOfImageLibQueryResponseObj\"\x00\x12\x39\n\x0eget_image_tags\x12\x11.ImageLibQueryObj\x1a\x12.ListOfImageTagObj\"\x00\x42\x03\x80\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'backend_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_GRPCSERVER']._serialized_start=53
  _globals['_GRPCSERVER']._serialized_end=952
# @@protoc_insertion_point(module_scope)
