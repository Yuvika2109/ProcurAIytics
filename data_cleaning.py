import pandas as pd

def clean_data():
    try:
        input_file = 'chat.xlsx'
        output_file = 'cleaned_chat.xlsx'
        
        df = pd.read_excel(input_file, engine="openpyxl", sheet_name="Sheet1")
        
    
        df = df.fillna('Unknown')
        for col in df.select_dtypes(include=['float64']).columns:
            df[col] = df[col].fillna(0).astype(int)
        
 
        df.to_excel(output_file, index=False, sheet_name="Sheet1")
        
        print(f"Cleaned data has been saved to {output_file}")
        return df

    except Exception as e:
        print(f"An error occurred: {e}")


clean_data()



