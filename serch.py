import csv
# data extraction

state=input(" Please Enter State only Maharashtra/Karnataka/Tamilnadu or India \n ")
operation=input(" please Enter cheapest/highest/average \n ")
cost=input("cost or rating \n ")
csv_file=csv.reader(open('hotels.csv','r'))
next(csv_file,None)

# print("dd")


if state=="India":

    data = []
    for row in csv_file:
        data.append(row)
    # print(data)

    if cost == 'cost':
        # for min value
        if operation == 'cheapest':
            for i in data:
                p = i[3]
                j = int(p)
            k = []
            k.append(j)
            m = (min(k))

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[3]:
                    code = col[1]
                    st= col[2]
                    print(f"Hotel With cheapest price in  {st} is  {code} with  price  {m}")

        # max value
        elif operation == 'highest':
            for i in data:
                p = i
                j = int(p)
            k = []
            k.append(j)
            m = (max(k))

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[3]:
                    code = col[1]
                    st = col[2]
                    print(f"Hotel With highest price in  {st} is  {code} with  price  {m}")
        # averege

        elif operation == "average":
            for i in data:
                p = i
                j = int(p)
            k = []
            k.append(j)
            m = round(sum(k) / len(k))
            print(m)

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[3]:
                    code = col[1]
                    st = col[2]
                    print(f"Hotel With average price in  {st} is  {code} with  price  {m}")

    # FOR rating..................
    elif cost == "rating":

        # for min value
        if operation == 'cheapest':
            for i in data:
                p = i[4]
                j = float(p)
            k = []
            k.append(j)
            m = (min(k))

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[4]:
                    code = col[1]
                    st = col[2]
                    print(f"Hotel With cheapest price in  {st} is  {code} with  price  {m}")

        # max value
        elif operation == 'highest':
            for i in data:
                p = i[4]
                j = float(p)
            k = []
            k.append(j)
            m = (max(k))
            print(m)

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[4]:
                    code = col[1]
                    st = col[2]
                    print(f"Hotel With highest price in  {st} is  {code} with  price  {m}")
        # averege

        elif operation == "average":
            for i in data:
                p = i[4]
                j = float(p)
            k = []
            k.append(j)
            m = sum(k) / len(k)
            print(m)

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[4]:
                    code = col[1]
                    st = col[2]

                    print(f"Hotel With average price in  {st} is  {code} with  price  {m}")




# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



else:

    print("..............................................................")
    data = []
    for row in csv_file:
        if state == row[2]:
            data.append(row)
    # print(data)

    if cost == 'cost':
        # for min value
        if operation == 'cheapest':
            for i in data:
                p = i[3]
                j = int(p)
            k = []
            k.append(j)
            m = (min(k))

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[3]:
                    code = col[1]
                    print(f"The Hotel in {state} and code is {code} and price is {m}")

        # max value
        elif operation == 'highest':
            for i in data:
                p = i[3]
                j = int(p)
            k = []
            k.append(j)
            m = (max(k))

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[3]:
                    code = col[1]
                    print(f"The Hotel in {state} and code is {code} and price is {m}")
        # averege

        elif operation == "average":
            for i in data:
                p = i[3]
                j = int(p)
            k = []
            k.append(j)
            m = round(sum(k) / len(k))
            print(m)

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[3]:
                    code = col[1]
                    print(f"The Hotel in {state} and code is {code} and price is {m}")

    # FOR rating..................
    elif cost == "rating":

        # for min value
        if operation == 'cheapest':
            for i in data:
                p = i[4]
                j = float(p)
            k = []
            k.append(j)
            m = (min(k))

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[4]:
                    code = col[1]
                    print(f"The Hotel in {state} and code is {code} and price is {m}")

        # max value
        elif operation == 'highest':
            for i in data:
                p = i[4]
                j = float(p)
            k = []
            k.append(j)
            m = (max(k))
            print(m)

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[4]:
                    code = col[1]
                    print(f"The Hotel in {state} and code is {code} and price is {m}")
        # averege

        elif operation == "average":
            for i in data:
                p = i[4]
                j = float(p)
            k = []
            k.append(j)
            m = sum(k) / len(k)
            print(m)

            csv_file = csv.reader(open('hotels.csv', 'r'))

            for col in csv_file:
                if str(m) == col[4]:
                    code = col[1]
                    print(f"The Hotel in {state} and code is {code} and price is {m}")
















