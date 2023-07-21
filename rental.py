#RENTAL INcome = 2986.00
#laundry = 0
#storage = 0
#misc = 0

#TOTAL monthly income = 2986.00 

#expenses 
#tax = 537.00
#insurance = 137.00

#utilities = 0.00
#electricty
#water 
#garbage
#gas

# HOA = 324.00
# LAWN = 0
# Vacancy 0.00
# repairs = 200.00
# copex 0.00
# property manage = 200.00
# mortage =1765.00

# total monthly expenses = $3163.00

# cash flow
# income - expenses:177.00 = cash flow

# cash on cash ROI 
# down payment: 78,200
# closing costs: 11730.00
# rehab budget:0
# misc other :0
# total investment:89930
# monthly cash flow x 12 = 2,124 = annual cash flow
# annual cash flow % total investment = 0.02% = cash on cash ROI 


   
class ROI():
     
        def __init__(self, income, expenses, cash_flow):
            self.income = income
            self.expenses = expenses
            self.cash_flow = cash_flow
            
            income = []
            expenses = []
            cash_flow = []

        def showIncome(self):
            Texas_income = input(" Which income of your choice would you like to clarify? Rental/Laundry/Storage/Misc: ")
        
            if Texas_income.lower() == 'rental':
                rental = int(input("Amuse to clarify the rental income: "))
                self.income.append(rental)
                
            elif Texas_income.lower() == 'laundry':
                laundry = int(input("Amuse to clarify the laundry income: "))
                self.income.append(laundry)
                
            elif Texas_income.lower() == 'storage':
                storage = int(input("Amuse to clarify the storage income: "))
                self.income.append(storage)
                
            elif Texas_income.lower() == 'misc':
                storage = int(input("Amuse to clarify the varied income: "))
                self.income.append(storage)
                
            elif Texas_income.lower == 'Quit':
                pass
             
            else:
                print("Try again")
            
            monthly_income = int(sum(self.income))
                
            print(f"The total monthly income is: {monthly_income}")
    
        def Expenses(self):
            Texas_expense = (input(" Which expense would you like to clarify? Tax,Insurance,Utilities,Repairs,Mortgage,storage and Other: "))
                  
            if Texas_expense.lower() == 'tax':
                tax = int(input("Amuse to clarify the tax expense: "))
                self.expenses.append(tax)
                  
            elif Texas_expense.lower() == 'insurance':
                insurance = int(input("Please clarify the insurance expense: "))
                self.expenses.append(insurance)
                  
            elif Texas_expense.lower() == 'utilities':
                utilities = int(input("Amuse to clarify the utilities expense: "))
                self.expenses.append(utilities)
                  
            elif Texas_expense.lower() == 'repairs':
                repairs = int(input("Amuse to clarify the repairs expense: "))
                self.expenses.append(repairs)

            elif Texas_expense.lower() == 'property_manage':
                property_manage = int(input("Amuse to clarify the property_manage expense: "))
                self.expenses.append(property_manage)
                
            elif Texas_expense.lower() == 'mortgage':
                mortgage = int(input("Amuse to clarify the mortgage expense: "))
                self.expenses.append(mortgage)
                
            elif Texas_expense.lower() == 'storage':
                storage = int(input("Amuse to clarify the storage expense: "))
                self.expenses.append(storage)
            
            elif Texas_expense.lower() == 'other':
                other = int(input("Amuse to clarify any other expenses: "))
                self.expenses.append(other)
                
            elif Texas_expense.lower == 'Quit':
                pass
            
            else:
                print("Try again")
           
            monthly_expenses = int(sum(self.expenses))
            
            print(f"The monthly expenses total to an amount of: {monthly_expenses}")
                  
        def Cash_Flow(self):
            current_cash_Flow = sum(self.income) - sum(self.expenses)
            self.cash_flow.append(current_cash_Flow)
            print(f"The current cash flow is: {current_cash_Flow}")
            
        
                  
        def ROI(self):
            total_investment = int(input("Amuse to clarify the total investment: "))
            cash_Flow = sum(self.cash_flow)
            annual_cash_Flow = cash_Flow * 12
            ROI = (annual_cash_Flow / total_investment) 
    
            print(f"The cash on cash ROI = {ROI} percent.")

        def run():
            property_Value = ROI([], [], [])
            while True:
                response = input("Select an alternative of your choice: Income,Expenses,Cash Flow,closing cost,down payment,ROI - Quit to Stop - ")

                if response.lower() == 'Income':
                    property_Value.Income()
                elif response.lower() == 'Expenses':
                    property_Value.Expenses()
                elif response.lower() == 'Cash Flow':
                    property_Value.Cash_Flow()
                elif response.lower() == 'Closing cost':
                    property_Value.closing_cost()
                elif response.lower() == 'Down payment':
                    property_Value.down_payment()
                elif response.lower() == 'ROI':
                    property_Value.ROI()
                elif response.lower() == 'Quit':
                    break
                else:
                    print("Try Again")
        run()
    