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
        if ip not in list_ip:
            list_ip.append(ip)
            dic_ips[ip] = 1
        else:
            dic_ips[ip] += 1
        if connection not in list_connection:
            list_connection.append(connection)
            dic_connection[connection] = 1
        else:
            dic_connection[connection] += 1
        if band not in list_bandwidth:
            list_bandwidth.append(band)
            dic_bandwidth[band] = 1
        else:
            dic_bandwidth[band] += 1
        if packet_size not in list_packet_size:
            list_packet_size.append(packet_size)
            dic_packet_size[packet_size] = 1
        else:
            dic_packet_size[packet_size] += 1
        if time not in list_time:
            list_time.append(time)
            dic_time[time] = 1
        else:
            dic_time[time] += 1
        if p2p not in list_p2p:
            list_p2p.append(p2p)
            dic_p2p[p2p] = 1
        else:
            dic_p2p[p2p] += 1
    print(dic_ips)
    print(dic_connection)
    print(dic_bandwidth)
    print(dic_packet_size)
    print(dic_time)
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

main()