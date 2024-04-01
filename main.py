from Recepeis import Recepee, RecepeiBook
from RecepeiBookToDownload import DownloadBook

# הקצעת אובייקטים
r = RecepeiBook()
re = Recepee(preperationtime=30, difficullty='hard', isDyatic='false', recepeeName='recepeeName', type='p',
             ingredient1='ingredient1', ingredient2='ingredient2', ingredient3='ingredient3', ingredient4='ingredient4',
             ingredient5='ingredient5')
d = DownloadBook()

print('👋 Welcome to our Recipe webSite 👋')
print('In our website you will able to find vairty of resepies for any time')
ans = 'on'
while ans != 'off':

    print("To show all Recipes press :1")
    print("To show recipe according to difficulty press: 2")
    print('If you want to add recipe press:3')
    print('To get recipe according to requirements press:4')
    print('To downLoad recipe Book press: 5')
    print('to close site enter: off')

    ans = input()

    if ans == '1':
        r.getAllRecepies()
    elif ans == '2':
        dif = input('enter difficulty :easy or hard')
        # using comprehension
        listDiff = [res.recepeeName for res in r.getRecepiesByDifficulty(difficulty=dif)]
        print(listDiff)
    elif ans == '3':
        # using try
        try:
            catgory = input('enter a category')
            if catgory != 'dessrets' and catgory != 'cakesAndCookeis':
                raise Exception
            preperationtime = int(input('press preperationtime'))
            difficullty = input('press difficulty :hard/easy')
            isDyatic = input('enter true/false if its dyatic')
            type = input('enter p if pareve d if dairy or m if meat')
            recepeeName = input('enter a recepeeName')
            ingredient1 = input('enter a  ingredient1')
            ingredient2 = input('enter a  ingredient2')
            ingredient3 = input('enter a  ingredient3')
            ingredient4 = input('enter a  ingredient4')
            ingredient5 = input('enter a  ingredient5')

            r.addRecepei(category=catgory, preperationtime=preperationtime, difficullty=difficullty, isDyatic=isDyatic,
                         type=type,
                         recepeeName=recepeeName, ingredient1=ingredient1,
                         ingredient2=ingredient2,
                         ingredient3=ingredient3,
                         ingredient4=ingredient4, ingredient5=ingredient5)
        except:
            print('no such category!')



    elif ans == '4':
        preperationtime = int(input('press preperationtime'))
        difficullty = input('press diffficulty :hard/easy')
        isDyatic = input('enter true/false if its dyatic')
        type = input('enter p if pareve d if dairy or m if meat')
        listDiff = r.getRecepiesByRequiremets(difficulty=difficullty, type=type, isDyatic=isDyatic,
                                              preperationtime=preperationtime)
        for res in listDiff:
            print(res.recepeeName)
    elif ans == '5':
        name=input('enter a name for the recipe book')
        d.createFileBook(book=r.getAllRecepies1(), respeiBookName=name)
    elif ans == 'off':
        print('Thank you for using our website!!🙏')
    else:
        print('incorrect action😒')


