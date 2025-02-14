#
import decisions


def main():
    result = decisions.get_options_ratio(5, 20)
    
    print (result)

    if (result):
        print('Unacceptable')


main()
   