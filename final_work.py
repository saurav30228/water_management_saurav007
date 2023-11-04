import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
import requests

def send_notification(ions, concentrations):
    bot_token = '6457474946:AAEEM8-ZhKrrUTVzDLQiys9k56MPgmLhrQg'  
    chat_id = '1656986995'  

    # Create a message with the ions and concentrations
    message = "Heavy Metal Ions and Concentrations:\n"
    for ion, concentration in zip(ions, concentrations):
        message += f"{ion}: {concentration}\n"

    base_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(base_url)
def display_graphs(welcome_window, file_path):
    # Clear the welcome page widgets
    for widget in welcome_window.winfo_children():
        widget.destroy()
        
    # Button to go back to the welcome page
    back_button = tk.Button(welcome_window, text="Go Back", command=lambda: show_welcome(welcome_window))
    back_button.pack(side="top", anchor="nw") 

    mix_d = np.loadtxt(file_path)
    xA = mix_d[:, 0:2]
    pA = xA[:, 0]
    cA = xA[:, 1]
    xB = mix_d[:, 2:4]
    pB = xB[:, 0]
    cB = xB[:, 1]
    xC = mix_d[:, 4:6]
    pC = xC[:, 0]
    cC = xC[:, 1]
    xD = mix_d[:, 6:8]
    pD = xD[:, 0]
    cD = xD[:, 1]
    xE = mix_d[:, 8:10]
    pE = xE[:, 0]
    cE = xE[:, 1]

    # Creating a figure with subplots for the first set of data
    fig, axes = plt.subplots(5, 1, figsize=(4, 8))

    # Plotting subplots for each dataset
    axes[0].plot(pA, cA)
    axes[0].set_ylabel('current')
    axes[0].set_xlabel('potential')
    axes[0].set_title(' 0.5ppb')

    axes[1].plot(pB, cB)
    axes[1].set_ylabel('current')
    axes[1].set_xlabel('potential')
    axes[1].set_title('1ppb')

    axes[2].plot(pC, cC)
    axes[2].set_ylabel('current')
    axes[2].set_xlabel('potential')
    axes[2].set_title('1.5ppb')

    axes[3].plot(pD, cD)
    axes[3].set_ylabel('current')
    axes[3].set_xlabel('potential')
    axes[3].set_title('2ppb')

    axes[4].plot(pE, cE)
    axes[4].set_ylabel('current')
    axes[4].set_xlabel('potential')
    axes[4].set_title('2.5ppb')

    fig.tight_layout(pad=1.0)

    canvas = FigureCanvasTkAgg(fig, master=welcome_window)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=False, fill='both')

def upload_file(file_label):
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=os.path.basename(file_path))

def show_result():
    #print("Showing result...")
    # Clear the welcome page widgets
    for widget in welcome_window.winfo_children():
        widget.destroy()
        
    # Button to go back to the welcome page
    back_button = tk.Button(welcome_window, text="Go Back", command=lambda: show_welcome(welcome_window))
    back_button.pack(side="top", anchor="nw") 
        
    mix_d = np.loadtxt('As_Cr.txt')
    xA = mix_d[:, 0:2]
    pA = xA[:, 0]
    cA = xA[:, 1]
    xB = mix_d[:, 2:4]
    pB = xB[:, 0]
    cB = xB[:, 1]
    xC = mix_d[:, 4:6]
    pC = xC[:, 0]
    cC = xC[:, 1]
    xD = mix_d[:, 6:8]
    pD = xD[:, 0]
    cD = xD[:, 1]
    xE = mix_d[:, 8:10]
    pE = xE[:, 0]
    cE = xE[:, 1]
    
    # Loading data for ARSENIC and CHROMIUM arrays
    AsIII_Arr = np.loadtxt('AsIII_array.txt')
    AsV_Arr = np.loadtxt('arsenicV_array.txt')
    CrIII_Arr = np.loadtxt('CrIII_array_.5.txt')
    CrVI_Arr = np.loadtxt('CrVI_array_.5.txt')
    
    # Finding indices of interest based on potential range
    ind1_AsIII = np.where((pC >= 0.30) & (pC <= 0.32))[0]
    ind1_AsV = np.where((pC >= 1.30) & (pC <= 1.33))[0]
    ind2_CrIII = np.where((pC >= 0.32) & (pC <= 0.38))[0]
    ind2_CrVI = np.where((pC >= 1.38) & (pC <= 1.41))[0]
    
    # Extracting potential values for ARSENIC and CHROMIUM
    asIII = pC[ind1_AsIII]
    asV = pC[ind1_AsV]
    cr_III = pC[ind2_CrIII]
    cr_VI = pC[ind2_CrVI]
    
    # Extracting current values for ARSENIC and CHROMIUM
    x1_asIII = cC[ind1_AsIII]
    x1_asV = cC[ind1_AsV]
    x1_cr_III = cC[ind2_CrIII]
    x1_cr_VI = cC[ind2_CrVI]
    
    # Finding maximum current and corresponding potential for ARSENIC (asIII)
    max_x1_asIII = np.max(x1_asIII)
    max_x1_asIII_rows = np.argmax(x1_asIII)
    as_at_max_x1_asIII = asIII[max_x1_asIII_rows]
    
    # Finding maximum current and corresponding potential for ARSENIC (asV)
    max_x1_asV = np.max(x1_asV)
    max_x1_asV_rows = np.argmax(x1_asV)
    as_at_max_x1_asV = asV[max_x1_asV_rows]
    
    # Finding maximum current and corresponding potential for CHROMIUM (crIII)
    max_x1_crIII = np.max(x1_cr_III)
    max_x1_crIII_rows = np.argmax(x1_cr_III)
    cr_at_max_x1_crIII = cr_III[max_x1_crIII_rows]
    
    # Finding maximum current and corresponding potential for CHROMIUM (crVI)
    max_x1_crVI = np.max(x1_cr_VI)
    max_x1_crVI_rows = np.argmax(x1_cr_VI)
    cr_at_max_x1_crVI = cr_VI[max_x1_crVI_rows]
    
    
    p_known_asIII = AsIII_Arr[:, 1]
    c_known_asIII = AsIII_Arr[:, 0]
    p_known_asV = AsV_Arr[:, 1]
    c_known_asV = AsV_Arr[:, 0]
    
    # Unique Potential
    p_unique_asIII, idx_AsIII = np.unique(p_known_asIII, return_index=True)
    c_unique_asIII = c_known_asIII[idx_AsIII]
    
    # Interpolating
    new_c_values_asIII = np.interp(as_at_max_x1_asIII, p_unique_asIII, c_unique_asIII, left=0, right=0)
    
    p_known_asV = AsV_Arr[:, 1]
    c_known_asV = AsV_Arr[:, 0]
    
    # Finding unique potential values and corresponding concentration values for ARSENIC (asV)
    p_unique_asV, idx_AsV = np.unique(p_known_asV, return_index=True)
    c_unique_asV = c_known_asV[idx_AsV]
    # Interpolate to find new concentration values at max potential for ARSENIC (asV)
    new_c_values_asV = np.interp(as_at_max_x1_asV, p_unique_asV, c_unique_asV, left=0, right=0)
    
    # Defining known potential and concentration values for CHROMIUM (crIII)
    p_known_crIII = CrIII_Arr[:, 1]
    c_known_crIII = CrIII_Arr[:, 0]
    
    # Find unique potential values and corresponding concentration values for CHROMIUM (crIII)
    p_unique_crIII, idx_crIII = np.unique(p_known_crIII, return_index=True)
    c_unique_crIII = c_known_crIII[idx_crIII]
    
    # Interpolate to find new concentration values at max potential for CHROMIUM (crIII
    new_c_values_crIII = np.interp(cr_at_max_x1_crIII, p_unique_crIII, c_unique_crIII, left=0, right=0)
    
    # Process CHROMIUM data (crVI)
    # Define known potential and concentration values for CHROMIUM (crVI)
    p_known_crVI = CrVI_Arr[:, 1]
    c_known_crVI = CrVI_Arr[:, 0]
    
    # Find unique potential values and corresponding concentration values for CHROMIUM (crVI)
    p_unique_crVI, idx_crVI = np.unique(p_known_crVI, return_index=True)
    c_unique_crVI = c_known_crVI[idx_crVI]
    
    # Interpolate to find new concentration values at max potential for CHROMIUM (crVI)
    new_c_values_crVI = np.interp(cr_at_max_x1_crVI, p_unique_crVI, c_unique_crVI, left=0, right=0)
    
    # plt.tight_layout()
    fig = plt.figure(figsize=(8, 6))

    # Displaying the Concentrations of Heavy Metal Ions
    print("Heavy Metal Ions and Concentrations:")
    ions = []
    concentrations = []

    if new_c_values_asIII:
        ions.append("AsIII")
        concentrations.append(new_c_values_asIII)

    if new_c_values_asV:
        ions.append("AsV")
        concentrations.append(new_c_values_asV)

    if new_c_values_crIII:
        ions.append("CrIII")
        concentrations.append(new_c_values_crIII)

    if new_c_values_crVI:
        ions.append("CrVI")
        concentrations.append(new_c_values_crVI)

    # Plotting the concentrations
    bars = plt.bar(ions, concentrations, color=['blue', 'green', 'orange', 'red'])

    # Add the values on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom')  # va: vertical alignment

    plt.xlabel('Heavy Metal Ions')
    plt.ylabel('Concentration')
    plt.title('Concentration of Heavy Metal Ions')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(axis='y')  # Show grid lines for y-axis

    # Add a legend
    plt.legend(bars, ions)

    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=welcome_window)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='x')
    # For Notifications
    print("Heavy Metal Ions and Concentrations:")
    ions = []
    concentrations = []
    
    if new_c_values_asIII:
        ions.append("AsIII")
        concentrations.append(new_c_values_asIII)
    
    if new_c_values_asV:
        ions.append("AsV")
        concentrations.append(new_c_values_asV)
    
    if new_c_values_crIII:
        ions.append("CrIII")
        concentrations.append(new_c_values_crIII)
    
    if new_c_values_crVI:
        ions.append("CrVI")
        concentrations.append(new_c_values_crVI)
    
    # Send the ions and concentrations to the Telegram bot
    send_notification(ions, concentrations)

def close_app(welcome_window):
    welcome_window.destroy()
from tkinter import ttk
from ttkthemes import ThemedTk

def show_welcome(welcome_window):
    # Clear the welcome page widgets
    for widget in welcome_window.winfo_children():
        widget.destroy()

    welcome_label = ttk.Label(welcome_window, text="Welcome To Water Management", font=("Arial", 20))
    welcome_label.pack()

    button_frame = ttk.Frame(welcome_window)
    button_frame.pack(side="bottom", fill="x")

    upload_frame = ttk.Frame(button_frame)
    upload_frame.pack(side="left", padx=10, pady=10)
    upload_button = ttk.Button(upload_frame, text="Upload File")
    upload_button.pack()
    file_label = ttk.Label(upload_frame, text="")
    file_label.pack()
    upload_button.config(command=lambda: upload_file(file_label))

    visualize_frame = ttk.Frame(button_frame)
    visualize_frame.pack(side="left", padx=10, pady=10)
    visualize_button = ttk.Button(visualize_frame, text="Visualize Input", command=lambda: display_graphs(welcome_window, file_label.cget("text")))
    visualize_button.pack()
    visualize_label = ttk.Label(visualize_frame, text="")
    visualize_label.pack()

    result_frame = ttk.Frame(button_frame)
    result_frame.pack(side="left", padx=10, pady=10)
    result_button = ttk.Button(result_frame, text="Show Result", command=show_result)
    result_button.pack()
    result_label = ttk.Label(result_frame, text="")
    result_label.pack()

    quit_frame = ttk.Frame(button_frame)
    quit_frame.pack(side="left", padx=10, pady=10)
    quit_button = ttk.Button(quit_frame, text="Quit", command=lambda: close_app(welcome_window))
    quit_button.pack()
    quit_label = ttk.Label(quit_frame, text="")
    quit_label.pack()

welcome_window = tk.Tk()
welcome_window.title("Welcome")
welcome_window.state('zoomed')

show_welcome(welcome_window)

welcome_window.mainloop()








