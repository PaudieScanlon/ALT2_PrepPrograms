import matplotlib.pyplot as plt

testString = ("Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his \"permanent vacation\" from his responsibilities as Python\'s \"benevolent dictator for life\", a title the Python community bestowed upon him to reflect his long-term commitment as the project\'s chief decision-maker. In January 2019, active Python core developers elected a five-member \"Steering Council\" to lead the project.")

#Read through the code then run it.
#1. Initialise variables for the rest of the vowels to zero.
#2. Add elif statements to count the numbers of the rest of the vowels in the text.
#3. Add the rest of the vowels to the plot at the end of the program.

lenMax = len(testString)
print(lenMax)

a = 0
e = 0
indexCount = 0

while indexCount < lenMax:
	if testString[indexCount] == "a":
    	a = a+1
	elif testString[indexCount] == "e":
    	e = e+1
	indexCount = indexCount+1
   	 
x1 = ["a", "e"]
y1 = [a, e]
plt.bar(x1, y1)
plt.plot()
plt.show()


