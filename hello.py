from math import log10

def calculate_bfp(age, height, weight, neck, waist, gender, hip=None):
    """
    Calculate body fat percentage based on various methods.
    
    Parameters:
    age : int
        Age of the individual
    height : float
        Height in centimeters (cm) or inches
    weight : float
        Weight in kilograms (kg) or pounds
    neck : float
        Neck circumference in centimeters (cm) or inches
    waist : float
        Waist circumference in centimeters (cm) or inches
    gender : str
        Gender of the individual ('M' for male, 'F' for female)
    hip : float, optional
        Hip circumference in centimeters (cm) or inches (required for females)
    
    Returns:
    float: Calculated body fat percentage
    """
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    
    # Convert weight to kg if in pounds
    if weight < 500:  # Assuming weight in kg is less than 500
        weight_kg = weight
    else:
        weight_kg = weight * 0.453592  # Convert pounds to kg

    # Convert height to meters if in inches
    if height > 100:  # Assuming height in cm is greater than 100
        height_m = height / 100
    else:
        height_m = height * 0.0254  # Convert inches to meters

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    if gender == 'M':
        # For males
        if neck < 100:  # Assuming neck circumference in cm
            bfp = 495 / (1.0324 - 0.19077 * log10(waist - neck) + 0.15456 * log10(height)) - 450
        else:  # Assuming neck circumference in inches
            bfp = 86.010 * log10(waist - neck) - 70.041 * log10(height) + 36.76
    elif gender == 'F':
        if hip is None:
            raise ValueError("Hip circumference is required for females")
        # For females
        if neck < 100:  # Assuming neck circumference in cm
            bfp = 495 / (1.29579 - 0.35004 * log10(waist + hip - neck) + 0.22100 * log10(height)) - 450
        else:  # Assuming neck circumference in inches
            bfp = 163.205 * log10(waist + hip - neck) - 97.684 * log10(height) - 78.387
    
    # Using BMI method for both genders as a fallback
    if gender in ['M', 'F']:
        bfp_bmi = 1.20 * bmi + 0.23 * age - (16.2 if gender == 'M' else 5.4)
        bfp = min(bfp, bfp_bmi)  # Choose the lower of the two estimates

    return round(bfp, 1)


print(calculate_bfp(25, 177.8, 70, 50, 96, "F", 92))