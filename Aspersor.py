from concurrent import futures
import grpc
import aspersor_pb2
import aspersor_pb2_grpc

class Aspersor():
    __HOSTIP__ = "10.43.101.87"
    __PORT__ = 65436

    def encenderAspersor(self, request, context):
        print("Aspersor Activado")
        return aspersor_pb2.ActivarRespuesta(message="Aspersor Activado Correctamente")
    
    def apagarAspersor(self, request, context):
        print("Aspersor desactivado")
        return aspersor_pb2.DesactivarRespuesta(message="Aspersor Desactivado Correctamente")

    def run_server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        aspersor_pb2_grpc.add_AspersorServiceServicer_to_server(self, server)
        server.add_insecure_port(f'{self.__HOSTIP__}:{self.__PORT__}')
        server.start()
        server.wait_for_termination()

if __name__ == "__main__":
    aspersor = Aspersor()
    aspersor.run_server()   