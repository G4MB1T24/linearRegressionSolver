import matplotlib.pyplot as plt


def isEmpty(arr):
    if len(arr) == 0:
        print("Parameters cant be 0 sized")
        exit()
    else:
        return


def mean(array):
    isEmpty(array)
    mean = 0
    for i in range(len(array)):
        mean += array[i]
    return mean / len(array)


def slope(mX, mY, arrayX, arrayY):
    isEmpty(arrayX)
    deviation = 0
    sumofDeviationXsquared = 0
    for i in range(len(arrayX)):
        deviation = deviation + (arrayX[i] - mX) * (arrayY[i] - mY)
        sumofDeviationXsquared = sumofDeviationXsquared + (arrayX[i] - mX) ** 2
        if sumofDeviationXsquared != 0 and deviation != 0:
            return deviation / sumofDeviationXsquared
        else:
            print("Provide atleast 2 or more values")
            exit()


def intercept(meanX, meanY, slope):
    return meanY - (slope * meanX)


def append_elements_to_lists(X, Y):
    # Append elements to list X
    print("Enter elements for list X (separated by space):")
    X.extend(map(int, input().split()))

    # Append elements to list Y
    print("Enter elements for list Y (separated by space):")
    Y.extend(map(int, input().split()))


X = []
Y = []

append_elements_to_lists(X, Y)
if len(X) == len(Y):

    meanX = mean(X)
    meanY = mean(Y)

    inter = intercept(meanX, meanY, slope(meanX, meanY, X, Y))
else:
    print("Parameterr size of X and Y aint equal")
    exit()
