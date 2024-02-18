from datetime import datetime

if __name__ =="__main__":
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%Y-%m-%d")
    print("Formatted date:", formatted_date)