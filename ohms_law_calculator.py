def ohms_law_calculator():
    while True:
        print("\nOhm's Law Calculator")
        print("Enter any two values to calculate the third.")
        print("Type 'quit' to exit.")
        
        try:
            # Get user input
            voltage_input = input("Enter Voltage (V): ")
            if voltage_input.lower() == 'quit':
                break
            voltage = float(voltage_input or "0")
            
            current_input = input("Enter Current (I): ")
            if current_input.lower() == 'quit':
                break
            current = float(current_input or "0")
            
            resistance_input = input("Enter Resistance (R): ")
            if resistance_input.lower() == 'quit':
                break
            resistance = float(resistance_input or "0")
            
            # Calculate the missing value
            if voltage and current:
                resistance = voltage / current
                print(f"Resistance (R) = {resistance:.2f} ohms")
            elif voltage and resistance:
                current = voltage / resistance
                print(f"Current (I) = {current:.2f} A")
            elif current and resistance:
                voltage = current * resistance
                print(f"Voltage (V) = {voltage:.2f} V")
            else:
                print("Please provide at least two values.")
            
            # Optional: Calculate Power
            if voltage and current:
                power = voltage * current
                print(f"Power (P) = {power:.2f} W")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
ohms_law_calculator()