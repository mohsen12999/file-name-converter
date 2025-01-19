import os

def convert_persian_to_english_number(persian_number):
    # Mapping of Persian numbers to English numbers
    persian_to_english = {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9"
    }
    
    # Replace each Persian number with the corresponding English number
    english_number = ''.join(persian_to_english.get(char, char) for char in persian_number)
    return english_number    
    pass

def main():
    default_path = "D:\DCIM\Camera"
    choice_path = input(f"\nEnter the path for convert [default({default_path})]: ") or default_path

    try:
        os.chdir(choice_path)
    except:
        print("problem in finding path")
        return
    
    all_files_list  = os.listdir()

    for fileName in all_files_list:
        if '۲۰' in fileName:
            newFileName = convert_persian_to_english_number(fileName)
            os.rename(fileName,newFileName)
            print("one file name changed!")

    print("process complete, have fun :)\n")

if __name__ == "__main__":
    main()