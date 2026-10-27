repeat:bool = True
while repeat:
    print("\nInput exit to stop.")
    test:str = input("Input something (test:string): ")
    print( "Length of input len(test) =", len(test) )
    print("Is the input an empty (test == \"\")?", test == "")
    if test != "":
        print("First character of the input (test[0]) =", test[0])
        print( "Convert the first character to lower case:", test[0].lower() )
        is_alpha:bool = test[0] >= "a" and test[0] <= "z"
        print( "Is the 1st character a lower case alphabetical:", is_alpha )
    #endif
    until:bool = (test == "exit")
    if until == True:
        repeat = False
    #endif
    print("input was", test)
    print("\nString slicing examples:")
    print("index=", end="")
    for index in range(len(test)):
        print(index, end="")
    print("\ntest=\"", end="")
    for index in range(len(test)):
        print(test[index], end="")
    print(f"\"\ntest[1:2]=\"{test[1:2]}\" ,test[2:4]=\"{test[2:4]}\"")
    middle:int = len(test) // 2
    print(f"test[:{middle}]=\"{test[:middle]}\", test[{middle}:]=\"{test[middle:]}\"")
#endwhile
# string[beginning:end]) #<= string slicing from first starting to end character index
# equivalent to pseudocode SUBSTRING/MID( test, beginning, (end-beginning) )
# string slicing is Python treating strings as 1D arrays (sort of)