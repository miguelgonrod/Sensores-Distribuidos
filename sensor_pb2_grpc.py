# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sensor_pb2 as sensor__pb2


class SensorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendData = channel.unary_unary(
                '/panqueques.distribuidos.SensorService/SendData',
                request_serializer=sensor__pb2.SensorData.SerializeToString,
                response_deserializer=sensor__pb2.SensorResponse.FromString,
                )


class SensorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SensorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendData': grpc.unary_unary_rpc_method_handler(
                    servicer.SendData,
                    request_deserializer=sensor__pb2.SensorData.FromString,
                    response_serializer=sensor__pb2.SensorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'panqueques.distribuidos.SensorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SensorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/panqueques.distribuidos.SensorService/SendData',
            sensor__pb2.SensorData.SerializeToString,
            sensor__pb2.SensorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)