import openpyxl
import os


FILEPATH = r"el path donde guardaras tu excel"

def create_salary_file():
    print("Creating Excel file...")

    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Salary Messages"

    
    headers = ["Date & Time", "Sender Name", "Message Content"]
    ws.append(headers)

    
    try:
        wb.save(FILEPATH)
        print(f"Excel creado: {FILEPATH}")
        
        
    except PermissionError:
        print("Cierra el excel para que lo pueda trabajar.")
        
    except FileNotFoundError:
        print("El folder no existe")

if __name__ == "__main__":
    create_salary_file()