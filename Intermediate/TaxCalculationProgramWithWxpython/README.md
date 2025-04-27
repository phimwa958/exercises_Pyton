# Tax Calculator Application

This is a Python-based desktop application built with wxPython for calculating and recording tax deductions. The program allows users to input financial data, calculate the remaining amount after tax deduction, and store the details in an Excel file for future reference. It also displays past records for easy tracking.

## Features

- **Input Fields**: Allow users to enter a description, the total amount before tax, and the tax amount.
- **Calculation**: Automatically calculates and displays the remaining amount and the percentage of the tax deduction.
- **Record Saving**: Saves the financial data to an Excel file with details such as description, total amount, tax amount, remaining amount, and tax deduction percentage.
- **History View**: Displays the list of previous records with relevant details in a simple interface.
- **Cancel Entry**: Resets the input fields without saving any data.

## Installation

### Prerequisites

Ensure that Python is installed on your system. You can download Python from [python.org](https://www.python.org/).

### Required Python Packages

Install the following Python libraries using `pip`:

```bash
pip install wxpython pandas openpyxl
```

- **wxPython**: Used for building the graphical user interface (GUI).
- **pandas**: Used for data handling and manipulation.
- **openpyxl**: Required for reading and writing Excel files.

### Running the Application

1. Clone or download this repository to your local machine.
2. Run the Python script using:

```bash
python tax_calculator.py
```

## Usage

1. **Enter Data**:
   - Fill in the "คำอธิบาย" field with a description of the transaction.
   - Enter the total amount before tax in the "จำนวนเงินก่อนหักภาษี" field.
   - Enter the tax amount to be deducted in the "จำนวนเงินที่ถูกหัก" field.

2. **Calculate**:
   - Click the "ดูผลลัพธ์" button to calculate and display the remaining amount and the deduction percentage.

3. **Save**:
   - Click the "บันทึก" button to save the record to the Excel file.
   - The record will include the description, the total amount before tax, the tax amount, the remaining amount, the deduction percentage, and the timestamp.

4. **View History**:
   - The application displays a list of all saved records in a panel for easy reference.

5. **Cancel**:
   - Click the "ยกเลิก" button to clear the input fields without saving any data.

## File Structure

```plaintext
.
├── tax_calculator.py          # Main application script
└── tax_records.xlsx           # Excel file storing records (created automatically)
```

## How to Customize

- Modify the `FILE_PATH` variable in `tax_calculator.py` to change the location or name of the Excel file.
- Customize the GUI appearance or functionality as needed using wxPython components.

## Troubleshooting

- **Excel File Not Created**: If the application doesn't create the `tax_records.xlsx` file, ensure that you have the correct permissions to write to the directory.
- **Invalid Input**: Ensure that you only enter numeric values in the "จำนวนเงินก่อนหักภาษี" and "จำนวนเงินที่ถูกหัก" fields. If non-numeric values are entered, an error message will appear.

## License

This project is open-source and free to use. Feel free to contribute or modify the code as needed.

## Acknowledgements

- [wxPython](https://wxpython.org/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

