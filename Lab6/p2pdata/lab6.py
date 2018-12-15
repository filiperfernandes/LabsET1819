import pandas as pd
import argparse
import random

files = ["1-labeled.dat", "2-labeled.dat", "3-labeled.dat", "4-labeled.dat"]
files_u = ["1-unlabeled.dat", "2-unlabeled.dat", "3-unlabeled.dat", "4-unlabeled.dat"]


def get_parser():
    parser = argparse.ArgumentParser(description="""Traffic Engineering P2P classification tool""")
    parser.add_argument('-e', '--error', dest='error', help="""specify training percentage, ex: 0.7""",
                        action="store")
    parser.add_argument('-l', '--label', help="""Label the unlabeled files""",
                        action="store_true")
    return parser


def gen_random(start, end, num):
    res = []

    for j in range(num):
        val = random.randint(start, end)
        while val in res:
            val = random.randint(start, end)
        res.append(val)

    return res


def index(filename, mode, percentage):
    df = pd.read_csv(filename, header=None)
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

    if mode == "label":
        mode_range = range(len(df))
    else:
        val = int(percentage*len(df))
        mode_range = gen_random(0, 9999, val)
        all_range = list(range(len(df)))
        missing_range = set(all_range).difference(mode_range)

    for n in mode_range:

        ip = df.values[n][0]
        connection = df.values[n][1]
        band = df.values[n][2]
        packet_size = df.values[n][3]
        time = df.values[n][4]
        p2p = df.values[n][5]

        # Populate IP dictionary
        if ip not in list_ip:
            list_ip.append(ip)
            if p2p == "p2p":
                dic_ips.update({ip: (1, 0)})
            else:
                dic_ips.update({ip: (0, 1)})
        else:
            tmp = dic_ips.get(ip)
            if p2p == "p2p":
                tmp = (tmp[0]+1, tmp[1])
                dic_ips.update({ip: tmp})
            else:
                tmp = (tmp[0], tmp[1]+1)
                dic_ips.update({ip: tmp})

        # Populate Connection dictionary
        if connection not in list_connection:
            list_connection.append(connection)
            if p2p == "p2p":
                dic_connection.update({connection: (1, 0)})
            else:
                dic_connection.update({connection: (0, 1)})
        else:
            tmp = dic_connection.get(connection)
            if p2p == "p2p":
                tmp = (tmp[0]+1, tmp[1])
                dic_connection.update({connection: tmp})
            else:
                tmp = (tmp[0], tmp[1]+1)
                dic_connection.update({connection: tmp})

        # Populate bandwidth dictionary
        if band not in list_bandwidth:
            list_bandwidth.append(band)
            if p2p == "p2p":
                dic_bandwidth.update({band: (1, 0)})
            else:
                dic_bandwidth.update({band: (0, 1)})
        else:
            tmp = dic_bandwidth.get(band)
            if p2p == "p2p":
                tmp = (tmp[0]+1, tmp[1])
                dic_bandwidth.update({band: tmp})
            else:
                tmp = (tmp[0], tmp[1]+1)
                dic_bandwidth.update({band: tmp})

        # Populate packet_size dictionary
        if packet_size not in list_packet_size:
            list_packet_size.append(packet_size)
            if p2p == "p2p":
                dic_packet_size.update({packet_size: (1, 0)})
            else:
                dic_packet_size.update({packet_size: (0, 1)})
        else:
            tmp = dic_packet_size.get(packet_size)
            if p2p == "p2p":
                tmp = (tmp[0]+1, tmp[1])
                dic_packet_size.update({packet_size: tmp})
            else:
                tmp = (tmp[0], tmp[1]+1)
                dic_packet_size.update({packet_size: tmp})

        # Populate time dictionary
        if time not in list_time:
            list_time.append(time)
            if p2p == "p2p":
                dic_time.update({time: (1, 0)})
            else:
                dic_time.update({time: (0, 1)})
        else:
            tmp = dic_time.get(time)
            if p2p == "p2p":
                tmp = (tmp[0]+1, tmp[1])
                dic_time.update({time: tmp})
            else:
                tmp = (tmp[0], tmp[1]+1)
                dic_time.update({time: tmp})

        if p2p not in list_p2p:
            list_p2p.append(p2p)
            if p2p == "p2p":
                dic_p2p.update({"count": (1, 0)})
            else:
                dic_p2p.update({"count": (0, 1)})
        else:
            tmp = dic_p2p.get("count")
            if p2p == "p2p":
                tmp = (tmp[0] + 1, tmp[1])
                dic_p2p.update({"count": tmp})
            else:
                tmp = (tmp[0], tmp[1]+1)
                dic_p2p.update({"count": tmp})

    if mode == "error":
        return dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time, dic_p2p, missing_range
    else:
        return dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time, dic_p2p


def get_prob(dic_p2p):
    prob_p2p = dic_p2p.get("count")[0] / (dic_p2p.get("count")[0] + dic_p2p.get("count")[1])
    prob_np2p = dic_p2p.get("count")[1] / (dic_p2p.get("count")[0] + dic_p2p.get("count")[1])
    return prob_p2p, prob_np2p


def output(filename, mode, missing_range, dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time,
           prob_p2p, prob_np2p):
    lines = []
    dfu = pd.read_csv(filename, header=None)

    if mode == "label":
        mode_range = range(len(dfu))
    else:
        error = 0
        nr_times = 0
        mode_range = missing_range

    for n in mode_range:
        ip_u = dfu.values[n][0]
        connection_u = dfu.values[n][1]
        band_u = dfu.values[n][2]
        packet_size_u = dfu.values[n][3]
        time_u = dfu.values[n][4]

        if mode == "error":
            p2p_u = dfu.values[n][5]

        # IP:
        ip_label_ip = dic_ips.get(ip_u)
        if ip_label_ip is not None:
            ip_p2p = ip_label_ip[0]/prob_p2p
            ip_np2p = ip_label_ip[1]/prob_np2p

        # Connection:
        ip_label_connection = dic_connection.get(connection_u)
        if ip_label_connection is not None:
            conn_p2p = ip_label_connection[0]/prob_p2p
            conn_np2p = ip_label_connection[1]/prob_np2p

        # Bandwidth:
        ip_label_band = dic_bandwidth.get(band_u)
        if ip_label_band is not None:
            band_p2p = ip_label_band[0] / prob_p2p
            band_np2p = ip_label_band[1] / prob_np2p

        # Packet_size:
        ip_label_packet = dic_packet_size.get(packet_size_u)
        if ip_label_packet is not None:
            packet_p2p = ip_label_packet[0] / prob_p2p
            packet_np2p = ip_label_packet[1] / prob_np2p
        # Time:
        ip_label_time = dic_time.get(time_u)
        if ip_label_time is not None:
            time_p2p = ip_label_time[0] / prob_p2p
            time_np2p = ip_label_time[1] / prob_np2p

        total_p2p = ip_p2p * conn_p2p * band_p2p * packet_p2p * time_p2p * prob_p2p
        total_np2p = ip_np2p * conn_np2p * band_np2p * packet_np2p * time_np2p * prob_np2p

    # Label mode
        if mode == "label":

            if total_p2p > total_np2p:
                line = ip_u + "," + str(connection_u) + "," + str(band_u) + "," + str(packet_size_u) + "," + time_u \
                       + "," + "p2p\n"
                lines.append(line)

            if total_p2p < total_np2p:
                line = ip_u + "," + str(connection_u) + "," + str(band_u) + "," + str(packet_size_u) + "," \
                       + time_u + "," + "not p2p\n"
                lines.append(line)
        else:
            if total_p2p > total_np2p:
                if p2p_u != "p2p":
                    error = error + 1

            if total_p2p < total_np2p:
                if p2p_u != "not p2p":
                    error = error + 1
            nr_times = nr_times + 1

    if mode == "label":
        # Write Output file
        if filename.startswith("1-"):
            f = open("out-1-labeled.dat", "w")
            f.writelines(lines)
            f.close()
        if filename.startswith("2-"):
            f = open("out-2-labeled.dat", "w")
            f.writelines(lines)
            f.close()
        if filename.startswith("3-"):
            f = open("out-3-labeled.dat", "w")
            f.writelines(lines)
            f.close()
        if filename.startswith("4-"):
            f = open("out-4-labeled.dat", "w")
            f.writelines(lines)
            f.close()
    else:
        perc_error = (error / nr_times) * 100
        print("Error =", perc_error, "%")


def main():

    parser = get_parser()
    args = vars(parser.parse_args())
    label = args['label']
    error = args['error']

    # Label mode
    if label:
        count = 0
        for filename in files:
            print(filename)
            print(files_u[count])
            dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time, dic_p2p = index(filename, "label", 1)
            prob_p2p, prob_np2p = get_prob(dic_p2p)
            output(files_u[count], "label", [], dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time,
                   prob_p2p, prob_np2p)
            count += 1

    # Error mode
    if error is not None:
        for filename in files:
            print(filename)
            dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time, dic_p2p, missing_range = \
                index(filename, "error", float(error))
            prob_p2p, prob_np2p = get_prob(dic_p2p)
            output(filename, "error", missing_range, dic_ips, dic_connection, dic_bandwidth, dic_packet_size,
                   dic_time, prob_p2p, prob_np2p)

    if not label and error is None:
        parser.print_help()


if __name__ == "__main__":
    main()
