import os
import sys

# Goal is to run a command like the following for all of the nodes in our cluster
# cat out/dynamic_conf.cfg | ssh -i my-key-pair.pem ec2-user@<IP_Address>  "cat - >> /usr/local/zookeeper/conf/zoo.cfg"
def main(key_pair_name):
    nodes = []
    with open("out/cluster_ips.txt") as f:
        nodes = f.readlines()
        for ip in nodes:
            command = "cat out/dynamic_conf.cfg | ssh -i {} ec2-user@{}  \"cat - >> /usr/local/zookeeper/conf/zoo.cfg\"".format(key_pair_name.strip(), ip.strip())
            os.system(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("missing argument: ssh keypair name")
        exit(1)
    main(sys.argv[1])