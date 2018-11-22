temperatures=[10,-20,-289,100]
def tulis(temperatures,berkas):
    with open(berkas,'w') as file:
        for i in temperatures:
            if i>-275.15:
                f=i*9/5+32
                file.write(str(f)+"\n")


tulis(temperatures,'temps.txt')
