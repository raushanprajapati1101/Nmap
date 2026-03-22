#/usr/bin/python3

import nmap

sc = nmap.PortScanner()

print("Welcome to Simple nmap Scanner :")
print("_________________________________________________")

ip_addr = input("Please enter your IP Address to scan : ")
print("the IP entered is : ", ip_addr)

resp = input("Please enter the Type of scan you need : 1. SYN Scan 2. UDP Scan 3. Comprehensive Scan\n")
       
print("You have Selected:", resp)
      
resp_dict = {'1':['-sS -v -sV','tcp'],'2':['-sS -sV -v','udp'],'3':['-sS -v -sV -A -sC','tcp']}

if resp not in resp_dict.keys():
    print("Please Enter a valid Option.")
else:
     print("nmap version:", sc.nmap_version())
     sc.scan(ip_addr, "1-1024", resp_dict[resp][0])
     
     if sc[ip_addr].state() == 'up':
            print("\nHOst is up, scanning results: ")
            
            for proto in sc[ip_addr].all_protocols():
                print("\nProtocol : {}".format(proto))
                print("Open Ports : {}".format(', '.join(map(str, sc[ip_addr]
[proto].keys()))))
                for port, info in sc[ip_addr][proto].items():
                    print("\nPort : {}\nService : {}\nState : {}".format(port,
info['name'], info['state']))
