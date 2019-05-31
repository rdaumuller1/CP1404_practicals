
import wikipedia

try:
    search = input("What would you like to search? ")
    while not search == '':
        print(wikipedia.summary(search))
        search = input("What would you like to search? ")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)

