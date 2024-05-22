#!/usr/bin/python3
import sys,json
import subprocess

user="XXXX"
password="XXXX"


def main(argv,power):
    if power=="STATUS":
        power=""
    host_j=open("./host.json")
    hostlist=json.load(host_j)
    host_j.close()

    try:
        output=subprocess.getoutput("echo yes | ./plink -ssh " +user+"@"+hostlist[argv]+" -pw "+password+ " POWER "+power)
        print(output)
    except:
        pass

    
    
if __name__ == "__main__":
   main(sys.argv[1],sys.argv[2])