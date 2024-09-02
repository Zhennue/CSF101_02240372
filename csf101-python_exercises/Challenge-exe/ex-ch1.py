with open( 'fruit_transactions.txt', 'r') as file:
    content = file.read()
    print(content)

with open('fruit_transaction.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())