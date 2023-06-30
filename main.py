if __name__ == "__main__":
    someArray = [1, "test", True, 1.6, "hey"]
    # get element by index
    print(someArray[4])
    # lenght array
    print(len(someArray))
    # last element array
    print(someArray[-1])
    # add elements to array
    someArray.append(2)
    print(someArray)
    # Remove element
    someArray.pop(1)
    print(someArray)
    someArray.remove('hey')
    print(someArray)
    # find element in array
    targetElement = someArray.index(1.6)
    print(targetElement)
    # replace
    targetElementIndex = someArray.index(1.6)
    someArray[targetElementIndex] = "test3"
    print(someArray)
    # reverse array
    someArray.reverse()
    print(someArray)
    # clear array
    someArray.clear()
    print(len(someArray))