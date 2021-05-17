import os
import sys

def main(cluster_file_location, key_pair_name):
    nodes = []
    with open(cluster_file_location) as f:
        nodes = f.readlines()
        for i, ip in enumerate(nodes):
            command = "cat out/server{}.cfg.add | ssh -o StrictHostKeychecking=no -i {} ec2-user@{}  \"cat - >> /usr/local/zookeeper/conf/zoo.cfg\"".format(i+1, key_pair_name.strip(), ip.strip())
            os.system(command)
            command = "echo '{}' | ssh -o StrictHostKeychecking=no -i {} ec2-user@{} -T \"cat > /var/lib/zookeeper/myid\"".format(i+1, key_pair_name.strip(), ip.strip())
            os.system(command)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cfgen/zk_write_remote_config.py <cluster_ip_txt_loc> <key_pair_loc>")
        exit(1)
    main(sys.argv[1], sys.argv[2])