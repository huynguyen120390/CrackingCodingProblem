def display(towers):
    towerNames = list(towers.keys())
    towerNames .sort()
    for i in towerNames :
        print(i, towers[i])
    print("")

def move(from_,to,towers):
    print(f"Move {from_} to {to}")
    towers[from_] -= 1
    towers[to] +=1
    display(towers)
    
def towersOfHanoi(n,from_,to,host):
    towers = {}
    towers[from_] = n
    towers[to] = 0
    towers[host] = 0
    display(towers)
    def helper(n,from_,to,host,towers):
        if n == 0:
            return
        helper(n-1,from_ = from_, to = host, host = to,towers = towers)
        move(from_,to,towers)
        helper(n-1,from_ = host, to = to, host = from_,towers = towers)
    helper(n,from_,to,host,towers)


towersOfHanoi(4,'A','C','B')
