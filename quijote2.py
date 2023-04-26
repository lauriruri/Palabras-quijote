'''
    APARTADO 3
    Haz que programa de contar palabras y pruébalo con el fichero quijote_s05.txt. 
    Copia la salida y ponla en un fichero llamado out_quijote_s05.txt 
'''

# -*- coding: utf-8 -*-

from pyspark import SparkContext
import sys

'''
def main(filename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(filename)
        words_rdd = data.map(lambda x: len(x.split()))
        print (words_rdd.collect())
        print ('RESULTS------------------')
        print ('words_count', words_rdd.sum())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 {0} <file>".format(sys.argv[0]))
    else:
        main(sys.argv[1])

'''

'''
    APARTADO 4
    Prueba el programa con el libro completo.
    Copia la salida en un fichero llamado out_quijote.txt 
'''

def main(infilename, outfilename):
    with SparkContext() as sc:
        with open(outfilename, 'w') as outfile:
            sc.setLogLevel("ERROR")
            data = sc.textFile(infilename)
            words_rdd = data.map(lambda x: len(x.split()))
            outfile.write(' '.join(map(str, words_rdd.collect())))
            outfile.write('\nRESULTS------------------ \n')
            outfile.write('words_count: ')
            outfile.write(str(words_rdd.sum()))

if __name__=="__main__":
    if len(sys.argv)<3:
        print(f"Usage: {sys.arv[0]} <infilename> <outfilename>")
        exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    main(infilename, outfilename)