import pandas as pd

files = ["1-labeled.dat", "2-labeled.dat", "3-labeled.dat", "4-labeled.dat"]
df = pd.read_csv(files[0])


def index():
    dic_ips = {}
    list_ip = []
    dic_connection = {}
    list_connection = []
    dic_bandwidth = {}
    list_bandwidth = []
    dic_packet_size = {}
    list_packet_size = []
    dic_time = {}
    list_time = []
    dic_p2p = {}
    list_p2p = []
    for n in range(len(df)):
        ip = df.values[n][0]
        connection = df.values[n][1]
        band = df.values[n][2]
        packet_size = df.values[n][3]
        time = df.values[n][4]
        p2p = df.values[n][5]

        # Populate IP dictionary
        if ip not in list_ip:
            list_ip.append(ip)
            if p2p=="p2p":
                dic_ips.update({ip: (1,0)})
            else:
                dic_ips.update({ip: (0, 1)})
        else:
            tmp = dic_ips.get(ip)
            if p2p=="p2p":
                tmp = (tmp[0]+1,tmp[1])
                dic_ips.update({ip: tmp})
            else:
                tmp = (tmp[0],tmp[1]+1)
                dic_ips.update({ip: tmp})

        # Populate Connection dictionary
        if connection not in list_connection:
            list_connection.append(connection)
            if p2p=="p2p":
                dic_connection.update({connection: (1,0)})
            else:
                dic_connection.update({connection: (0, 1)})
        else:
            tmp = dic_connection.get(connection)
            if p2p=="p2p":
                tmp = (tmp[0]+1,tmp[1])
                dic_connection.update({connection: tmp})
            else:
                tmp = (tmp[0],tmp[1]+1)
                dic_connection.update({connection: tmp})

        # Populate bandwidth dictionary
        if band not in list_bandwidth:
            list_bandwidth.append(band)
            if p2p=="p2p":
                dic_bandwidth.update({band: (1,0)})
            else:
                dic_bandwidth.update({band: (0, 1)})
        else:
            tmp = dic_bandwidth.get(band)
            if p2p=="p2p":
                tmp = (tmp[0]+1,tmp[1])
                dic_bandwidth.update({band: tmp})
            else:
                tmp = (tmp[0],tmp[1]+1)
                dic_bandwidth.update({band: tmp})

        # Populate packet_size dictionary
        if packet_size not in list_packet_size:
            list_packet_size.append(packet_size)
            if p2p=="p2p":
                dic_packet_size.update({packet_size: (1,0)})
            else:
                dic_packet_size.update({packet_size: (0, 1)})
        else:
            tmp = dic_packet_size.get(packet_size)
            if p2p=="p2p":
                tmp = (tmp[0]+1,tmp[1])
                dic_packet_size.update({packet_size: tmp})
            else:
                tmp = (tmp[0], tmp[1]+ 1)
                dic_packet_size.update({packet_size: tmp})

        # Populate time dictionary
        if time not in list_time:
            list_time.append(time)
            if p2p=="p2p":
                dic_time.update({time: (1,0)})
            else:
                dic_time.update({time: (0, 1)})
        else:
            tmp = dic_time.get(time)
            if p2p=="p2p":
                tmp = (tmp[0]+1,tmp[1])
                dic_time.update({time: tmp})
            else:
                tmp = (tmp[0],tmp[1]+1)
                dic_time.update({time: tmp})

        if p2p not in list_p2p:
            list_p2p.append(p2p)
            dic_p2p[p2p] = 1
        else:
            dic_p2p[p2p] += 1

    print("IP LIST:")
    print(list_ip)
    print("IP dict:")
    print(dic_ips)
    print("Connection LIST:")
    print(list_ip)
    print("Connection dict:")
    print(dic_connection)
    print("Bandwidth LIST:")
    print(list_bandwidth)
    print("Bandwidth dict:")
    print(dic_bandwidth)
    print("Packet_size LIST:")
    print(list_packet_size)
    print("Packet_size dict:")
    print(dic_packet_size)
    print("Time LIST:")
    print(list_time)
    print("Time dict:")
    print(dic_time)
    print("Time LIST:")
    print(list_time)
    print("Time dict:")
    print(dic_time)
    print("P2P dict:")
    print(dic_p2p)
    return dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time, dic_p2p


def prob(dic_p2p):
    prob_p2p = dic_p2p["p2p"] / (dic_p2p["p2p"] + dic_p2p["not p2p"])
    prob_Np2p = dic_p2p["not p2p"] / (dic_p2p["p2p"] + dic_p2p["not p2p"])
    print(prob_p2p)
    print(prob_Np2p)


def main():
    dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time, dic_p2p = index()
    prob(dic_p2p)


#main()
index()