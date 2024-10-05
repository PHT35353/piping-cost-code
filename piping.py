import pandas as pd
import math

def Barlow(S, D, t):
    P = (2*S*t)/((D))
    return P

def get_user_inputs1():
    pressure = float(input("Enter the pressure (bar): "))
    temperature = float(input("Enter the temperature (°C): "))
    medium = input("Enter the medium: ")
    return pressure, temperature, medium

def choose_pipe_material(P, T, M): # No B1003
        # Medium constraints
        if M.lower() in ('water glycol', 'water-glycol', 'pressurized water', 'pressurized-water'):
            if P > 10 and T > 425:
                return 'B1005'
            else:
                return 'B1008'

        # Pipe material choices based on pressure and temperature
        if P <= 10:
            if T <= 60:
                material = 'B1008'
            elif 60 <= T <= 425:
                material = 'B1001'  # Specify both B1001 and B1003 as valid options
            else:
                material = 'B1008'
        else:
            if T <= 425:
                material = 'B1001'  # Specify both B1001 and B1003 as valid options
            else:
                material = 'B1005'

        # Medium-specific constraints
        if M.lower() in ('steam', 'thermal oil', 'thermal-oil'):
            return material
        else:
            # Handle the case for B1003 when applicable
            if M.lower() in ('water glycol', 'water-glycol', 'pressurized water', 'pressurized-water'):
                return 'B1008' if material != 'B1005' else material
                



def stress_b1001(): # T < 425 and not corrosion resistant
    Nominal_diameter = [
        21.3, 26.7, 33.4, 48.3, 60.3, 88.9, 114.3, 141.3, 168.3, 219.1, 273.0, 323.9, 355.6, 406.4, 508.0
          ]# in mm
    Wall_thickness = [
        2.8, 2.9, 3.4, 3.7, 3.9, 5.5, 6.0, 6.6, 7.1, 8.2, 9.3, 9.5, 9.5, 9.5, 9.5 
        ] # in mm
    FOS = 3  # Updated to 3
    Bar_yield_strength = 2050 #Assumption grade A
    Allowable_stress_bar = 2050 / FOS
    
    x = [Barlow(Allowable_stress_bar, dia, thick) for dia, thick in zip(Nominal_diameter, Wall_thickness)]
    Pressure_allowance = [round(i, 2) for i in x]
    print(Pressure_allowance)
        
def stress_b1003():
    nominal_diameter = [
        21.3, 26.7, 33.4, 48.3, 60.3, 88.9, 114.3, 141.3, 168.3, 219.1, 273.0, 323.9, 355.6, 406.4, 508.0
          ]# in mm
    wall_thickness_mm = [
        3.7, 3.9, 4.5, 5.1, 5.5, 7.6, 8.6, 9.5, 11.0, 12.7, 12.7, 12.7, 12.7, 12.7, 12.7
        ]
    FOS = 3  # Updated to 3
    Bar_yield_strength = 2050 #Assumption grade A
    Allowable_stress_bar = 2050 / FOS
    
    x = [Barlow(Allowable_stress_bar, dia, thick) for dia, thick in zip(nominal_diameter, wall_thickness_mm)]
    Pressure_allowance = [round(i, 2) for i in x]
    print(Pressure_allowance)

def stress_b1005_304(): #Stainless steel pipes and T > 425 and corrosion resistant 
    outside_diameter_in_mm = [
        21.34, 26.67, 33.4, 42.16, 48.26, 60.32, 73.02, 88.9, 114.3, 141.3, 168.27, 219.07, 273.05, 323.85
        ]
    wall_thickness_in_mm = [
        2.11, 2.11, 2.77, 2.77, 2.77, 2.77, 3.05, 3.05, 3.05, 3.4, 3.4, 3.76, 4.19, 4.57
        ]   
    FOS = 3  # Updated to 3
    Bar_yield_strength = 2050
    Allowable_stress_bar = 2050 / FOS 

    x = [Barlow(Allowable_stress_bar, dia, thick) for dia, thick in zip(outside_diameter_in_mm, wall_thickness_in_mm)]
    Pressure_allowance = [round(i, 2) for i in x]
    print(Pressure_allowance)

def stress_b1007(): # T < 70
    outside_diameter_mm = [
    20, 25, 25, 32, 32, 40, 40, 50, 50, 63, 63, 75, 75, 90, 90, 
    110, 110, 125, 125, 160, 160, 200, 200, 250, 250, 315, 315
    ]
    wall_thickness_mm = [
    1.9, 1.6, 2.3, 1.9, 3.0, 2.3, 3.7, 2.9, 4.6, 3.6, 5.8, 4.3, 6.9, 5.1, 8.2, 
    6.3, 10.0, 7.1, 11.4, 9.1, 14.6, 11.4, 18.2, 14.2, 22.8, 17.9, 28.7
    ]
    cost_per_100_m = [
    237, 226, 295, 226, 295, 306, 480, 514, 751, 768, 1155, 1075, 1665, 1515, 2240,
    2240, 3280, 2740, 4225, 4610, 6815, 7045, 10740, 10740, 16750, 18020, 27605
    ]
    
    FOS = 3  # Updated to 3
    Bar_yield_strength = 250
    Allowable_stress_bar = 250 / FOS

    x = [Barlow(Allowable_stress_bar, dia, thick) for dia, thick in zip(outside_diameter_mm, wall_thickness_mm)]
    Pressure_allowance = [round(i, 2) for i in x]
    print(Pressure_allowance)

def stress_b1008(): # T < 65 and anti corrosion
    outside_diameter_mm = [25, 32, 40, 50, 50, 63, 63, 75, 75, 90, 90, 110, 110, 125, 125, 160, 160, 200, 200]
    wall_thickness_mm = [1.5, 1.8, 1.9, 1.8, 2.4, 1.8, 3.0, 2.2, 3.6, 2.7, 4.3, 3.2, 5.3, 3.7, 6.0, 4.7, 7.7, 5.9, 9.6]
    cost_per_100_m = [208, 243, 312, 370, 445, 531, 658, 728, 959, 1180, 1365, 1500, 1985, 2170, 2770, 3475, 4205, 6120, 7450]

    FOS = 3  # Updated to 3
    Bar_yield_strength = 550
    Allowable_stress_bar = 550 / FOS

    x = [Barlow(Allowable_stress_bar, dia, thick) for dia, thick in zip(outside_diameter_mm, wall_thickness_mm)]
    Pressure_allowance = [round(i, 2) for i in x]
    print(Pressure_allowance)


# Main function to filter pipes based on user input, without outputting nominal diameter and pressure
def B1001_filter(P, file_path='B1001.csv'):
    # Load the cleaned data (assuming it's in the same format as above)
    df = pd.read_csv(file_path)

    # Split the data and clean it as before
    df_split = df['Nominal diameter in inches;External diameter in mm;Wall thickness in mm;Weight in kg/m;Cost per 100 m in Euro\'s;Pressure in bar'].str.split(';', expand=True)
    df_split.columns = ['Nominal diameter (inches)', 'External diameter (mm)', 'Wall thickness (mm)', 'Weight (kg/m)', 'Cost per 100 m (Euro)', 'Pressure (bar)']

    # Convert necessary columns to numeric
    df_split['External diameter (mm)'] = pd.to_numeric(df_split['External diameter (mm)'])
    df_split['Wall thickness (mm)'] = pd.to_numeric(df_split['Wall thickness (mm)'])
    df_split['Cost per 100 m (Euro)'] = pd.to_numeric(df_split['Cost per 100 m (Euro)'])
    df_split['Pressure (bar)'] = pd.to_numeric(df_split['Pressure (bar)'])

    # Convert the cost per 100 m to cost per meter
    df_split['Cost per m (Euro)'] = df_split['Cost per 100 m (Euro)'] / 100

    try:
        # Get user input for the pressure
        input_pressure = P
        
        # Filter the pipes that have a pressure rating greater than or equal to the input pressure
        available_pipes = df_split[df_split['Pressure (bar)'] >= input_pressure]
        
        if available_pipes.empty:
            print(f"No pipes found for the pressure of {input_pressure} bar.")
        else:
            print(f"Available carbon steel pipesfor {input_pressure} bar or higher pressure:")
            print(available_pipes[['External diameter (mm)', 'Wall thickness (mm)', 'Cost per m (Euro)']])
    except ValueError:
        print("Invalid input. Please enter a valid number for pressure.")

def B1003_filter(P, file_path='B1003.csv'):
    # Load the cleaned data (assuming it's in the same format as above)
    df = pd.read_csv(file_path)

    # Split the data and clean it as before
    df_split = df['Nominal diameter in inches;Outside diameter in mm;Wall thickness in mm;Weight in kg/m;Cost per 100 m;Pressure in bar'].str.split(';', expand=True)
    df_split.columns = ['Nominal diameter (inches)', 'External diameter (mm)', 'Wall thickness (mm)', 'Weight (kg/m)', 'Cost per 100 m (Euro)', 'Pressure (bar)']

    # Convert necessary columns to numeric
    df_split['External diameter (mm)'] = pd.to_numeric(df_split['External diameter (mm)'])
    df_split['Wall thickness (mm)'] = pd.to_numeric(df_split['Wall thickness (mm)'])
    df_split['Cost per 100 m (Euro)'] = pd.to_numeric(df_split['Cost per 100 m (Euro)'])
    df_split['Pressure (bar)'] = pd.to_numeric(df_split['Pressure (bar)'])

    # Convert the cost per 100 m to cost per meter
    df_split['Cost per m (Euro)'] = df_split['Cost per 100 m (Euro)'] / 100

    try:
        # Get user input for the pressure
        input_pressure = P
        
        # Filter the pipes that have a pressure rating greater than or equal to the input pressure
        available_pipes = df_split[df_split['Pressure (bar)'] >= input_pressure]
        
        if available_pipes.empty:
            print(f"No pipes found for the pressure of {input_pressure} bar.")
        else:
            print(f"Available extra strong carbon steel pipes for {input_pressure} bar or higher pressure:")
            print(available_pipes[['External diameter (mm)', 'Wall thickness (mm)', 'Cost per m (Euro)']])
    except ValueError:
        print("Invalid input. Please enter a valid number for pressure.")

def B1005_filter(P, file_path='B1005.csv'):

    # Load the cleaned data (assuming it's in the same format as above)
    df = pd.read_csv(file_path) #(file_path, usecols = [])+

    # Split the data and clean it as before
    df_split = df['Nominal diameter in inches;Outside diameter in mm;Wall thickness in mm;Weight in kg/m;Cost per m (304 L);Cost per m (316 L);Pressure in bar'].str.split(';', expand=True)
    df_split.columns = ['Nominal diameter (inches)', 'External diameter (mm)', 'Wall thickness (mm)', 'Weight (kg/m)', 'Cost per m04 (Euro)', 'Cost per m16 (Euro)', 'Pressure (bar)']

    # Convert necessary columns to numeric
    df_split['External diameter (mm)'] = pd.to_numeric(df_split['External diameter (mm)'])
    df_split['Wall thickness (mm)'] = pd.to_numeric(df_split['Wall thickness (mm)'])
    df_split['Cost per m (Euro)'] = pd.to_numeric(df_split['Cost per m04 (Euro)'])
    df_split['Pressure (bar)'] = pd.to_numeric(df_split['Pressure (bar)'])

    try:
        # Get user input for the pressure
        input_pressure = P
        
        # Filter the pipes that have a pressure rating greater than or equal to the input pressure
        available_pipes = df_split[df_split['Pressure (bar)'] >= input_pressure]
        
        if available_pipes.empty:
            print(f"No pipes found for the pressure of {input_pressure} bar.")
        else:
            print(f"Available stainless steel pipes for {input_pressure} bar or higher pressure:")
            print(available_pipes[['External diameter (mm)', 'Wall thickness (mm)', 'Cost per m (Euro)']]) #Change here to view pressure
    except ValueError:
        print("Invalid input. Please enter a valid number for pressure.")

def B1007_filter(P, file_path='B1007.csv'): #Not fixed
    
    # Load the cleaned data (assuming it's in the same format as above)
    df = pd.read_csv(file_path)

    # Split the data and clean it as before
    df_split = df['Outside Diameter (mm);Wall Thickness (mm);Cost per 100 meters;Working Pressure (bar)'].str.split(';', expand=True)
    df_split.columns = ['External diameter (mm)', 'Wall thickness (mm)', 'Cost per 100 m (Euro)', 'Pressure (bar)']

    # Convert necessary columns to numeric
    df_split['External diameter (mm)'] = pd.to_numeric(df_split['External diameter (mm)'])
    df_split['Wall thickness (mm)'] = pd.to_numeric(df_split['Wall thickness (mm)'])
    df_split['Cost per 100 m (Euro)'] = pd.to_numeric(df_split['Cost per 100 m (Euro)'])
    df_split['Pressure (bar)'] = pd.to_numeric(df_split['Pressure (bar)'])

    # Convert the cost per 100 m to cost per meter
    df_split['Cost per m (Euro)'] = df_split['Cost per 100 m (Euro)'] / 100

    try:
        # Get user input for the pressure
        input_pressure = P
        
        # Filter the pipes that have a pressure rating greater than or equal to the input pressure
        available_pipes = df_split[df_split['Pressure (bar)'] >= input_pressure]
        
        if available_pipes.empty:
            print(f"No pipes found for the pressure of {input_pressure} bar.")
        else:
            print(f"Available pipes for {input_pressure} bar or higher pressure:")
            print(available_pipes[['External diameter (mm)', 'Wall thickness (mm)', 'Cost per m (Euro)']])
    except ValueError:
        print("Invalid input. Please enter a valid number for pressure.")

def B1008_filter(P, file_path='B1008.csv'):
    
    # Load the cleaned data (assuming it's in the same format as above)
    df = pd.read_csv(file_path)

    # Split the data and clean it as before
    df_split = df['Outside Diameter (mm);Wall Thickness (mm);Working Pressure (bar);Cost per 100 m'].str.split(';', expand=True)
    df_split.columns = ['External diameter (mm)', 'Wall thickness (mm)', 'Pressure (bar)', 'Cost per 100 m (Euro)']

    # Convert necessary columns to numeric
    df_split['External diameter (mm)'] = pd.to_numeric(df_split['External diameter (mm)'])
    df_split['Wall thickness (mm)'] = pd.to_numeric(df_split['Wall thickness (mm)'])
    df_split['Cost per 100 m (Euro)'] = pd.to_numeric(df_split['Cost per 100 m (Euro)'])
    df_split['Pressure (bar)'] = pd.to_numeric(df_split['Pressure (bar)'])

    # Convert the cost per 100 m to cost per meter
    df_split['Cost per m (Euro)'] = df_split['Cost per 100 m (Euro)'] / 100

    try:
        # Get user input for the pressure
        input_pressure = P
        
        # Filter the pipes that have a pressure rating greater than or equal to the input pressure
        available_pipes = df_split[df_split['Pressure (bar)'] >= input_pressure]
        
        if available_pipes.empty:
            print(f"No pipes found for the pressure of {input_pressure} bar.")
        else:
            print(f"Available PVC pipes for {input_pressure} bar or higher pressure:")
            print(available_pipes[['External diameter (mm)', 'Wall thickness (mm)', 'Cost per m (Euro)']])
    except ValueError:
        print("Invalid input. Please enter a valid number for pressure.")


def Pipe_finder(material, P): # No B1003 as input
    if material == 'B1001':
        # Special case: Combine results from both B1001_filter and B1003_filter
        B1001_filter(P, file_path='B1001.csv')
        print()
        B1003_filter(P, file_path='B1003.csv')
        
    elif material == 'B1005':
        B1005_filter(P, file_path='B1005.csv')
        
    elif material == 'B1008':
         B1008_filter(P, file_path= 'B1008.csv')
        
    else:
        return "Material not found"
def data_print(result):

    if isinstance(result, tuple):
        # Special case where both B1001 and B1003 data are returned
        pipe_data_B1001, pipe_data_B1003 = result
        print(f"Pipe data B1001: {pipe_data_B1001}")
        print(f"Pipe data B1003: {pipe_data_B1003}")
    else:
        # Normal case where only one pipe data is returned
        print(f"Pipe data: {result}")

def pipe_main():
    try:
        P, T, M = get_user_inputs1()
        Pipe_Material = choose_pipe_material(P, T, M)
        Pipe_finder(Pipe_Material, P)

    except Exception as e:
        print(f"An error occurred: {e}")

pipe_main()
