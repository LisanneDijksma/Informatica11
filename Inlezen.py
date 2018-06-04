def inlezen():   
    data=open("RNA-Seq-counts.txt", 'r')
    annotatie=open("WCFS1_anno.txt", 'r')
    
    data_list=[]
    anno_list=[]
    
    for line in data:
        data_list.append(line)
    for line in annotatie:
        anno_list.append(line)
    

    print (data_list)

def main():
    inlezen()

main()