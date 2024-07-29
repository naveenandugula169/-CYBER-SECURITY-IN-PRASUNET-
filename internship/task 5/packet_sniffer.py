from scapy.all import sniff, IP, TCP, UDP, ICMP, conf

# Function to analyze captured packets
def packet_analyzer(packet):
    print(f"{'-'*50}")
    print(f"Packet captured at {packet.time}")
    
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")

        # Protocol-specific details
        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            print("TCP Payload:")
            print(tcp_layer.payload)
        
        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
            print("UDP Payload:")
            print(udp_layer.payload)
        
        elif packet.haslayer(ICMP):
            icmp_layer = packet.getlayer(ICMP)
            print("ICMP Type:", icmp_layer.type)
            print("ICMP Code:", icmp_layer.code)
            print("ICMP Payload:")
            print(icmp_layer.payload)

    print(f"{'-'*50}\n")

# Capture packets
def start_sniffing(interface):
    print(f"[*] Starting packet capture on interface {interface}")
    sniff(iface=interface, prn=packet_analyzer, store=False, filter="ip")

if __name__ == "__main__":
    interface = "Ethernet"  # Replace with your network interface name as recognized by Npcap
    start_sniffing(interface)
