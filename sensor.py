from msvcrt import kbhit, getch
import grpc
import sensor_pb2
import sensor_pb2_grpc
import time
import random
import sys

#0 for smoke
#1 for temperature
#2 for humidity

VALUE_RANGES = [[0,1],[11,29.4],[70,100]]

class Sensor:
    def __init__(self, file_path, sensor_type):
        self.file_path = file_path
        if sensor_type == 0:
            self.sensor_type = sensor_type
            self.gen_interval = 3
        elif sensor_type == 1:
            self.sensor_type = sensor_type
            self.gen_interval = 6
        elif sensor_type == 2:
            self.sensor_type = sensor_type
            self.gen_interval = 5
        else:
            self.gen_interval = -1

        self.server_address = "localhost:50051"
        self.running = False

    def read_sensor_config(self):
        with open(self.file_path, 'r') as file:
            data = [float(line.strip()) for line in file]
        return data

    def generate_data(self):
        correct_count = 0
        incorrect_count = 0
        error_count = 0
        while self.running:
            if kbhit():
                getch()
                self.stop()
                break
            sensor_value = None
            sensor_config = self.read_sensor_config()
            correct = sensor_config[0] * 10
            incorrect = sensor_config[1] * 10
            error = sensor_config[2] * 10
            #we do a bit of trolling here

            #data generation for smoke sensor (only has correct and error values according to the pdf)
            #we also use int cuz its a boolean
            if(self.sensor_type == 0):
                if(correct_count < correct):
                    sensor_value = random.randint(VALUE_RANGES[self.sensor_type][0], VALUE_RANGES[self.sensor_type][1])
                    correct_count+=1
                elif (error_count < error):
                    sensor_value = random.randint(sys.float_info.min, -1)
                    error_count+=1
                else:
                    correct_count = 0
                    error_count = 0
            #the other sensors have the 3 (correct, incorrect and error)
            else:
                #this things can have floats so we use uniform
                if(correct_count < correct):
                    sensor_value = random.uniform(VALUE_RANGES[self.sensor_type][0], VALUE_RANGES[self.sensor_type][1])
                    correct_count+=1 
                elif (incorrect_count < incorrect):
                    belowOrAbove = random.randint(0, 1)
                    #below treshold or above treshold
                    if belowOrAbove == 0:
                        sensor_value = random.uniform(0, VALUE_RANGES[self.sensor_type][0]) 
                    else:
                        sensor_value = random.uniform(VALUE_RANGES[self.sensor_type][0], sys.float_info.max) 
                    incorrect_count+=1
                elif (error_count < error):
                    sensor_value = random.uniform(sys.float_info.min, -1)
                    error_count+=1
                else:
                    correct_count = 0
                    incorrect_count = 0
                    error_count = 0

            #we send the sensor data
            self.send_sensor_data(self.server_address, sensor_value)
            time.sleep(self.gen_interval)

    def send_sensor_data(self, server_address, sensValue):
        #try catch for not doing a bit of trolling here
        try:
            with grpc.insecure_channel(server_address) as channel:
                stub = sensor_pb2_grpc.SensorServiceStub(channel)
                response = stub.SendData(sensor_pb2.SensorData(value=sensValue))
                print("\nMessage sent to proxy")
            
        except grpc.RpcError as e:
            if isinstance(e, grpc._channel._Rendezvous) and e.code() == grpc.StatusCode.UNAVAILABLE:
                print("oops, no proxy available to receive the message")
            else:
                print("\nit seems like something went wrong with the grpc, here's the error message:")
                print(e)

    def start(self):
        if not self.running:
            self.running = True

    def stop(self):
        self.running = False
        print("\nSensor stopped by the user")

if __name__ == "__main__":
    file_path = "configuration.txt" 
    sensor_type = 1
    server_address = "localhost:50051"

    sensor = Sensor(file_path, sensor_type)
    if sensor.gen_interval != -1:
        sensor.start()
        sensor.generate_data()
    else:
        print("\nInvalid sensor data")
