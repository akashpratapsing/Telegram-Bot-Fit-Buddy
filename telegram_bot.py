from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
import Calculator

load_dotenv()
TOKEN = os.getenv("TOKEN")

print(" Started.....")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your Fitness Bot " Fit Buddy ". Use /help to see available commands.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Welcome to your Virtual Fitness Coach Bot! Here are the available commands:

1. **/bmi <weight in kg> <height in cm>** - Calculate your Body Mass Index (BMI).
   Example: `/bmi 70 170`

2. **/calories <weight in kg> <height in cm> <age in years> <gender (M/F)>** - Calculate your daily calorie needs based on the Mifflin-St Jeor equation.
Calculate your Basal Metabolic Rate (BMR).
   Example: `/calories 70 170 25 M`

3. **/bodyfatPercentage** - Calculate your Body Fat percentage using the Navy Method.
   Example: `/bodyfat 70 170 25 M` 

4. **/idealweight <height in cm> <gender (M/F)>** - Calculate your Ideal Weight based on your height and gender.
   Example: `/idealweight 170 M`

5. **/pace <distance in km> <time in minutes>** - Calculate your running pace.
   Example: `/pace 5 30`

6. **/armybodyfat <waist in cm> <neck in cm> <height in cm> <gender (M/F)>** - Calculate your Body Fat percentage as per Army standards.
   Example: `/armybodyfat 80 40 170 M`

7. **/leanbodymass <weight in kg> <height in cm> <age in years> <gender (M/F)>** - Calculate your Lean Body Mass.
   Example: `/leanbodymass 70 170 25 M`

8. **/caloriesburned <activity> <time in minutes> <weight in kg>** - Estimate Calories Burned during an activity.
    Example: `/caloriesburned running 30 70`
      
Feel free to type any of the commands above to get started!
    """
    await update.message.reply_text(help_text)

# This function calculate the BMI - (Body Mass Index)
async def calculate_bmi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Extract weight and height from user input (e.g., /bmi 70 175)
        args = context.args
        
        if len(args) == 2:
            # If weight and height are provided in metric system (kg, cm)
            weight = float(args[0])
            height = float(args[1])
            bmi = Calculator.calculate_bmi(weight, height)
        elif len(args) == 3:
            # If weight is in pounds and height is in feet and inches
            weight = (float(args[0]),)  # Weight in pounds
            height = (int(args[1]), int(args[2]))  # Height in feet and inches
            bmi = Calculator.calculate_bmi(weight, height)
        else:
            await update.message.reply_text("Please provide valid input: /bmi <weight> <height>")
            return
        
        # Send the calculated BMI back to the user
        await update.message.reply_text(f"Your BMI is: {bmi}")

    except (ValueError, IndexError):
        await update.message.reply_text("Invalid input format. Example usage: /bmi 70 175 or /bmi 154 5 9")

# This function calculate the Calories according to body weight, height, age and gender
async def calculate_calories(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Example command: /calories <weight in kg> <height in cm> <age in years> <gender (M/F)>
        weight = float(context.args[0])
        height = float(context.args[1])
        age = int(context.args[2])
        gender = context.args[3].upper()

        if gender == 'M':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        elif gender == 'F':
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            await update.message.reply_text('Please enter a valid gender (M/F).')
            return
        
        await update.message.reply_text(f'Your Basal Metabolic Rate (BMR) is: {bmr:.2f} calories/day.')

    except (IndexError, ValueError):
        await update.message.reply_text('Please provide your weight, height, age, and gender (M/F) in the format: /calories <weight> <height> <age> <gender>')

# This function caculates the range of weight 
async def idle_weight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     try:
        # Extract height from user input (e.g., /normalweight 175 or /normalweight 5 9)
        args = context.args
        
        if len(args) == 1:
            # Height is in centimeters (cm)
            height = float(args[0])
            bmi, min_weight, max_weight = Calculator.calculate_bmi_and_normal_range(height)
            result = f"Your BMI for the middle of the healthy weight range is: {bmi}\n"
            result += f"Healthy weight range for your height: {min_weight} kg to {max_weight} kg."
        elif len(args) == 2:
            # Height is in feet and inches
            height = (int(args[0]), int(args[1]))
            bmi, min_weight, max_weight = Calculator.calculate_bmi_and_normal_range(height)
            result = f"Your BMI for the middle of the healthy weight range is: {bmi}\n"
            result += f"Healthy weight range for your height: {min_weight} kg to {max_weight} kg."
        else:
            await update.message.reply_text("Please provide valid height input: /normalweight <height> or /normalweight <feet> <inches>")
            return
        
        # Send the calculated range back to the user
        await update.message.reply_text(result)
     except (ValueError, IndexError):
        await update.message.reply_text("Invalid input format. Example usage: /normalweight 175 or /normalweight 5 9")


async def calculate_body_fat_percentage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /calculatebfp command."""
    try:
        # Parse arguments from the command
        args = context.args
        if len(args) < 6:
            await update.message.reply_text('Usage: /calculatebfp <age> <height> <weight> <neck> <waist> <gender> [hip]')
            return

        # Extract and convert arguments
        age = int(args[0])
        height = float(args[1])
        weight = float(args[2])
        neck = float(args[3])
        waist = float(args[4])
        gender = args[5].upper()
        hip = float(args[6]) if len(args) > 6 else None

        if gender not in ['M', 'F']:
            await update.message.reply_text('Gender must be "M" for male or "F" for female.')
            return

        # Call the BFP calculation function
        bfp = Calculator.calculate_bfp(age, height, weight, neck, waist, gender, hip)
        
        # Send the result back to the user
        await update.message.reply_text(f'Your Body Fat Percentage (BFP) is: {bfp}%')

    except ValueError as e:
        await update.message.reply_text(f'Error: {e}')
    except Exception as e:
        await update.message.reply_text(f'An unexpected error occurred: {e}')


def main():
    # Initializing the Application with bot token
    application = ApplicationBuilder().token(TOKEN).build()

    # command handlers to the application
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('bmi', calculate_bmi))
    application.add_handler(CommandHandler('calories', calculate_calories))
    application.add_handler(CommandHandler('idealweight', idle_weight))
    application.add_handler(CommandHandler('bodyfatPercentage', calculate_body_fat_percentage))

    # Starting the bot
    application.run_polling()

if __name__ == '__main__':
    main()


