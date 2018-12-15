def output(dic_ips, dic_connection, dic_bandwidth, dic_packet_size, dic_time, prob_p2p, prob_np2p):
    dfu = pd.read_csv(files_u[0])
    for n in range(len(dfu)):
        ip_u = dfu.values[n][0]
        connection_u = dfu.values[n][1]
        band_u = dfu.values[n][2]
        packet_size_u = dfu.values[n][3]
        time_u = dfu.values[n][4]

        # IP:
        ip_label_ip = dic_ips.get(ip_u)
        if ip_label_ip is not None:
            IP_p2p = ip_label_ip[0]/(ip_label_ip[0] + ip_label_ip[1])
            IP_np2p = ip_label_ip[1]/(ip_label_ip[0] + ip_label_ip[1])
            print(ip_u)

        # Connection:
        ip_label_connection = dic_connection.get(connection_u)
        if ip_label_connection is not None:
            conn_p2p = ip_label_connection[0]/(ip_label_connection[0] + ip_label_connection[1])
            conn_np2p = 1 - conn_p2p

        # Bandwidth:
        ip_label_band = dic_bandwidth.get(band_u)
        if ip_label_band is not None:
            band_p2p = ip_label_band[0] / (ip_label_band[0] + ip_label_band[1])
            band_np2p = 1 - band_p2p

        # Packet_size:
        ip_label_packet = dic_packet_size.get(packet_size_u)
        if ip_label_packet is not None:
            packet_p2p = ip_label_packet[0] / (ip_label_packet[0] + ip_label_packet[1])
            packet_np2p = 1 - packet_p2p

        # Time:
        ip_label_time = dic_time.get(time_u)
        if ip_label_time is not None:
            time_p2p = ip_label_time[0] / (ip_label_time[0] + ip_label_time[1])
            time_np2p = 1 - time_p2p

        total_p2p = IP_p2p * conn_p2p * band_p2p * packet_p2p * time_p2p * prob_p2p
        total_np2p = IP_np2p * conn_np2p * band_np2p * packet_np2p * time_np2p * prob_np2p

        print(ip_u)
        print(connection_u)
        print(band_u)
        print(packet_size_u)
        print(time_u)

        if total_p2p > total_np2p:
            with open(files_u[0], 'r') as file:
                # read a list of lines into data
                data = file.readlines()
            data[n] += ", p2p"
            with open(files_u[0]+".new", 'w') as file:
                file.writelines(data)
        if total_p2p < total_np2p:
            with open(files_u[0], 'r') as file:
                # read a list of lines into data
                data = file.readlines()
            data[n] += ", not p2p"
            with open(files_u[0]+".new", 'w') as file:
                file.writelines(data)