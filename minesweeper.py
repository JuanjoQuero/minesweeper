#First, a welcome message. I ask user to enter how many rows and columns he wanted for his grid. 
#And how to enter the symbols for different positions in the grid.
print("Welcome to the Minesweeper game. Let's create your grid...")
rows = int(input("Please enter the number of rows for your grid: "))
cols = int(input("Please enter the number of columns for your grid: "))
print("""Almost there! Now you can choose the position of your mines. 
Please enter '#' for mine or '-' for a mine-free spot and press enter after every selection:""")

#Now a module to generate the grid using user selection.
grid = []
for i in range(rows):          # "For loop" for row entries.
    a =[]
    for j in range(cols):      # "For loop" for column entries.
         a.append((input()))   # we append the input to our row list.
         
    grid.append(a) #and we append our rows into our grid.

print("Excellent! This is how your grid looks \n")
[print(x) for x in grid] #To print the output in the required format.

#We are going to create a function that will take our grid(2d list) as a parameter and return another grid 
#replacing each dash for a digit indicating the number of mines immediately adjacent to the spot.
def minesweeper(input_grid: list):
    output_grid = [] #Creating a new list
    for current_row, row in enumerate(input_grid): #Iterating over our list using the enumerate method.
        output_row = []
        for current_col, col in enumerate(row):
            if col == "#": # Check if the spot is a mine, if it is, keep the "#" symbol.
                
                output_row.append("#")
            
            else: # If is not a mine "#", we need to count number of bombs around it.
                
                counter = 0
                for check_row in range(-1, 2): # Running through adjacent positions for rows and columns.
                    for check_col in range(-1, 2):
                        #  we have to use a try... except... block to avoid index out of range.
                        try:
                            # the sum of current_row and check_row has to be >= 0 to avoid going out of range, same for columns.
                            if current_row + check_row >= 0 and current_col + check_col >= 0:
                                
                                if input_grid[current_row + check_row][current_col + check_col] == "#":
                                    
                                    counter += 1 #if there is a mine adjacent we are adding 1 to our counter.
                        except:
                            IndexError
                output_row.append(counter)
        
        output_grid.append(output_row)
    
    print("\nAnd this is your grid replacing each dash for the number of mines inmediately adjacent.\n")
    [print(x) for x in output_grid]
    
    return output_grid

minesweeper(grid) #Running our grid through the function
