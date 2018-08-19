import csv
import sys
import consul
import psycopg2


def consul_get(host=None):
    try:
        client = consul.Consul(host=host)
        _, data = client.kv.get('env_vars/prod/common/redshift/', recurse=True)
        return data
    except:
        return None


def redshift_credentials():
    print("trying localhost")
    data = consul_get()
    if data is None:
        print("trying consul-cli.massdrop.com")
        data = consul_get('consul-cli.massdrop.com')
    if data is None:
        raise ValueError('Cannot reach consul :sad-face:')

    dict = {}
    for kv in data:
        key = kv['Key'].rsplit('/', 1)[-1]
        if len(key):
            dict[key] = kv['Value'].decode("utf-8")

    return dict


def redshift_client():
    data = redshift_credentials()
    print('conneccting to redshift')
    conn = psycopg2.connect(
        host=data['md_redshift_hostname'],
        user=data['md_redshift_ro_username'],
        port=int(data['md_redshift_port']),
        password=data['md_redshift_ro_password'],
        dbname=data['md_redshift_db'])

    return conn


conn = redshift_client()
cur = conn.cursor()
print('connected!')

cur.execute(
"""
select
    COUNT(*)
 from analysis_user_sources
 WHERE
 utm_medium='influencer' 
 AND utm_term='15757'
 and date_registered between '2017-01-01' and '2018-10-01'
"""

        )

df_urls = cur.fetchall()
print(df_urls)