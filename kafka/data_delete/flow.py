from prefect import flow
from task import delete_error_message

from prefect.infrastructure import docker
@flow(description='This flow consist of a task that is responsible for deleting kafka_message data')
def data_delete_flow():
    """ kafka_message 테이블에 있는 데이터를 금일 날짜 기준으로 이전 데이터를 삭제하는 flow
    """
    delete_error_message()

