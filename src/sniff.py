import pyshark


capture = pyshark.LiveCapture(interface='Adapter for loopback traffic capture', bpf_filter='tcp port 1010')
#change for working with QUB

capture.sniff(packet_count=5)
print(capture)
for packet in capture:
    print(packet.highest_layer)