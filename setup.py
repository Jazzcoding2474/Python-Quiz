Name23 = str(input("Enter in your name:"))
print("\n" + Name23 +" I want you to answer my quiz.")
print("Answer only by (a. or b. or c. or d.) It's case sensitive!")
print("\n Is \\n used just like the Enter key on a keyboard? Hint: Look at the code")
print("a. Yes   b. No ")
ans1 = input("Enter your answer here:")

if ans1 == "a.":
 print("Correct")
 print("\n Which is the hardest programming language out of the four? Hint: The english pronunciation rhymes with dwell ")
 print("a. SQL   b. Python")
 print("c. HTML  d. Javascript")
 ans2 = input("\nEnter your answer:")

 if ans2 == "a.":
     print("Correct, SQL is pronounced SEQUEL")
 elif ans2 == "b.":
     print("Wrong, SQL is the right answer because SQL is pronounced SEQUEL ")
 elif ans2 == "c.":
     print("Wrong, SQL is the right answer because SQL is pronounced SEQUEL ")
 elif ans2 == "d.":
     print("Wrong, SQL is the right answer because SQL is pronounced SEQUEL ")
 else:
     print("Invalid input try again")

elif ans1 == "b.":
 print("Wrong, the right answer was Yes")
 print("\n Which is the hardest programming language out of the four? Hint: The english pronunciation rhymes with dwell ")
 print("a. SQL   b. Python")
 print("c. HTML  d. Javascript")
 ans2 = input("\nEnter your answer:")

 if ans2 == "a.":
     print("Correct, SQL is pronounced SEQUEL")
 elif ans2 == "b.":
     print("Wrong, SQL is the right answer because SQL is pronounced SEQUEL ")
 elif ans2 == "c.":
     print("Wrong, SQL is the right answer because SQL is pronounced SEQUEL ")
 elif ans2 == "d.":
     print("Wrong, SQL is the right answer because SQL is pronounced SEQUEL ")
 else:
     print("Invalid input try again")
else:
    print("Invalid input try again.")
