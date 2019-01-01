import pandas
import datetime
from jinja2 import Template

from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta
#from func import *


def make_hotel_table(**kwargs):
    # データ取得するsqlの実行
    #実行日時の取得
    execution_date = kwargs.get('execution_date').date()
    prev_execution_date = execution_date - datetime.timedelta(days=1)
    with open("make_hotel_table.sql", 'r') as f:
        sql = " ".join(f.readlines())

    sql = Template(sql).render(date_from=prev_execution_date, date_to=execution_date)

    conn = pymssql.connect(server='test', port='test', user='test', password='test')
    data = pd.read_sql_query(sql, conn)
    data.to_csv('hotel_table.csv')

    return True

default_args = {
    'owner': 'ikyu',
    # いつからデータをためるかを定義
    'start_date': datetime(2017, 10, 1),
}

dag = DAG(
    'ikyu_etl', default_args=default_args, schedule_interval='@daily') # いつ実行するかを定義

make_hotel_table = PythonOperator(
    task_id='make_hotel_table',
    provide_context=True,
    python_callable=make_hotel_table,
    dag=dag
)

make_hotel_table
