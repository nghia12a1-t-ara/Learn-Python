import logging
logging.basicConfig(filename='D:\\Python\\a.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = %s, total = %s' % (i, total))

    logging.debug('Return value = %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
