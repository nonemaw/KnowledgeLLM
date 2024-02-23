# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import server.grpc.obj_basic_pb2 as obj__basic__pb2
import server.grpc.obj_shared_pb2 as obj__shared__pb2


class GrpcServerStub(object):
    """Server APIs
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.heartbeat = channel.unary_unary(
                '/GrpcServer/heartbeat',
                request_serializer=obj__basic__pb2.VoidObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.get_task_state = channel.unary_unary(
                '/GrpcServer/get_task_state',
                request_serializer=obj__basic__pb2.StringObj.SerializeToString,
                response_deserializer=obj__shared__pb2.TaskInfoObj.FromString,
                )
        self.is_task_done = channel.unary_unary(
                '/GrpcServer/is_task_done',
                request_serializer=obj__basic__pb2.StringObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.is_task_successful = channel.unary_unary(
                '/GrpcServer/is_task_successful',
                request_serializer=obj__basic__pb2.StringObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.cancel_task = channel.unary_unary(
                '/GrpcServer/cancel_task',
                request_serializer=obj__basic__pb2.StringObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.create_library = channel.unary_unary(
                '/GrpcServer/create_library',
                request_serializer=obj__shared__pb2.LibInfoObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.use_library = channel.unary_unary(
                '/GrpcServer/use_library',
                request_serializer=obj__basic__pb2.StringObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.demolish_library = channel.unary_unary(
                '/GrpcServer/demolish_library',
                request_serializer=obj__shared__pb2.LibInfoObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.make_library_ready = channel.unary_unary(
                '/GrpcServer/make_library_ready',
                request_serializer=obj__shared__pb2.LibGetReadyParamObj.SerializeToString,
                response_deserializer=obj__basic__pb2.StringObj.FromString,
                )
        self.get_current_lib_info = channel.unary_unary(
                '/GrpcServer/get_current_lib_info',
                request_serializer=obj__basic__pb2.VoidObj.SerializeToString,
                response_deserializer=obj__shared__pb2.LibInfoObj.FromString,
                )
        self.get_library_list = channel.unary_unary(
                '/GrpcServer/get_library_list',
                request_serializer=obj__basic__pb2.VoidObj.SerializeToString,
                response_deserializer=obj__shared__pb2.ListOfLibInfoObj.FromString,
                )
        self.get_library_path_list = channel.unary_unary(
                '/GrpcServer/get_library_path_list',
                request_serializer=obj__basic__pb2.VoidObj.SerializeToString,
                response_deserializer=obj__basic__pb2.ListOfStringObj.FromString,
                )
        self.lib_exists = channel.unary_unary(
                '/GrpcServer/lib_exists',
                request_serializer=obj__basic__pb2.StringObj.SerializeToString,
                response_deserializer=obj__basic__pb2.BooleanObj.FromString,
                )
        self.query = channel.unary_unary(
                '/GrpcServer/query',
                request_serializer=obj__shared__pb2.DocLibQueryObj.SerializeToString,
                response_deserializer=obj__shared__pb2.ListOfDocLibQueryResponseObj.FromString,
                )
        self.image_for_image_search = channel.unary_unary(
                '/GrpcServer/image_for_image_search',
                request_serializer=obj__shared__pb2.ImageLibQueryObj.SerializeToString,
                response_deserializer=obj__shared__pb2.ListOfImageLibQueryResponseObj.FromString,
                )
        self.text_for_image_search = channel.unary_unary(
                '/GrpcServer/text_for_image_search',
                request_serializer=obj__shared__pb2.ImageLibQueryObj.SerializeToString,
                response_deserializer=obj__shared__pb2.ListOfImageLibQueryResponseObj.FromString,
                )
        self.get_image_tags = channel.unary_unary(
                '/GrpcServer/get_image_tags',
                request_serializer=obj__shared__pb2.ImageLibQueryObj.SerializeToString,
                response_deserializer=obj__shared__pb2.ListOfImageTagObj.FromString,
                )


class GrpcServerServicer(object):
    """Server APIs
    """

    def heartbeat(self, request, context):
        """Heartbeat API
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_task_state(self, request, context):
        """Task APIs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def is_task_done(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def is_task_successful(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cancel_task(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_library(self, request, context):
        """Library manager APIs for library control
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def use_library(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def demolish_library(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def make_library_ready(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_current_lib_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_library_list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_library_path_list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def lib_exists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def query(self, request, context):
        """Document library APIs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def image_for_image_search(self, request, context):
        """Image library APIs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def text_for_image_search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_image_tags(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.heartbeat,
                    request_deserializer=obj__basic__pb2.VoidObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'get_task_state': grpc.unary_unary_rpc_method_handler(
                    servicer.get_task_state,
                    request_deserializer=obj__basic__pb2.StringObj.FromString,
                    response_serializer=obj__shared__pb2.TaskInfoObj.SerializeToString,
            ),
            'is_task_done': grpc.unary_unary_rpc_method_handler(
                    servicer.is_task_done,
                    request_deserializer=obj__basic__pb2.StringObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'is_task_successful': grpc.unary_unary_rpc_method_handler(
                    servicer.is_task_successful,
                    request_deserializer=obj__basic__pb2.StringObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'cancel_task': grpc.unary_unary_rpc_method_handler(
                    servicer.cancel_task,
                    request_deserializer=obj__basic__pb2.StringObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'create_library': grpc.unary_unary_rpc_method_handler(
                    servicer.create_library,
                    request_deserializer=obj__shared__pb2.LibInfoObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'use_library': grpc.unary_unary_rpc_method_handler(
                    servicer.use_library,
                    request_deserializer=obj__basic__pb2.StringObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'demolish_library': grpc.unary_unary_rpc_method_handler(
                    servicer.demolish_library,
                    request_deserializer=obj__shared__pb2.LibInfoObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'make_library_ready': grpc.unary_unary_rpc_method_handler(
                    servicer.make_library_ready,
                    request_deserializer=obj__shared__pb2.LibGetReadyParamObj.FromString,
                    response_serializer=obj__basic__pb2.StringObj.SerializeToString,
            ),
            'get_current_lib_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_current_lib_info,
                    request_deserializer=obj__basic__pb2.VoidObj.FromString,
                    response_serializer=obj__shared__pb2.LibInfoObj.SerializeToString,
            ),
            'get_library_list': grpc.unary_unary_rpc_method_handler(
                    servicer.get_library_list,
                    request_deserializer=obj__basic__pb2.VoidObj.FromString,
                    response_serializer=obj__shared__pb2.ListOfLibInfoObj.SerializeToString,
            ),
            'get_library_path_list': grpc.unary_unary_rpc_method_handler(
                    servicer.get_library_path_list,
                    request_deserializer=obj__basic__pb2.VoidObj.FromString,
                    response_serializer=obj__basic__pb2.ListOfStringObj.SerializeToString,
            ),
            'lib_exists': grpc.unary_unary_rpc_method_handler(
                    servicer.lib_exists,
                    request_deserializer=obj__basic__pb2.StringObj.FromString,
                    response_serializer=obj__basic__pb2.BooleanObj.SerializeToString,
            ),
            'query': grpc.unary_unary_rpc_method_handler(
                    servicer.query,
                    request_deserializer=obj__shared__pb2.DocLibQueryObj.FromString,
                    response_serializer=obj__shared__pb2.ListOfDocLibQueryResponseObj.SerializeToString,
            ),
            'image_for_image_search': grpc.unary_unary_rpc_method_handler(
                    servicer.image_for_image_search,
                    request_deserializer=obj__shared__pb2.ImageLibQueryObj.FromString,
                    response_serializer=obj__shared__pb2.ListOfImageLibQueryResponseObj.SerializeToString,
            ),
            'text_for_image_search': grpc.unary_unary_rpc_method_handler(
                    servicer.text_for_image_search,
                    request_deserializer=obj__shared__pb2.ImageLibQueryObj.FromString,
                    response_serializer=obj__shared__pb2.ListOfImageLibQueryResponseObj.SerializeToString,
            ),
            'get_image_tags': grpc.unary_unary_rpc_method_handler(
                    servicer.get_image_tags,
                    request_deserializer=obj__shared__pb2.ImageLibQueryObj.FromString,
                    response_serializer=obj__shared__pb2.ListOfImageTagObj.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GrpcServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GrpcServer(object):
    """Server APIs
    """

    @staticmethod
    def heartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/heartbeat',
            obj__basic__pb2.VoidObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_task_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/get_task_state',
            obj__basic__pb2.StringObj.SerializeToString,
            obj__shared__pb2.TaskInfoObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def is_task_done(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/is_task_done',
            obj__basic__pb2.StringObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def is_task_successful(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/is_task_successful',
            obj__basic__pb2.StringObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cancel_task(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/cancel_task',
            obj__basic__pb2.StringObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_library(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/create_library',
            obj__shared__pb2.LibInfoObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def use_library(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/use_library',
            obj__basic__pb2.StringObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def demolish_library(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/demolish_library',
            obj__shared__pb2.LibInfoObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def make_library_ready(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/make_library_ready',
            obj__shared__pb2.LibGetReadyParamObj.SerializeToString,
            obj__basic__pb2.StringObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_current_lib_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/get_current_lib_info',
            obj__basic__pb2.VoidObj.SerializeToString,
            obj__shared__pb2.LibInfoObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_library_list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/get_library_list',
            obj__basic__pb2.VoidObj.SerializeToString,
            obj__shared__pb2.ListOfLibInfoObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_library_path_list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/get_library_path_list',
            obj__basic__pb2.VoidObj.SerializeToString,
            obj__basic__pb2.ListOfStringObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def lib_exists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/lib_exists',
            obj__basic__pb2.StringObj.SerializeToString,
            obj__basic__pb2.BooleanObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/query',
            obj__shared__pb2.DocLibQueryObj.SerializeToString,
            obj__shared__pb2.ListOfDocLibQueryResponseObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def image_for_image_search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/image_for_image_search',
            obj__shared__pb2.ImageLibQueryObj.SerializeToString,
            obj__shared__pb2.ListOfImageLibQueryResponseObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def text_for_image_search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/text_for_image_search',
            obj__shared__pb2.ImageLibQueryObj.SerializeToString,
            obj__shared__pb2.ListOfImageLibQueryResponseObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_image_tags(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcServer/get_image_tags',
            obj__shared__pb2.ImageLibQueryObj.SerializeToString,
            obj__shared__pb2.ListOfImageTagObj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
