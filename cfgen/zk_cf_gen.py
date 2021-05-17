import sys
def load_template(path):
    result = []
    with open(path) as f:
        result = f.readlines()
    return result

def gen_zk_cf(identifier):
    single_zk_cloud_formation = load_template("templates/generation/single_zk.template.yml")
    for i in range(0, len(single_zk_cloud_formation)):
        single_zk_cloud_formation[i] = substitute("NUMBER", identifier, single_zk_cloud_formation[i])
    return single_zk_cloud_formation

def main(keeperCount: int):
    ec2_resources = []    
    base_cloud_formation = load_template("templates/generation/base.template.yml")
    for i in range(0, len(base_cloud_formation)):    
        line = base_cloud_formation[i]
        if should_substitute("AUTO_GENERATED_INSTANCES", line):
            for j in range(0, keeperCount):
                ec2_resources += gen_zk_cf(j)
        else:
            ec2_resources.append(line)
    print("".join(ec2_resources))

def substitute(name, new, line):
    return line.replace("@{" + name + "}", str(new))

def should_substitute(name, line):
    return "@{" + name + "}" in line

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: cfgen/zk_cf_gen.py <keeperCount>")
        exit(1)
    main(int(sys.argv[1]))