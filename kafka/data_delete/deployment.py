from service.cmn import const
from service.api import client, deployment

from flow import data_delete_flow

from prefect.server.schemas.schedules import CronSchedule


# agent가 실행할 job이 배포가 안 되어 있으면 배포
if "KAFKA_TABLE_DELETE" not in client.flow_list:
    param = const.DEPLOYMENT_FORMAT.copy()
    param["flow"] = data_delete_flow
    param["name"] = "KAFKA_TABLE_DELETE"
    param["schedule"] = CronSchedule(cron="15 00 * * *", timezone="Asia/Seoul")
    param["work_queue_name"] = "kafka"
    param["tags"] = ["kafka", "ERR_IN", "delete"]

    deployment.deployment_build(param)

