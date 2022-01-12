import pyshark
#tshark - pyshark - wireshark

#Need to fix import for testing
#Scanner class will eventually be used to automatically check packets transfered over a specific connection
#Filtering will also be implemented

def print_live_cap():
    capture = pyshark.LiveCapture(interface="***INTERFACE NAME***")
    for packet in capture:
        if "DNS" in packet and not packet.dns.flags_response.int_value:
            print(packet.dns.qry_name)
            
if __name__ == "__main__":
    print_live_cap()