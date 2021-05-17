import sys

def load_file(path):
    result = []
    with open(path) as f:
        result = f.readlines()
    return result

def main():
    outputs = []
    cluster_ips = load_file("out/cluster_ips.txt")
    i = 1
    for ip_address in cluster_ips:
        outputs.append("server.{}={}:{}:{}\n".format(i, ip_address.strip(), 2888, 3888))
        i += 1
    print("".join(outputs))

if __name__ == "__main__":
    main()