vehicles = {
"1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
"1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
"WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
"5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
"1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
"2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
}

def main():
    vin = input("Please enter a vehicle identification number: ")
    if vin in vehicles: 
        vininfo = vehicles[vin]
    
        print(f"Vehicle information for {vin}:")
        print(f"Year: {vininfo [0]}")
        print(f"Manufacturer: {vininfo [1]}")
        print(f"Model: {vininfo [2]}")
        print(f"Color: {vininfo [3]}")
        print(f"Eng Design: {vininfo [4]}")
        print(f"Eng Displace: {vininfo [5]}")
    
    else: 
        print(f"The vehicle identification number {vin} is not found")
        
if __name__ == "__main__":
    main()