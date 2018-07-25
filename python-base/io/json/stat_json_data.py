import json


FILE_PATH = r"json_data.txt"

broker_send_req_cnt_dict = {}
broker_send_fail_cnt_dict = {}
broker_send_retry_cnt_dict = {}
broker_send_timeout_cnt_dict = {}
broker_receive_req_cnt_dict = {}
broker_wait_resp_cnt_dict = {}

broker_stat_dict_list = [
    broker_send_req_cnt_dict,
    broker_send_fail_cnt_dict,
    broker_send_retry_cnt_dict,
    broker_send_timeout_cnt_dict,
    broker_receive_req_cnt_dict,
    broker_wait_resp_cnt_dict,
]


partition_receive_msg_cnt_dict = {}
partition_receive_msg_byte_dict = {}
partition_remain_msg_cnt_dict = {}
partition_remain_msg_byte_dict = {}

partition_stat_dict_list = [
    partition_receive_msg_cnt_dict,
    partition_receive_msg_byte_dict,
    partition_remain_msg_cnt_dict,
    partition_remain_msg_byte_dict,
]


def handle_file():
    with open(FILE_PATH, 'r') as stat_file:
        for line in stat_file:
            start_idx = line.index("{")
            json_str = line[start_idx:]
            # print("json_data = ", json_str)
            handle_json_str(json_str)

    dump_stat_dict_list(partition_stat_dict_list, 'partition_stat_result_by_py.csv')
    dump_stat_dict_list(broker_stat_dict_list, 'broker_stat_result_by_py.csv')


def handle_json_str(json_str):
    json_obj = json.loads(json_str)
    # print("json_obj = ", json_obj)

    # for key in json_obj:
    #     print("json_obj[", key, '] = ', json_obj[key])
    # print("-" * 30)

    name = json_obj["name"]
    brokers = json_obj["brokers"]
    topics = json_obj["topics"]
    origin = json_obj["origin"]

    client_id = name[0: name.index("#")]
    cluster_id = origin[0: origin.index("#")]
    server_ip = origin[origin.index("#")+1:]
    # print("-" * 30)

    stat_broker_indicators(brokers, cluster_id, client_id)
    stat_topic_indicators(topics, cluster_id, client_id)


def dump_stat_dict_list(stat_dict_list, dist_path):
    file = open(dist_path, 'w')
    for stat_dict in stat_dict_list:
        for indicator in stat_dict:
            int_values = stat_dict[indicator]
            str_values = [str(x) for x in int_values]
            line = indicator + ", " + ", ".join(str_values)
            file.write(line + "\n")
    file.close()


def stat_topic_indicators(topics, cluster_id, client_id):
    for topic_key in topics:
        topic = topics[topic_key]

        partitions = topic["partitions"]
        for partition_id in partitions:
            if partition_id == "-1":
                continue
            partition = partitions[partition_id]
            key_prefix = cluster_id + "_" + client_id + "_" + topic_key + "_" + partition_id

            receive_msg_cnt = partition["txmsgs"]
            receive_msg_cnt_key = key_prefix + "_receiveMsgCnt"
            if receive_msg_cnt_key in partition_receive_msg_cnt_dict:
                partition_receive_msg_cnt_dict[receive_msg_cnt_key].append(receive_msg_cnt)
            else:
                receive_msg_cnt_list = [receive_msg_cnt]
                partition_receive_msg_cnt_dict[receive_msg_cnt_key] = receive_msg_cnt_list

            receive_msg_byte = partition["txbytes"]
            receive_msg_byte_key = key_prefix + "_receiveMsgByte"
            if receive_msg_byte_key in partition_receive_msg_byte_dict:
                partition_receive_msg_byte_dict[receive_msg_byte_key].append(receive_msg_byte)
            else:
                receive_msg_byte_list = [receive_msg_byte]
                partition_receive_msg_byte_dict[receive_msg_byte_key] = receive_msg_byte_list

            remain_msg_cnt = partition["xmit_msgq_cnt"]
            remain_msg_cnt_key = key_prefix + "_remainMsgCnt"
            if remain_msg_cnt_key in partition_remain_msg_cnt_dict:
                partition_remain_msg_cnt_dict[remain_msg_cnt_key].append(remain_msg_cnt)
            else:
                remain_msg_cnt_list = [remain_msg_cnt]
                partition_remain_msg_cnt_dict[remain_msg_cnt_key] = remain_msg_cnt_list

            remain_msg_byte = partition["xmit_msgq_bytes"]
            remain_msg_byte_key = key_prefix + "_remainMsgByte"
            if remain_msg_byte_key in partition_remain_msg_byte_dict:
                partition_remain_msg_byte_dict[remain_msg_byte_key].append(remain_msg_byte)
            else:
                remain_msg_byte_list = [remain_msg_byte]
                partition_remain_msg_byte_dict[remain_msg_byte_key] = remain_msg_byte_list


def stat_broker_indicators(brokers, cluster_id, client_id):
    for broker_key in brokers:
        broker = brokers[broker_key]
        # print(broker_key, " == ", broker)
        key_prefix = cluster_id + "_" + client_id + "_" + broker_key

        send_req_cnt = broker["tx"]
        send_req_cnt_key = key_prefix + "_sendReqCnt"
        if send_req_cnt_key in broker_send_req_cnt_dict:
            broker_send_req_cnt_dict[send_req_cnt_key].append(send_req_cnt)
        else:
            send_req_cnt_list = [ send_req_cnt ]
            broker_send_req_cnt_dict[send_req_cnt_key] = send_req_cnt_list

        send_fail_cnt = broker["txerrs"]
        send_fail_cnt_key = key_prefix + "_sendFailCnt"
        if send_fail_cnt_key in broker_send_fail_cnt_dict:
            broker_send_fail_cnt_dict[send_fail_cnt_key].append(send_fail_cnt)
        else:
            send_fail_cnt_list = [ send_fail_cnt ]
            broker_send_fail_cnt_dict[send_fail_cnt_key] = send_fail_cnt_list

        send_retry_cnt = broker["txretries"]
        send_retry_cnt_key = key_prefix + "_sendRetryCnt"
        if send_retry_cnt_key in broker_send_retry_cnt_dict:
            broker_send_retry_cnt_dict[send_retry_cnt_key].append(send_retry_cnt)
        else:
            send_retry_cnt_list = [ send_retry_cnt ]
            broker_send_retry_cnt_dict[send_retry_cnt_key] = send_retry_cnt_list

        req_timeout_cnt = broker["req_timeouts"]
        req_timeout_cnt_key = key_prefix + "_reqTimeoutCnt"
        if req_timeout_cnt_key in broker_send_timeout_cnt_dict:
            broker_send_timeout_cnt_dict[req_timeout_cnt_key].append(req_timeout_cnt)
        else:
            req_timeout_cnt_list = [req_timeout_cnt]
            broker_send_timeout_cnt_dict[req_timeout_cnt_key] = req_timeout_cnt_list

        receive_req_cnt = broker["rx"]
        receive_req_cnt_key = key_prefix + "_receiveReqCnt"
        if receive_req_cnt_key in broker_receive_req_cnt_dict:
            broker_receive_req_cnt_dict[receive_req_cnt_key].append(receive_req_cnt)
        else:
            receive_req_cnt_list = [receive_req_cnt]
            broker_receive_req_cnt_dict[receive_req_cnt_key] = receive_req_cnt_list

        wait_resp_cnt = broker["waitresp_cnt"]
        wait_resp_cnt_key = key_prefix + "_waitRespCnt"
        if wait_resp_cnt_key in broker_wait_resp_cnt_dict:
            broker_wait_resp_cnt_dict[wait_resp_cnt_key].append(wait_resp_cnt)
        else:
            wait_resp_cnt_list = [wait_resp_cnt]
            broker_wait_resp_cnt_dict[wait_resp_cnt_key] = wait_resp_cnt_list


if __name__ == '__main__':
    # pass
    handle_file()