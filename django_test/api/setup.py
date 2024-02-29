from django_test.proto.ml_instance_pb2 import MLInstanceSetup, MLInstanceResponse, MLImportResponse
from django_test.proto.ml_instance_pb2_grpc import MLInstanceServicer
from django_test.models import MLInstance


class MLInstanceAPI(MLInstanceServicer):
    def setup(self, request, context):
        r = MLInstance(name=request.name)
        r.save()
        response = MLInstanceResponse(
            name=r.name,
            status=r.status
        )
        return response

    def import_data(self, request, context):
        result = []
        for f in request.data:
            result.append(f.filename)
        return MLImportResponse(filename=result)

    def predict(self, request, context):
        pass
    def export(self, request, context):
        pass

    def create_dataset(self, request, context):
        pass

    def logs(self, request, context):
        pass

    def download_checkpoint(self, request, context):
        pass