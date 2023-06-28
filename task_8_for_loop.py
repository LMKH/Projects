# the star variable is blank. i did this because the for loop will add a star for each line.
# the for loop adds a star for each itteration/line. Until it goes down to 5 stars
star = ""

for i in range(0, 5):
    star = star + "*"
    print(star)