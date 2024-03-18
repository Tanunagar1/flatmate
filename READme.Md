# Flatmate Bill

## Description

The Flatmate Bill is an application designed to calculate how much each flatmate has to pay based on the total bill amount and the number of days each flatmate stayed in the house during a specific billing period. It generates a PDF report summarizing the details of the bill, including the names of the flatmates, the billing period, and the amount each flatmate has to pay.

## Usage

1. **Enter the bill details**:
   - Provide the total bill amount and the billing period.
   - Input your name and the number of days you stayed in the house during the billing period.
   - Enter the name of the other flatmate and their corresponding number of days stayed.

2. **Calculate**:
   - Click on the "Calculate" button to compute how much each flatmate has to pay.
   - The calculated amounts will be displayed on the screen.

3. **Download PDF report** (Optional):
   - A link will be generated where you can click to download the PDF report.
   - The report contains detailed information about the bill, including the names of the flatmates, the billing period, and the amount each flatmate has to pay.

## Objects

### Bill

- **Attributes**:
  - `amount`: The total amount of the bill.
  - `period`: The billing period for the bill.

### Flatmates

- **Attributes**:
  - `name`: The name of the flatmate.
  - `days_in_house`: The number of days the flatmate stayed in the house during the billing period.

- **Methods**:
  - `pays(bill, other_flatmate)`: Calculates the amount the flatmate has to pay based on the bill amount and the number of days stayed, relative to the other flatmate.

### PDFReport

- **Methods**:
  - `generate(flatmate1, flatmate2, bill)`: Generates a PDF report containing detailed information about the bill, including the names of the flatmates, the billing period, and the amount each flatmate has to pay.
