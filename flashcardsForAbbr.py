import csv
import numpy

if __name__ == '__main__':
    while True:
        with open('abbr.csv', encoding='UTF-8') as f:
            reader = csv.reader(f)
            l = []
            for row in reader:
                if len(row) != 0:
                    l.append(row)
        while True:
            i = numpy.random.randint(0, len(l))
            print(l[i][0].strip())
            answer = input()
            if answer.lower().strip() == 'restart' or answer.lower().strip() == 'reset':
                break
            if answer.lower().strip() == 'end' or answer.lower().strip() == 'finish' or answer.lower().strip() == 'quit' or answer.lower().strip() == 'exit':
                exit()
            if answer.lower().strip() == l[i][1].lower().strip():
                print('  ヾ(*´∀`*)ﾉ 正解！')
                print(l[i][0].strip() + ' : ' +l[i][1].strip())
                print(l[i][2].strip())
                print('')
                del l[i]
            else:
                print('◆◆◆◆◆◆◆◆ (・_・)不正解……◆◆◆◆◆◆◆◆')
                print(l[i][0].strip() + ' : ' +l[i][1].strip())
                print(l[i][2].strip())
                print('')
            
            if len(l) == 0:
                print('  旦_(-ω- ,,)一周しました。')
                print('')
                break
    
        



