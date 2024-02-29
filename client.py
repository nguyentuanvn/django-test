from django_test.proto import ml_instance_pb2, ml_instance_pb2_grpc
import grpc


def setup():
    channel = grpc.insecure_channel("localhost:50051")
    client = ml_instance_pb2_grpc.MLInstanceStub(channel)
    response = client.setup(ml_instance_pb2.MLInstanceSetup(name="test", token="test"))
    print(response)

def import_mldata():
    channel = grpc.insecure_channel("localhost:50051")
    client = ml_instance_pb2_grpc.MLInstanceStub(channel)
    request = ml_instance_pb2.MLImport()
    files = {
        "file_1": b"test",
        "file_2": b"test file 2"
    }
    base64 = {
        "file_3": "test"
    }
    for file_name, file_data in files.items():
        f = ml_instance_pb2.MLData(filename=file_name, file_content=file_data)
        request.data.append(f)
    for file_name, file_data in base64.items():
        f = ml_instance_pb2.MLData(filename=file_name, base64_content=file_data)
        request.data.append(f)
    response = client.import_data(request)
    print(response)

if __name__ == "__main__":
    setup()
    import_mldata()