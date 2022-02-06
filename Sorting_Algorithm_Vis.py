from tkinter import *
from tkinter import ttk
# to create a random new array
import random
from Bubble_sort import bubbleSort
from Selection_sort import selectionSort
from MergeSort import merge_sort
from tkinter import messagebox




# basic tkinter layout
root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='grey')



# Variables
selected_alg = StringVar() # stores the output of the combobox
data = [] # declare global array since there are two buttons accessing this data

# colorArray to hold color names
def drawData(data, colorArray): # to make ui work, takes in array with data to draw

    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1) # width of bar graphs, calculated.

    offset = 10 # to not start at border, changed from 30 to 10 pixels
    spacing = 10 # spacing between bars

    # returns the largest iterable, e.g. 90, by dividing each element by 90.
    # in other words, bars are resized to canvas
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left, composed of two coordinates.
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340 # needs to be less than c_height, at 340 40 pixels are left
        # bottom right coordinates, tkinter will connect these two across and below to form a rectangle
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i])) # writes number over bar
    # update the steps after every change
    root.update()

def Generate():
    print('Alg selected: ' + selected_alg.get()) # grabs the input value
    global data # grabs global data array to modify it by generating new data below
    minValue = int(minEntry.get())
    maxValue = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = [] # resets data once generate button is clicked, and then generates new data
    for e in range(size):
        data.append(random.randrange(minValue, maxValue+1)) # creates a new data set for range in size

    # second parameter passes in array of red for each element in data
    drawData(data, ['red' for x in range(len(data))])

def popup():
    # Parameters 2: 1) titlebar 2) message in the popup
    messagebox.showinfo('Title',
            "1) Select the Data Size, Min and Max Value and click Generate.\n\n"
            "2) Choose the Algorithm to run.\n\n"
            "3) Select the Speed to run the algorithm and click Start.\n\n")


def StartAlgorithm():
    global data
    # third parameter is passed in to receive the speed input = the timetick amount for the algorithm
    # can now regulate speed of algorithm
    if algMenu.get() == 'Bubble Sort':
        bubbleSort(data, drawData, speedScale.get())

    if algMenu.get() == 'Selection Sort':
        selectionSort(data, drawData, speedScale.get())

    if algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())

    # displays all bars in green when algorithm is done
    drawData(data, ['green' for x in range(len(data))])

# frame, the top of the options with root as the master
UI_frame = Frame(root, width=600, height=200, bg='lightblue')
#grid
UI_frame.grid(row=0, column=0, padx=(2,2), pady=5) # display runs off the screen, need to fix this

# create the canvas
canvas = Canvas(root, width=600, height=380, bg='grey')
# create canvas.grid variable, with row=1 so that its under the ui frame
canvas.grid(row=1, column=0, padx=10, pady=5)

# user interface area
# row[0], what is the sticky parameter?
Label(UI_frame, text="Algorithm: ", bg='white').grid(row=0, column=0, padx=5, pady=0)

# create the combobox and keep a reference of it inside algMenu.
# the 1st parameter defines location where its displayed. 2nd parameter stores the output.
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Selection Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0) # sets the default value

# speed to play algorithm, from time 'to step' of the algorithm. Length of item is 200 pixels
speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)


# row[1], row set to 1 in order to work on next row
# create the input box and save the reference; entry object is created and place inside the ui frame
sizeEntry = Scale(UI_frame, from_=3, to=20, length=200, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

# min value
minEntry = Scale(UI_frame, from_=0, to=5, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

# max value
maxEntry = Scale(UI_frame, from_=5, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# create buttons
Button(UI_frame, text="Generate", command=Generate, highlightbackground='red').grid(row=3, column=0, padx=20, pady=20)
Button(UI_frame, text="How to use", command=popup, highlightbackground='orange').grid(row=3, column=2, padx=20, pady=20)
Button(UI_frame, text="Start", command=StartAlgorithm, highlightbackground='yellow').grid(row=3, column=1, padx=20, pady=20)

# starts the application
root.mainloop()