import math
from math import log10

def calculate_bmi(weight, height):
    """
    Calculate BMI based on weight and height.
    
    Parameters:
    weight : float or tuple
        Weight in kilograms (kg) or pounds (lbs)
        If tuple, first element is interpreted as pounds
    height : float or tuple
        Height in centimeters (cm) or tuple of (feet, inches)
    
    Returns:
    float: Calculated BMI value
    """
    # Determine unit system and convert if necessary
    if isinstance(weight, tuple):
        # Weight is in pounds
        weight_kg = weight[0] * 0.453592  
    else:
        # Weight is in kg
        weight_kg = weight

    if isinstance(height, tuple):
        # Height is in (feet, inches)
        height_m = (height[0] * 12 + height[1]) * 0.0254
    else:
        # Height is in cm
        height_m = height / 100

    bmi = weight_kg / (height_m ** 2)
    
    return round(bmi, 1)


def calculate_bmi_and_normal_range(height):
    """
    Calculate BMI and provide the weight range for "Normal" BMI category.
    
    Parameters:
    height : float or tuple
        Height in centimeters (cm) or tuple of (feet, inches)
    
    Returns:
    tuple: (calculated BMI, weight range for "Normal" BMI)
    """
    if isinstance(height, tuple):
        # Height is in (feet, inches)
        height_m = (height[0] * 12 + height[1]) * 0.0254
    else:
        # Height is in cm
        height_m = height / 100
    
    # Calculate weight range for "Normal" BMI (18.5 to 24.9)
    normal_weight_min = 18.5 * (height_m ** 2)
    normal_weight_max = 24.9 * (height_m ** 2)
    
    # Calculate BMI for the middle of the healthy weight range
    mid_weight = (normal_weight_min + normal_weight_max) / 2
    bmi = mid_weight / (height_m ** 2)
    
    return (round(bmi, 1), round(normal_weight_min, 1), round(normal_weight_max, 1))

def calculate_bfp(age, height, weight, neck, waist, gender, hip=None):
    """
    Calculate body fat percentage based on various methods.
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
    """
    if gender not in ['M', 'F']:
        raise ValueError("Gender must be 'M' for male or 'F' for female")
    
    # Convert weight to kg if in pounds
    if weight < 500:  
        weight_kg = weight
    else:
        weight_kg = weight * 0.453592  

    # Convert height to meters if in inches
    if height > 100:  
        height_m = height / 100
    else:
        height_m = height * 0.0254  

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    if gender == 'M':
        # For males
        if neck < 100:
            bfp = 495 / (1.0324 - 0.19077 * log10(waist - neck) + 0.15456 * log10(height)) - 450
        else:  
            bfp = 86.010 * log10(waist - neck) - 70.041 * log10(height) + 36.76
    elif gender == 'F':
        if hip is None:
            raise ValueError("Hip circumference is required for females")
        # For females
        if neck < 100: 
            bfp = 495 / (1.29579 - 0.35004 * log10(waist + hip - neck) + 0.22100 * log10(height)) - 450
        else: 
            bfp = 163.205 * log10(waist + hip - neck) - 97.684 * log10(height) - 78.387
    
    # Using BMI method for both genders as a fallback
    if gender in ['M', 'F']:
        bfp_bmi = 1.20 * bmi + 0.23 * age - (16.2 if gender == 'M' else 5.4)
        bfp = min(bfp, bfp_bmi)

    return round(bfp, 1)
