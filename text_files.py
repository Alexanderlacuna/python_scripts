

def fetch_text_file(dataset_name, text_dir,conn):
    with conn.cursor() as cursor:
        query = 'SELECT Id, FullName FROM ProbeSetFreeze WHERE Name = "%s"' % dataset_name
        cursor.execute(query)
        results = cursor.fetchone()
    if (results):
        for file in os.listdir(text_dir):
            if file.startswith(f"ProbeSetFreezeId_{results[0]}_"):
                return os.path.join(text_dir, file)

    # use backup catch in temp

def read_text_file(sample_dict, file_path):

    def parse_line_csv(line):
        return_list = line.split('","')
        return_list[-1] = return_list[-1][:-2]
        return_list[0] = return_list[0][1:]
        return return_list

    def __fetch_id_positions__(all_ids, target_ids):
        _vals = []
        _posit = []

        for (idx, strain) in enumerate(all_ids):
            if strain in target_ids:
                _vals.append(target_ids[strain])
                _posit.append(idx)
            else:
                _vals.append(0)  # todo on rust

        return (_posit, _vals) 
    with open(file_path, "r") as file_handler:
        all_ids = file_handler.readline()
        _posit, sample_vals = __fetch_id_positions__(
            parse_line_csv(all_ids)[1:], sample_dict)

        return (sample_vals, [",".join(parse_line_csv(line)) for line in file_handler.readlines()])

count = 0
while (count < 5):
    print("hello")

exit()