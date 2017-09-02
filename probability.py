from random import randint
def run():
        flipHeads = 0
        flipTotal = 0
        percentageHeads = 0
        totalOne = 0
        throwTotal = 0
        while True:
            if randint(0, 1) == 1:
                flipHeads = flipHeads + 1
            flipTotal = flipTotal + 1
            percentageHeads = flipHeads / flipTotal * 100
            if percentageHeads == 1/2*100:
                throwTotal = throwTotal + 1
                print('-', flipTotal, flipHeads, throwTotal, percentageHeads, '-')
            if flipTotal % 5000000 == 0:
                print(flipTotal, flipHeads, throwTotal, percentageHeads)
run()
