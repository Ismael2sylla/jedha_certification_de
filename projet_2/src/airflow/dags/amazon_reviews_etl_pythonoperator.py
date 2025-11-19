from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import yaml
from etl.extract import run_extract
from etl.transform import run_transform
from etl.model import run_model

def load_cfg():
    with open("config/config.yaml","r",encoding="utf-8") as f:
        return yaml.safe_load(f)

def task_extract(**context):
    cfg = load_cfg()
    res = run_extract(cfg)
    context['ti'].xcom_push(key="batch_id", value=res["batch_id"])

def task_transform(**context):
    cfg = load_cfg()
    batch_id = context['ti'].xcom_pull(key="batch_id", task_ids="extract")
    run_transform(cfg, batch_id=batch_id)

def task_model(**context):
    cfg = load_cfg()
    batch_id = context['ti'].xcom_pull(key="batch_id", task_ids="extract")
    run_model(cfg, batch_id=batch_id)

default_args = {"owner":"data-team","retries":1,"retry_delay":timedelta(minutes=5)}
with DAG(
    dag_id="amazon_reviews_etl_python",
    start_date=datetime(2025,1,1),
    schedule="0 2 * * *",
    catchup=False,
    default_args=default_args,
    tags=["etl","amazon","pythonoperator"]
) as dag:
    extract = PythonOperator(task_id="extract", python_callable=task_extract, provide_context=True)
    transform = PythonOperator(task_id="transform", python_callable=task_transform, provide_context=True)
    model = PythonOperator(task_id="model", python_callable=task_model, provide_context=True)
    extract >> transform >> model
