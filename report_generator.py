import pandas as pd #data proce. library
from datetime import datetime
import os

def generate_report():
    print("Report generation started")

    input_file = "data/sales_data.csv"

    if not os.path.exists(input_file): #csv file che k ny 
        print("CSV data file not found")
        return None, []

    os.makedirs("reports", exist_ok=True)

    df = pd.read_csv(input_file) #table
    print("CSV file read successfully")

    today = datetime.now().strftime("%Y-%m-%d")
    output_file = f"reports/sales_report_{today}.xlsx"

    df.to_excel(output_file, index=False) #data ne exel ma convert krse

    emails = df["Email"].dropna().astype(str).tolist() #empty value remove, list ma convert
    print("Email List:", emails)
    
    print(f"Report generated: {output_file}")
    print(f"Total recipients: {len(emails)}")
    return output_file, emails

if __name__ == "__main__":
    generate_report()