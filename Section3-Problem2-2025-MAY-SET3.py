with open(filename) as f:

    header = list(map(str.strip,f.readline().strip().strip('|').split('|')))
    f.readline() # skipping the header separator    

    data = [
      list(map(int, row.strip().strip(' |').split('|')))
      for row in f
    ]

    # col_sums = [
    #   sum(data[i][j]for i in range(len(data)))
    #   for j in range(len(data[0]))
    # ]
    
    col_sums = map(sum, zip(*data)) # shortcut

    for name, col_sum in zip(header, col_sums):
        print(f"{name}: {col_sum}")

# #Another Method:


# # Read the temporary file `filename`, parse the markdown table,
# # compute column sums and print the result in the required format.


# with open(filename,'r') as file:
#     line1=file.readline().rstrip()
#     header_list=line1.split('|')
#     header_list=header_list[1:-1]
    
#     file_width=len(header_list)
    
#     line2=file.readline().rstrip()
    
#     l=[]
#     for i in range(file_width):
#         l.append(0)
    
#     for line in file:
#         # print (line)
#         temp_list=line.split('|')
#         temp_list=temp_list[1:-1]
        
#         # print (temp_list)
#         for i in range(len(temp_list)):
#             ch=temp_list[i].strip()
#             num=int(ch)
#             l[i] +=num
#     for i in range(file_width):
#         print (f"{header_list[i].strip()}: {l[i]}")
    
            
#     Column Totals in a Markdown Table (Numeric Columns Only)
# Read the contents of a file containing a markdown table with integer values and print the column sums.

# Markdown table format

# First line contains the readers surrounded and separated by | character.
# Second line is header separater containing | and - and has no data.
# Every following line is a data row with values surrounded and separated by | character.
# Spaces may appear around the pipes and around the cell contents.
# All columns contain integer values (positive, negative or zero).
# Output format

# One column sum per line, in the format:

# <column_name>: <total>
# The order of the output must follow the order of the columns in the header.

# Note: This is a fileinstdout type problem the whole input should be written to a temporary file first, and the solution must read from that file.        
        
        
        
    
    
    
    
    
   
        
