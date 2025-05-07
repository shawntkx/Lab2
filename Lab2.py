def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 float_list = get_user_input()
 print("Average Temperature is: " + str(calc_average_temperature(float_list)))
 print("Minimum and Maximum Temperature is :" + str(calc_min_max_temperature(float_list)))

## i added a print for the avg n minmax

def display_main_menu():
 print("Enter some numbers separated by commas (e.g. 5, 67,32)")

def get_user_input():
 user_input = input("input: ")
 str_list = user_input.split(",")
 float_list = [float(num.strip()) for num in str_list]
 return float_list

def calc_average_temperature(float_list):
 avg_temp = sum(float_list) / len(float_list)
 return avg_temp

def calc_min_max_temperature(float_list):
 min_temperature = min(float_list)
 max_temperature = max(float_list)
 return (min_temperature, max_temperature)

if __name__ =="__main__":
 main()
