from datetime import datetime



a = input("Start Typing: I will calculate time from and to Entering : ")
start_time = datetime.now()

sentence = input("Start: ")

print("End")

end_time = datetime.now()

all_time = end_time - start_time
print(f"Time: {all_time}")