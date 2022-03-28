import subprocess

def find_brightnes(idx):
    brightnises = []
    result = subprocess.check_output(["ddcutil", "getvcp", "10", "-d", str(idx+1), "--brief"],encoding='utf8')
    #logger.error(str(result))

    result = result.split(" ")

    max_b = int(result[4])
    curr_b = int(result[3])



    return str(float(curr_b/max_b)*100)



print(find_brightnes(0))
print(find_brightnes(1))
print(find_brightnes(2))
