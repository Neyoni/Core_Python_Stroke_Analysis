def load_dataset(filepath): #Function to load the dataset
    
    dataset={}
    rows_id=0
    
    with open ("data.csv", 'r') as file: #Reading the csv file using with open
        columns = file.readline().strip().split(',')#Reading the first line in the file (Column names) and striping of every whitespace and spliting the data on the delimiter (,)

        for col in file: 
            row = col.strip().split(',')
        
            rows={}
            for i,value in enumerate(row): #
                rows[columns[i]]= value
            dataset[rows_id]=rows
            rows_id +=1
    
    return dataset 