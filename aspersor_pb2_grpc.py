# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import aspersor_pb2 as aspersor__pb2


class AspersorServiceStub(object):
    def __init__(self, channel):
        self.EncenderAspersor = channel.unary_unary(
                '/myservice.AspersorService/EncenderAspersor',
                request_serializer=aspersor__pb2.ActivarSolicitud.SerializeToString,
                response_deserializer=aspersor__pb2.ActivarRespuesta.FromString,
                )
        self.ApagarAspersor = channel.unary_unary(
                '/myservice.AspersorService/ApagarAspersor',
                request_serializer=aspersor__pb2.DesactivarSolicitud.SerializeToString,
                response_deserializer=aspersor__pb2.DesactivarRespuesta.FromString,
                )


class AspersorServiceServicer(object):
    def EncenderAspersor(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApagarAspersor(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AspersorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EncenderAspersor': grpc.unary_unary_rpc_method_handler(
                    servicer.EncenderAspersor,
                    request_deserializer=aspersor__pb2.ActivarSolicitud.FromString,
                    response_serializer=aspersor__pb2.ActivarRespuesta.SerializeToString,
            ),
            'ApagarAspersor': grpc.unary_unary_rpc_method_handler(
                    servicer.ApagarAspersor,
                    request_deserializer=aspersor__pb2.DesactivarSolicitud.FromString,
                    response_serializer=aspersor__pb2.DesactivarRespuesta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'myservice.AspersorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AspersorService(object):
    @staticmethod
    def EncenderAspersor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/myservice.AspersorService/EncenderAspersor',
            aspersor__pb2.ActivarSolicitud.SerializeToString,
            aspersor__pb2.ActivarRespuesta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ApagarAspersor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/myservice.AspersorService/ApagarAspersor',
            aspersor__pb2.DesactivarSolicitud.SerializeToString,
            aspersor__pb2.DesactivarRespuesta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)