
country= str(input('Enter your country: ').title().strip())
countries= ["Egypt", "Palestine", 'Syria', "Yemen", "Ksa", "Usa", "Bahrain", "England" ]


price =100
discount= 30

if country in countries:
    print(f'Your country Eligible For Discount And The Price After Discount is ${ price - discount }')
else:
    print(f'Your country Not Eligible For Discount And The Price After Discount is ${price}')