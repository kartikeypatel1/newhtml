fruits=["banana","mango","pineapple"]
fruits.remove("banana")#remove is use to remove any given number in list
print(fruits)
more_fruits=["guava","kiwi","grapes"]
fruits.extend(more_fruits)
fruits.pop(2) #pop is use to pop out the element by giving index value
print(fruits)
fruits.pop()#if we did not give any index value then this remove the last element of list
print(fruits)