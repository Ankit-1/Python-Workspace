def  main():
    buffersize = 50000 
    infile=open('olives.jpg','rb')
    outfile=open('new.jpg','wb')
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end='')
        buffer=infile.read(buffersize)
        print()
    print('Done.............!')
main() 