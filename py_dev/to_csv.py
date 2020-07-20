def get_key_list():
    map_list = []
    cluster_map = []
    cluster_id = ""
    for item in map_list['rows']:
        cluster_id += item['clusterId']
        cluster_id += ','
    print(cluster_id)
    print()


    taskList = []
    for item in map_list['rows']:
        row = []
        row.append(str(item['taskId']))
        row.append(item['taskName'])
        row.append(item['proposer'])
        row.append(item['proposerEmail'])
        row.append(item['clusterId'])
        row.append(item['clusterName'])
        counter = 0
        for cluster in cluster_map['dataList']:
            if cluster['id'] == item['clusterId'] and cluster['zone'] == 'default':
                row.append(cluster['proposer'])
                # row.append(cluster['zone'])
                taskList.append(row)
                counter += 1
        if counter == 0:
            print(','.join(row))
            print()

    for task in taskList:
        row_str = ','.join(task)
        print(row_str)

get_key_list()