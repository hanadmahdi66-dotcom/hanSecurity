from scapy.all import sniff, IP, TCP, Raw


def computer(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst

        print("\n__---__---__")
        print("FROM:", src)
        print("TO  :", dst)


        if packet.haslayer(TCP):

            sport = packet[TCP].sport
            dport = packet[TCP].dport

            print("__---__---")
            print(f"TCP: {sport} ---> {dport}")


        if packet.haslayer(Raw):

            data = packet[Raw].load

            print("RAW:")
            print(data[:50])



def start():

    print("""
========================
   HAN SECURITY TOOL
========================

1. Monitor All Traffic
2. Exit

""")

    choose = input("Choose: ")


    if choose == "1":

        print("Starting monitor...\n")

        sniff(
            prn=computer,
            store=False
        )


    elif choose == "2":

        print("Bye")

    else:
        print("Invalid choice")



start()
