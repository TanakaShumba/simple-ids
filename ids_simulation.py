import random
import time

def detect_intrusion(packet):
    suspicious_ips = ['192.168.1.100', '10.0.0.50']
    if packet['src_ip'] in suspicious_ips:
        print(f"ALERT! Suspicious packet detected from {packet['src_ip']}")
    else:
        print(f"Packet from {packet['src_ip']} is normal")

if __name__ == '__main__':
    for _ in range(10):
        packet = {
            'src_ip': f"192.168.1.{random.randint(1, 150)}",
            'dst_ip': '192.168.1.1',
            'data': 'Sample payload'
        }
        detect_intrusion(packet)
        time.sleep(1)
