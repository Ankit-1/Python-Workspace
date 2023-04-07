try:
    a=open('line.txt')
    for loop_var in a:
        print(loop_var.strip())
    #s=1/0
except IOError as r:
    print('Error found!',r)
    
except ZeroDivisionError as r:
    print('Error found!',r)
    
finally:
    print('I am finally',flush=False)
    try:
        a.close()
    except NameError as r:
        print("Error found",r)
    
print('done')



# def main():
#     infile = open('lines.txt','r')
#     outfile=open('new.txt','w')
#     for line in infile:
#         print(line,file=outfile,end="")
#     print('done')
# 
# main()
#     
# a=open('new.txt')
# for line in a:
#     print(line)
#for opening a file .... file object = open(file_name[,access_model]
#access modes -text files  r,w,r+    
#access modes - binary files rb,wb,rb+
