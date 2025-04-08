
def Madlibs():
  name = str(input("Enter Your Name:  "))
  city = str(input("Enter Your City:  "))
  institute = str(input("Enter Your Institute:  "))
  teacher = str(input("Enter Your Teacher Name:  "))
  adjective = str(input("Enter Adjective ..:  "))

  story = f"""My name is {name}, I live in {city},
  I have been a part of {institute},
  I have been taking classes by {teacher}
  and he is very {adjective}."""
  print(story)
Madlibs()