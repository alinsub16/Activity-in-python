while True:
    try:
        while True:
            try:
                FirstNoun = input("Enter First Noun:")
                if not FirstNoun.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input!")

        while True:
            try:
                SecondNoun = input("Enter Second Noun:")
                if not SecondNoun.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input!")

        while True:
            try:
                ThirdNoun = input("Enter Third Noun:")
                if not ThirdNoun.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input!")

        while True:
            try:
                FirstVerb = input("Enter First Verb:")
                if not FirstVerb.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input!")

        while True:
            try:
                SecondVerb = input("Enter Second Verb:")
                if not SecondVerb.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input!")

        while True:
            try:
                ThirdVerb = input("Enter Third Verb:")
                if not ThirdVerb.isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input!")

        print("""
___________________ORIGINAL____________________

\tThe Partial Explanation

\tSeems like a long time
\tSince the waiter took my order.
\tGrimy little luncheonette,
\tThe snow falling outside.

\tSeems like it has grown darker
\tSince I last heard the kitchen door
\tBehind my back
\tSince I last noticed
\tAnyone pass on the street.

_______________________________________________
____________________RESULT_____________________

\tThe Partial Explanation

\tSeems like a long time
\tSince the %s took my order.
\t%s little luncheonette,
\tThe %s falling outside.

\tSeems like it has grown %s
\tSince I last %s the kitchen door
\tBehind my back
\tSince I last %s
\tAnyone pass on the street.


\t— charles Simic –      
        """ % (FirstNoun.upper(), SecondNoun.upper(), ThirdNoun.upper(), FirstVerb.upper(), SecondVerb.upper(), ThirdVerb.upper()))
        break
    except ValueError:
        print("Invalid Input!")
