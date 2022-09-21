

def generate(rowIndex: int) -> list[list[int]]:
    
    # List = [1]
    # List2 = [List[0], List[0]]
    # List3 = [List[0], [List2[0]+List2[1]], List]
    # List4 = [List[0], [List3[0]+List3[1]], [List3[1]+List3[2]], List]
    # List5 = [List[0], [List4[0]+List4[1]], [List4[1]+List4[2]], [List4[2]+List4[3]], List]
    # print(List3)
    pascal = []
    for i in range(rowIndex+1):
        row = []
        for j in range(i+1):
            
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            
        pascal.append(row)
        
    return pascal[rowIndex]
    
print(generate(rowIndex=1))