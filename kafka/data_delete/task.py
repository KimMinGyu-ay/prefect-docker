import time

from prefect import task, get_run_logger

from service.cmn.mapper import get_sql
from service.cmn import transaction as tx

# @task(retries=3)
# def delete_error_message():
#     """kafka_message 테이블에서 금일 날짜기준으로 이전 데이터 삭제
#     """
#     logger = get_run_logger()
#     start_time = time.time()
#     query = get_sql('KAFKA_MESSAGE_ERR_IN_DELETE_QUERY')
#     tx.postgresql_con('delete', query, [])
#     logger.info("Work that \"Kafka message data_delete\" finished  : ---{}s seconds---".format(time.time() - start_time))


from prefect.filesystems import GitHub

github_block = GitHub.load("test")
print(github_block)