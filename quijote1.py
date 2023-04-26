#quijote laura

'''
    APARTADO 1
Genera una programa que estraiga de forma aleatoria un porcentaje 
de las líneas de un fichere: se leen el fichero por líneas y se 
"tira un dado". Si el dado es menor que el porcentaje la línea 
se graba en el fichero de salida 

'''
import random
import sys
def main(infilename, outfilename, ratio):
    with open(infilename) as infile:
        with open(outfilename, 'w') as outfile:
            for line in infile:
                if random.random()<=ratio:
                    outfile.write(line)


if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.arv[0]} <infilename> <outfilename> <ratio>")
        exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    ratio = float(sys.argv[3])
    main(infilename, outfilename, ratio)


'''
    APARTADO 2
    Con ese programa genera un fichero que se llame quijote_s05.txt 
'''