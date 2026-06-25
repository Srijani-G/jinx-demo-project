"""Nightly ETL DAG: orchestrates the analytics warehouse load (Airflow).

Schedules extract -> transform -> load tasks every night and enforces
task dependencies so the warehouse refresh is deterministic.
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract():
    ...


def transform():
    ...


def load_warehouse():
    ...


with DAG(
    dag_id="nightly_etl",
    schedule="0 2 * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load_warehouse", python_callable=load_warehouse)
    e >> t >> l