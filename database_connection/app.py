import json
import sys
import logging
import rds_config
import pymysql
import os
import boto3

# rds settings
rds_host = "database-sami.cluster-cap1ismvex7k.ap-southeast-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    item_count = 0

    with conn.cursor() as cur:
        # cur.execute("drop table TblSupplier")
        # cur.execute(
        #     "create table TblSupplier(SuplierProductID varchar(25),productName varchar(50),productDescription varchar(50),productDetails varchar(50),productFeatured bool,productPrice int)")
        cur.execute('insert into TblSupplier  values("MZ123123", "Unstitch Cloths","This is best Product","Wholesale product",TRUE ,800)')
        conn.commit()
        cur.execute("select * from TblSupplier")
        for row in cur:
            item_count += 1
            logger.info(row)
            # print(row)
    conn.commit()

    return {
        'message': item_count
    }
