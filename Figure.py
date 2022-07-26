import time
import os
clear = lambda: os.system('cls')
boucle = False
welcom="""
    ********************************************************

    #     #  #######  #        ######  #######  ##   ##   #
    #     #  #        #       #        #     #  #  ## #   #
    #     #  ####     #       #        #     #  #     #   #
    #  #  #  #        #       #        #     #  #     # 
     #   #   #######  ######   ######  #######  #     #   #

    ********************************************************
    """

while(boucle==False):
    print(welcom)
    print("\n0-STOP\n1-RESTART\n2-FORME")
    switchcase=input()
    clear()
    match int(switchcase):
        case 0:
            boucle=True
            clear()
            print("FIN !")
        case 1:
            print("RESTART")
            clear()
        case 2:
            L=input("Longueur : ")
            l=input("Largeur : ")
            clear()
            for i in range(int(L)):
                print("   *   ", end='')
            print("\n")
            for y in range(int(l)):
                print("#", end="")
                for i in range(int(l)):
                    print("       ", end='')# création des espaces pour la seconde colone de droite
                print("#")
                print("\n")
            for ii in range(int(L)):
                print("   *   ", end='')
            time.sleep(3)
            clear()
            






