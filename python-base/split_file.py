# coding=UTF-8
# 保存文件函数
def save_file(client, server, count):
    file_name_client = 'client_' + str(count) + '.txt'
    file_name_server = 'server_' + str(count) + '.txt'

    client_file = open(file_name,'w')
    server_file = open(file_name,'w')

    client_file.writelines(client)
    server_file.writelines(server)

    client_file.close()
    server_file.close()
    
# 把原文件内容切分
def split_file(file_name):
    f = open(file_name,encoding='UTF-8')

    client = []
    server = []
    count = 1

    for each_line in f:
        if each_line[:].strip() != '=======':
            print(each_line)
            (role,line_spoken) = each_line.split('：',1)
            print(each_line.split('：',1))
            print(role)
            print(each_line)
            if(role == '小黄'):
                client.append(line_spoken)
            if(role == '客服'):
                server.append(line_spoken)
        else:
            print(client)
            save_file(client, server, count)
            print("执行了")

            client = []
            server = []
            count += 1
    save_file(client, server, count)
    f.close()

split_file('record.txt')

            
