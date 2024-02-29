from concurrent import futures
import grpc
from django.core.management.base import BaseCommand

from django_test.proto.ml_instance_pb2_grpc import add_MLInstanceServicer_to_server
from django_test.api.setup import MLInstanceAPI


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MLInstanceServicer_to_server(MLInstanceAPI(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

class Command(BaseCommand):
    help = "GRPC server"

    def handle(self, *args, **options):
        print('Successfully started grpc server ')
        serve()
