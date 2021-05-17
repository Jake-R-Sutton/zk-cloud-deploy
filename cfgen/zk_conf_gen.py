import sys

def load_file(path):
    result = []
    with open(path) as f:
        result = f.readlines()
    return result

def main(cluster_file_location):
    cluster_ips = load_file(cluster_file_location)
    for i in range(0, len(cluster_ips)):
        outputs = []
        for j, ip in enumerate(cluster_ips):    
            if i == j: 
                ip = "0.0.0.0"
            outputs.append("server.{}={}:{}:{}\n".format(j + 1, ip.strip(), 2888, 3888))
        
        f = open("out/server{}.cfg.add".format(i + 1), "w")
        f.writelines(outputs)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: cfgen/zk_conf_gen.py <cluster_ips_file.txt>")
        exit(1)
    main(sys.argv[1])