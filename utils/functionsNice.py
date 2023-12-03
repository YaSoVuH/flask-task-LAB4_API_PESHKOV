def makeMatrix(s):
    ar = s.split(';')
    r = []
    for v in ar:
        vs = v.split(' ')
        ms = []
        for el in vs:
            ms.append(int(el))
        r.append(ms)
    return r

def checkMatrix(M):
    rows = len(M)
    for i in range(0, rows):
        if not (len(M[i])==rows):
            return False
    return 0 < rows < 4

def matrInv(M):
    N = len(M)
    if(N==1):
        return 1/M[0] if M[0] else 'Определитель равен нулю, обратной матрицы не существует'
    
    if(N==2):
        det=(M[0][0]*M[1][1])-(M[1][0]*M[0][1])
        if(det==0):
           return False
        d=1/det
        t = M[0][0]
        M[0][0] = M[1][1]
        M[1][1] = t
        M[0][1] = -M[0][1]
        M[1][0] = -M[1][0]

        for i in range(0,N):
            for j in range(0,N):                
                M[i][j] = M[i][j]*d
        return M
    
    if(N==3):
        det=(M[0][0]*M[1][1]*M[2][2])+(M[0][1]*M[1][2]*M[2][0])+(M[1][0]*M[0][2]*M[2][1])-(M[0][2]*M[1][1]*M[2][0])-(M[0][1]*M[1][0]*M[2][2])-(M[0][0]*M[1][2]*M[2][1]);                
        if(det==0):
            return 'Определитель равен нулю, обратной матрицы не существует'
        d=1/det
                
        for i in range(0,N):
            for j in range(0,N):              
                tmp = M[i][j]
                M[i][j] = M[j][i]
                M[j][i] = tmp

        Dop = [[1, 2, 3],[3, 4, 5],[5, 6, 7]]
        Dop[0][0]= M[1][1]*M[2][2]-M[1][2]*M[2][1]
        Dop[1][0]= -(M[0][1]*M[2][2]-M[0][2]*M[2][1])
        Dop[2][0]= M[0][1]*M[1][2]-M[0][2]*M[1][1]  
        Dop[0][1]= -(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        Dop[1][1]= M[0][0]*M[2][2]-M[0][2]*M[2][0]
        Dop[2][1]= -(M[0][0]*M[1][2]-M[0][2]*M[1][0])
        Dop[0][2]= M[1][0]*M[2][1]-M[1][1]*M[2][0]
        Dop[1][2]= -(M[0][0]*M[2][1]-M[0][1]*M[2][0])
        Dop[2][2]= M[0][0]*M[1][1]-M[0][1]*M[1][0]
        for i in range(0,N):
            for j in range(0,N):                
                Dop[i][j] = round(Dop[i][j]*d*1e3)/1e3
        return Dop

def matrixReverse(data):
    matrix = makeMatrix(data)
    if (checkMatrix(matrix)):
        return matrInv(matrix)
    else:
        return 'Ошибка: допустимы квадратные матрицы порядка 1,2,3'
    

def caesar(s, offset):
    alpha = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    res = []
    for i in s.lower():
        res.append(alpha[(alpha.find(i)+offset+len(alpha))%len(alpha)]) 
    return ''.join(res)

def getSum(string):
    array = string.split(' ')
    sum = 0
    for i in range(len(array)):
            if (isNum(array[i])):
                sum += float(array[i])
            else: return False    
    return sum

def isNum(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
#ADD

def MatrixToList(matrix):
    try:
        ListMatrix = []
        
        matrix = matrix.split('; ', 2)

        for i in range(0, 2):
            matrix[i] = matrix[i].split(' ')

        ListMatrix += matrix

        for i in range(0, 2):
            for j in range(0, 2):
                ListMatrix[i][j] = int(ListMatrix[i][j]) #Elm's Mat From Str To Int

        return ListMatrix
    except:
        return None

def ConvertFrom6to10(string): #Первая задача
    if len(string) == 0:
        return 'Вы не ввели число!'
    
    result = int(string, 6)

    return result

def multiplyMatrixAlgStrasen(M1, M2): #Вторая задача
    Matrix1 = []
    Matrix2 = []

    Matrix1 = MatrixToList(M1)
    Matrix2 = MatrixToList(M2)

    if Matrix1 == None or Matrix2 == None:
        return 'Допущена ошибка при вводе матрицы!'

    if len(Matrix1) != 2 or len(Matrix2) != 2:
        return 'Ошибка. Допустимы матрицы 2 на 2'

    D1 = (Matrix1[0][0] + Matrix1[1][1]) * (Matrix2[0][0] + Matrix2[1][1])
    D2 = (Matrix1[1][0] + Matrix1[1][1]) * Matrix2[0][0]
    D3 = Matrix1[0][0] * (Matrix2[0][0] - Matrix2[0][1])
    D4 = Matrix1[1][1] * (Matrix2[1][1] - Matrix2[0][0])
    D5 = (Matrix1[0][0] + Matrix1[0][1]) * Matrix2[1][1]
    D6 = (Matrix1[1][0] - Matrix1[0][0]) * (Matrix2[0][0] + Matrix2[0][1])
    D7 = (Matrix1[0][1] - Matrix1[1][1]) * (Matrix2[1][0] + Matrix2[1][1])

    ResultMatrix = [[D1 + D4 - D5 + D7, D3 + D5], [D2 + D4, D1 - D2 + D3 + D6]]

    return ResultMatrix

def SkolkoRazBukvVTexte(string, letter): #Третья задача
    string = list(string)

    if len(string) == 0:
        return 'Вы не ввели текст в котором будет осуществляться поиск'

    if len(letter) != 1:
        return 'Вы ввели больше одной или меньше одной буквы для поиска!'

    count = 0

    for i in range(0, len(string)):
        if string[i] == letter:
            count += 1
    
    return count

def DeleteGlasBukv(string): #Четрвёртвя задача
    if len(string) == 0:
        return 'Вы не ввели текст в котором будет осуществляться удаление!'

    res = string
    bukv = 'ауоыиэяюеёАУОЫИЭЯЮЕЁaoeiuyAOEIUY'
    
    for i in bukv:
        res = res.replace(i, '')
    
    return res