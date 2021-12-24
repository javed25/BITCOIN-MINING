from hashlib import sha256
import time
max_number=10000000000000000

fresh_hash=None
def hashcode(string):
    return sha256(string.encode("ascii")).hexdigest()

def bitcoin(block_num,trans,prev_hash,zeros):
    global fresh_hash,max_number,max_number
    zero_string="0"*zeros
    try:
        for num in range(max_number):
            string=str(block_num)+trans+prev_hash+str(num)
            fresh_hash = hashcode(string)
            if fresh_hash.startswith(zero_string):
                print("Mined Succesfully")
                return fresh_hash

    except Exception as e:
        print("Sorry Computational Power Reach!!!")
        print(e)
        return None


trans='''
a-b-6
c-d-3
e-f-7
g-h-20
i-j-30
'''
prev_hash ="00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"
block_num=1
zeros=8

print("Start Mining.....")
start_time=time.time()

h=bitcoin(block_num,trans,prev_hash,zeros)

end_time=time.time()

print(f"Mining took {end_time-start_time} seconds")
print(f"Fresh hash is : {h} at {num} iteration")