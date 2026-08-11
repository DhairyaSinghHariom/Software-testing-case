age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
    
    
#     | TC ID | Test Scenario  | No. | Test Step      | Expected Result         |
# | ----- | -------------- | --: | -------------- | ----------------------- |
# | TC01  | Below boundary |   1 | Enter age `17` | Not eligible for voting |
# | TC02  | Boundary value |   2 | Enter age `18` | Eligible for voting     |
# | TC03  | Above boundary |   3 | Enter age `19` | Eligible for voting     |
