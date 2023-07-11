#Importing relevant Modules
import nmap
import sys

#Checking for zero arguements
if len(sys.argv) < 2:
    print("usage:" +sys.argv[0]+" <ip>")
    sys.exit(1)

#List of port numbers to be scanned
ports = [ 21,22,80,139,443,8080]

# Target IP Address
target = str(sys.argv[1])

# Instantiating a scan variable for Nmap
scan_ = nmap.PortScanner()

print("\n Scanning " + target + " for ports "+str(ports)+". \n" )

for port in ports:
    portscan = scan_.scan(target,str(port))
    # The result from the above code contains various information
    # Hence we need to select which information we want to see
    # Information selected include state and status of the port 
    #portscan = portscan['scan'][target]['tcp'][port]['state']['name']['status']
    print("Port "+ str(port) +" is "+ portscan['scan'][target]['tcp'][port]['state'] + "\n" )

print("\n Host "+ target +" is " + portscan['scan'][target]['status']['state'])