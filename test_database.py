
import time
import argparse
import functools
import numpy as np
from io import BytesIO
from urllib.parse import urlparse
import pymysql as mdb
import os
import csv
import lmdb


def parse_db_url(sql_url):
    """function to parse SQL_URI env varible note:there\
    is a default value for SQL_URI so a tuple result is\
    always expected"""
    parsed_db = urlparse(sql_url)

    return (
        parsed_db.hostname, parsed_db.username, parsed_db.password,
        parsed_db.path[1:], 3306)


# This function is deprecated. Use database_connection instead.
def database_connector(sql_url):
    """function to create db connector"""
    host, user, passwd, db_name, db_port = parse_db_url(sql_url)
    return mdb.connect(host=host, user=user, password=passwd, database=db_name)

    # return mdb.connect(host, user, passwd, db_name, port=(db_port or 3306))


def get_probesetfreezes(conn, inbredsetid=1):

    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT ProbeSetFreeze.Id, ProbeSetFreeze.Name, ProbeSetFreeze.FullName "
            "FROM ProbeSetFreeze, ProbeFreeze "
            "WHERE ProbeSetFreeze.ProbeFreezeId=ProbeFreeze.Id "
            "AND ProbeFreeze.InbredSetId=%s",
            (inbredsetid,)
        )

        return cursor.fetchall()  # todo monads


def get_strains(conn, inbredsetid=1):

    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT Strain.Id, Strain.Name "
            "FROM StrainXRef, Strain "
            "WHERE StrainXRef.InbredSetId=%s "
            "AND StrainXRef.StrainId=Strain.Id "
            "ORDER BY StrainXRef.OrderId",
            (inbredsetid)
        )

        return cursor.fetchall()


def probesetfreeze_list():
    inbredsetid = 112


SQL_URI = "mysql://kabui:1234@localhost/db_webqtl"
#SQL_URI = "mysql://webqtlout:webqtlout@localhost/db_webqtl"
#conn = database_connector()

db_name = "HC_M2_0606_P"


def fetch_datasets(conn, db_name):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT ProbeSet.Name, Strain.Name, ProbeSetData.value "
            "FROM Strain LEFT JOIN ProbeSetData "
            "ON Strain.Id = ProbeSetData.StrainId "
            "LEFT JOIN ProbeSetXRef ON ProbeSetData.Id = ProbeSetXRef.DataId "
            "LEFT JOIN ProbeSet ON ProbeSetXRef.ProbeSetId = ProbeSet.Id "
            "WHERE ProbeSetXRef.ProbeSetFreezeId IN "
            "(SELECT Id FROM ProbeSetFreeze WHERE Name = %s) "
            "ORDER BY Strain.Name",
            (db_name,))
        return cursor.fetchall()  # use of maybe'


def get_probesetfreeze(conn, probes):

    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT ProbeSetFreeze.Id, ProbeSetFreeze.Name, ProbeSetFreeze.FullName "
            "FROM ProbeSetFreeze "
            "WHERE ProbeSetFreeze.Id=%s",
            (probes,)
        )
        return cursor.fetchone()

# store the results in sparql


def query_for_last_modification(conn):
    # database engine innodb check for both
    pass


def parse_dataset(results):
    ids = ["ID"]
    data = {}
    for (trait, strain, val) in results:
        if strain not in ids:
            ids.append(strain)

        if trait in data:
            data[trait].append(val)
        else:
            data[trait] = [trait, val]

    return (data, ids)


# above refactor the code

def generate_csv_file(conn, db_name, txt_dir, file_name):

    # write to file

    # file name ,file expiry,type of storage

    # I want to use lmdb to store the files
    # file name already done  #import that

    # file expiry to be done lt

    try:
        (data, col_ids) = parse_dataset(fetch_probeset_data(conn, db_name))
        with open(os.path.join(txt_dir, file_name), "w+", encoding='UTF8') as file_handler:

            writer = csv.writer(file_handler)
            writer.writerow(col_ids)  # write header s
            writer.writerows(val for val in data.values())
            return "success"

    except Exception as e:
        raise e


# write into matrix data matrix

def __get_strain_col__(results):
    ids = ["ID"]
    data = {}
    for (trait, strain, val) in results:
        if strain not in ids:
            ids.append(strain)
        if trait in data:
            data[trait].append(val)
        else:
            data[trait] = [trait, val]
    return (data, ids)


# https://stackoverflow.com/questions/53376786/convert-byte-array-back-to-numpy-array


def array_to_bytes(x: np.ndarray) -> bytes:
    np_bytes = BytesIO()

    np.save(np_bytes, x, allow_pickle=True)
    return (np_bytes.getvalue())


def bytes_to_array(b: bytes) -> np.ndarray:
    np_bytes = BytesIO(b)
    return np.load(np_bytes, allow_pickle=True)

# def generate_tmp_file()


def fetch_probeset_data(conn, inbredsetid=1):

    for (_id, shortname, fullname) in get_probesetfreezes(conn):
        return fetch_datasets(conn, db_name=shortname)


#results = get_probesetfreezes(conn=conn)


#results2 = get_strains(conn=conn)

# results3 = fetch_datasets(conn=conn) # to be improved

#results4 = get_probesetfreeze(conn=conn,probes=112)
#results5 = fetch_probeset_data(conn)
# breakpoint()


#results_6 = (data, col_ids) = parse_dataset(fetch_probeset_data(conn, db_name))

"""
data_list = np.array(list(data.values()))

map_size = data_list.nbytes*10

env = lmdb.open("txxx", map_size=map_size)
with env.begin(write=True) as txn:

    txn.put(str("HC_M2_0606_P").encode(), array_to_bytes(data_list))
"""

"""

env = lmdb.open('txxx', readonly=True)
with env.begin() as txn:
    raw_datum = bytes_to_array(txn.get(b'HC_M2_0606_P'))


breakpoint()

results = generate_file(conn, db_name)
"""

"""

SELECT database_name,table_name,last_update FROM
  mysql.innodb_table_stats a,
  (SELECT database_name AS db_last_update_name,
       max(last_update) AS db_last_update 
   FROM mysql.innodb_table_stats 
   WHERE database_name  in ( "db_webqtl")
   GROUP BY database_name )  AS b 
WHERE a.database_name = b.db_last_update_name

  AND a.last_update = b.db_last_update ;

"""

"""

import  lmdb
import os
import tempfile
with tempfile.TemporaryDirectory() as tmpdirname:

    tmp_file_path = os.path.join(tmpdirname,"img_lmdb")
    breakpoint()
    db = lmdb.open(tmp_file_path, map_size=int(1e12))

    with db.begin(write=True) as in_txn:
        in_txn.put("hello".encode(), "data_str".encode())

    db.close()

"""


def lmdb_error_handler(func):
    @functools.wraps(func)
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except lmdb.Error as error:
            print(f"{func.__name__} >>>> error . {str(error)}")
            return None
    return inner_function


@lmdb_error_handler
def create_dataset(file_path, db_name, col_names, dataset: np.ndarray):
    # map size int(ie12)
    # code to matrixify the arrays
    with lmdb.open(file_path, map_size=dataset.nbytes*10) as env:
        with env.begin(write=True) as txn:
            # txn.put(f"{db_name}:{col_names}".encode(),db_name['cols'].encode())
            # txn.put(f"{db_name}:{row_count}".encode(),db_name["rows"].encode())
            txn.put(db_name.encode(), array_to_bytes(dataset))
            txn.put(f"{db_name}:cols".encode(), array_to_bytes(col_names))
            return (file_path, db_name)

# @lmdb_error_Handler


@lmdb_error_handler
def read_dataset(file_name, db_name):
   # try:
    with lmdb.open(file_name, readonly=True, create=False) as env:
        with env.begin() as txn:
            results = txn.get(db_name.encode())
            col_names = txn.get(f"{db_name}:cols".encode())
            if results and col_names:
                return (bytes_to_array(col_names), bytes_to_array(results))
    # except lmdb.Error as  error:
    #    return None
            # convert from bytes to array

    # col_names
    # create time
    # number of dataset
    # number of columns


# create_dataset("twww","HC_M2_0606_P",col_ids,np.array(list(data.values())))

# dict insertion
# improvements to be made have key value inserts

init_time = time.time()
#results = read_dataset("twww","HC_M2_0606_P")


results = ""
end_time = time.time() - init_time
print(results)
print(end_time)


def generate_one(args, parser):
    # we require the dataset name
    try:
        return ""
    except Exception as e:
        raise e



#(data, col_ids) = parse_dataset(fetch_probeset_data(conn, db_name))


def generate_all(args, parser):
    # db_connection
    try:
        # move this to a single function
        conn = database_connector(args.database)
        for (_id, db_name,full_name) in  get_probesetfreezes(conn):

            print(f">>>>>>generating>>>>>>>{full_name} ::{db_name}")
            (data,col_ids) = parse_dataset(fetch_datasets(conn,db_name))
            if data:
                return create_dataset(os.path.join("/tmp/",full_name),db_name, col_ids, np.array(list(data.values())))
    except Exception as error:
        raise error

parser = argparse.ArgumentParser(prog="text_file generator")


parser.add_argument(
    "-a",
    "--all",
    dest="accumulate",
    action="store_const",
    const=generate_all,
    help="fetch all textfiles.",
)

parser.add_argument(
    "-o",
    "--one",
    dest="accumulate",
    action="store_const",
    const=generate_one,
    help="generate spefic textfile"
)


parser.add_argument(
    "-d",
    "--database",
    metavar="DB",
    type=str,
    default="db_webqtl_s",
    help="Use database (default db_webqtl_s)",
)


parser.add_argument(
    "-t",
    "--tmpdir",
    type=str,
    default="/tmp/",
    help="tempdir path to generate the files",
)


args = parser.parse_args()

args.accumulate(args, parser)

print(read_dataset("twww", "HC_M2_0606_P"))
