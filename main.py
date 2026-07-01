import os
import datetime

# run pytest and generate report
def generateReport():
    # create a dynamic directory name using timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    allure_dir = f"reports_allure/{timestamp}"

    # Ensure directory exists (pytest will create it too, but for safety)
    os.makedirs(allure_dir, exist_ok=True)

    # run pytest and use serve to generate the report
    os.system(f"pytest --alluredir={allure_dir}")
    os.system(f"allure serve {allure_dir}") # comment this line to not generate the report


# run main to run whole test suite
if __name__ == "__main__":
    generateReport()
    print("Press any key to exit")
