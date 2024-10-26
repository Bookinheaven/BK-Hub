

def TowerOfHanoi(num: int, from_Rod, to_Rod, aux_Rod):
    if num == 0:
        return
    TowerOfHanoi(num-1  ,from_Rod, aux_Rod, to_Rod)
    print("Move disk", num, "from rod", from_Rod, "to rod", to_Rod)
    TowerOfHanoi(num-1, aux_Rod, to_Rod, from_Rod)



if __name__ == "__main__":
   TowerOfHanoi(3, 'A', 'C', 'B')