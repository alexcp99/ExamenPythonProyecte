from pprint import pprint as pp

class Cinema:

    def __init__(self,rows,seats_per_row):
        """
        Args:
            rows: filas de la sala
            seats_per_row: butacas de cada fila    
        """
        self.__rows = rows
        self.__seats_per_row = seats_per_row
        self.__seating = [None] 
        #El seating lo inicializamos como None
    
    def create_cinema_seating(self):
        """
        Inicializa el seating de la sala, que es una lista de diccionarios.
          - Cada elemento de la lista representa una fila de butacas, empezando por la fila 0 que esta en la posicion 0.
          - Cada fila tiene un diccionario para representar las butacas de esa fila.
          - Las claves del diccionario son cada una de las butacas de esa fila (1, 2, 3, etc.).
        """        
        row = { i : None for i in range(1, self.__seats_per_row+1) }        
        for j in range(1, self.__rows+1):
            self.__seating.append(row)
        
    def print_seating(self):
        """
        Imprime el seating de la sala
        """
        pp(self.__seating)

    def book_seat(self,row,seat):
        """
        Marca una butaca como ocupada.
        Args:
            row: la fila de la butaca
            seat: el numero de la butaca
        """
        """Deberia de ser diferente a None, si es diferente a None, quiere decir que esta ocupada
        """
        if self.__seating[row][seat] != None:
            self.__seating[row][seat] = "occupied"

    def count_free_seats(self,rows_seats):
        """
        Calcula la cantidad de butacas libres que hay en una lista
        Args:
            rows_seats: lista de butacas a buscar
            total: valor inicial donde se acumulará el total
        """
        total = 0
        for row, seat in rows_seats:
            if self.__seating[row][seat] == None:
                total=total + 1
        return total

#------------------------------------------- MAIN -----------------------------------------------
cinema = Cinema(rows=10, seats_per_row=8)

#ERROR 1: al reservar una butaca (p.e. fila 2 butaca 4) e imprimir el seating, veo que aparece como ocupada la 4 de cada fila, y no solo de la fila 2.
print("------------- Error 1 -----------------")
cinema.create_cinema_seating()
cinema.book_seat(2,4)
cinema.print_seating()

#ERROR 2: le paso la lista de "seats" donde debería haber 2 libres y me dice que hay 0.
print("\n------------- Error 2 -----------------")
seats = [(2,4), (3,1), (5,2)]

a = cinema.count_free_seats(seats)
print("total: " , a)
     
#El error esta en el total, que la funcion no nos lo devolvia
#por tanto lo he devuelto y lo he definido directament dentro de la funcion
#para en el main llama a = funcion(), donde ese a ja sera el total de butacas libres

        

#ERROR 3: quiero modificar la butaca (2,4) de la lista anterior para que sea la (3,4) y no me deja.
print("\n------------- Error 3 -----------------")
seats[2][4]== 3 #Queremos modificar la 2,4
seat[0] == (3,4)
a = cinema.count_free_seats(seat)
print("total: ", a)
#He añadido en la posicinon 0 de seat el nuevo asiento