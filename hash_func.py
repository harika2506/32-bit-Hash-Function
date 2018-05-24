
import sys
import os
sys.path.append( "pathname_to_BitVector_directory" )
import BitVector as bve
import fileinput
import glob as g
#hash_function to find h value
def hash_function():
    # open a file for storing the output hast values
    output=open("hashOutputFile.txt",'w')
    # read all the files in the current directory
    directory = g.glob('*.*')
    # Removing the output file from the directory
    directory.remove('hashOutputFile.txt')

    if(len(directory)<=1):
        input=open("sample.txt","w+")
        input.write("Hello World")
        input.close()
        directory = g.glob('*.*')



    for file in directory:
        bv = bve.BitVector(filename = file)
        # creating a 32-bit hash with all zeroes
        hash = bve.BitVector(size = 32)


        while(bv.more_to_read):
            bv1 = bv.read_bits_from_file(8)
            # shifting the hash value for 4 bits
            hash << 4
            hash[0:8] = bv1 ^ hash[0:8]

        myHexHash = hash.getHexStringFromBitVector()

        output.write(myHexHash)
        output.write('\n')
    # close the output file
    output.close()

# To check if there are any collisions in the output file
def hash_check_collision():
    list1=[]
    count=0
    openFile = open("hashOutputFile.txt", 'r')
    for i in openFile:
        if i not in list1:
            list1.append(i)
        else:
            count=count+1
            break
    if count>0:
        print "Colllision Occurred"
    else:
        print "No Collision"
    # close the opened output file
    openFile.close()







hash_function()
hash_check_collision()
