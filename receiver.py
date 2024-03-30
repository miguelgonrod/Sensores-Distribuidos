import grpc
import sensor_pb2
import sensor_pb2_grpc
from concurrent import futures

class SensorService(sensor_pb2_grpc.SensorServiceServicer):
    def SendData(self, request, context):
        print("Received sensor data:", request.value)
        return sensor_pb2.SensorResponse(message="Data received successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensor_pb2_grpc.add_SensorServiceServicer_to_server(SensorService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started. Listening on port 50051.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()