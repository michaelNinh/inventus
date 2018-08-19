import csv
import sys
import consul
import psycopg2


def get_utms_from_csv(csvPath):
    f = open(csvPath)

    csv_f = csv.reader(f)

    utms_as_tuples = []

    firstline = True
    # the following converts readData into pythonData
    for row in csv_f:
        if firstline:
            firstline = False
            continue
        # create an object from row

        utm_tuple = (row[0],row[1],row[2])
        utms_as_tuples.append(utm_tuple)
        # print(utm_tuple)

    return utms_as_tuples

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

# import pandas as pd


# This maps to build/live_products.sql

utm_term = get_utms_from_csv('/Users/michaelninh/PycharmProjects/inventus/csvRaws/7%2F23 - 7%2F29 - get_7D_data.csv')




master_conversion_list = []

for utm in utm_term:

    one_day_data = []

    one_day_data.append(utm[0])


    # get number of buyers in timeframe
    cur.execute(

        """
    SELECT COUNT(*) FROM (
    select a.uid, a.product_id
    from estimated_transaction_sales a
    inner join ( select uid from analysis_user_sources
    where utm_term in (%s)) b
    on (a.uid=b.uid)
    where transaction_date between %s and %s
    group by 1,2
    limit 9999);
    """
        , utm)

    df_urls = cur.fetchall()
    one_day_data.append(df_urls[0][0])


    # get number of sign ups in timeframe
    cur.execute(
    """    
    select
    COUNT(*)
    from analysis_user_sources
    WHERE
    utm_medium='influencer' 
    AND utm_term=%s
    and date_registered between %s and %s
    """, utm
    )
    one_day_signs = cur.fetchall()
    one_day_data.append(one_day_signs[0][0])


    print(one_day_data)

    master_conversion_list.append(one_day_data)


print(master_conversion_list)

exportPath = '/Users/michaelninh/PycharmProjects/inventus/exports/test1D.csv'

with open(exportPath, 'w', encoding='utf-8') as csvfile:
    fieldnames = ['utm','1D conv','1D signs']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for utm_conversion in master_conversion_list:
        # dumboFormat is the format needed to correctly write into csv
        dumboFormat = {
            'utm':str(utm_conversion[0]),
            '1D conv':str(utm_conversion[1]),
            '1D signs':str(utm_conversion[2])
        }

        writer.writerow(dumboFormat)
print('SAVED TO MEMORY')

"""
referrer order for CSV

0 - UTM term
1 - source 
2 - UTM medium
3 - referrer 
4 - Count

"""
