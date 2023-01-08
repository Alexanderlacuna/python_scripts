
from urllib.parse import urlparse
import pymysql as mdb



def parse_db_url():
    """function to parse SQL_URI env variable note:there\
    is a default value for SQL_URI so a tuple result is\
    always expected"""
    parsed_db = urlparse(SQL_URI)


    return (
        parsed_db.hostname, parsed_db.username, parsed_db.password,
        parsed_db.path[1:], 3306)


# This function is deprecated. Use database_connection instead.
def database_connector():
    """function to create db connector"""
    host, user, passwd, db_name, db_port = parse_db_url()

    conn=mdb.connect(host=host,user=user,password=passwd,database=db_name)
    return conn

    #return mdb.connect(host, user, passwd, db_name, port=(db_port or 3306))


def get_probesetfreezes(conn):

	inbredsetid = 1

	with conn.cursor() as cursor:
		cursor.execute(
			"SELECT ProbeSetFreeze.Id, ProbeSetFreeze.Name, ProbeSetFreeze.FullName "
    		"FROM ProbeSetFreeze, ProbeFreeze "
    		"WHERE ProbeSetFreeze.ProbeFreezeId=ProbeFreeze.Id "
    		"AND ProbeFreeze.InbredSetId=%s",
    		(inbredsetid,)
			)

		results = cursor.fetchall()
		return results


def get_strains(conn,inbredsetid=1):

	inbredsetid = 1

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
conn = database_connector()

db_name = "HC_M2_0606_P"



def fetch_datasets(conn):
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
	    results_v  = cursor.fetchall()

	return results_v
 


# store the results in sparql



def parse_dataset(results):
	ids = ["ID"]
	data = {}
	for (trait, strain,val) in results:
		if strain  not in ids:
			ids.append(strain)

		if trait in data:
			data[trait].append(val)
		else:
			data[trait] = [trait,val]

	return (data,ids)





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



results = get_probesetfreezes(conn=conn)


results2 = get_strains(conn=conn)

results3 = fetch_datasets(conn=conn) # to be improved

breakpoint()