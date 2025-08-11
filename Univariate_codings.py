class univariate():
    def QuanQual(Dataset):
        Quan = []
        Qual = []
        for columnName in Dataset.columns:
            if Dataset[columnName].dtype == 'O':
                Qual.append(columnName)
            else:
                Quan.append(columnName)
    
        return Quan, Qual