def main():
    number = input()
    temp_list = list(map(int, input().split()))
    count_dict = {"APPROVED":0, "DENIED":0}

    for i in temp_list:
        if i%2 == 0 and (i%3 != 0 and i%5 != 0):
           count_dict["DENIED"] += 1
            
    if count_dict["DENIED"] == 0:
        print("APPROVED")
    else:
        print("DENIED")

if __name__ == "__main__":
    main()