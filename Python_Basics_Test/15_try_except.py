try: 
    with open("new_file1.txt","r") as f:
        data= f.read()
        print(data)
# except Exception as e:
#     print("Error",e)
except FileNotFoundError as e:
    print("Exception",e)



