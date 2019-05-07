#Створити консольну програму мовою Python і
#написати клас <Назва_із_завдання> який
#міститиме:
#1. Три додаткових поля, які найкраще
#описують даний клас    
#2. Конструктор (із вказаними дефолтними
#значеннями)
#3. Деструктор
#4. Метод, що повертає стрічкове
#представлення класу
#5. Статичне поле +
#6. Статичний метод, що повертає значення
#статичного поля  
#7. В main() методі визначіть 3 об’єкти типу із
#завдання (з-за допомогою передачі різної
#кількості параметрів) та виведіть
#інформацію про них з-за допомогою методу з
#пункту 4 в консоль

#Створити клас “Парк” котрий містить поля:
#- адреса
#- довжина велосипедних доріжок (в метрах)
#- ціна вхідного квитка
class Park :

    number_of_parks = 0

    def __init__(self ,address = None,length_cycle_tracks_in_meters = 0.0,
                 price_of_entrance_ticket = 0.0, year_foundation = 0, area = 0.0, title = None) :
        self.address = address
        self.length_cycle_tracks_in_meters = length_cycle_tracks_in_meters
        self.price_of_entrance_ticket =  price_of_entrance_ticket
        self.year_foundation = year_foundation
        self.area = area
        self.title = title
        Park.number_of_parks += 1

    def __del__(self):
        Park.number_of_parks -= 1
        print("destructor worked")

    def __str__(self):
        return "Park : " +\
                "\n\t address :\t" + str(self.address) +\
                "\n\t length cycle tracks in meters :\t" + str(self.length_cycle_tracks_in_meters) +\
                "\n\t price of entrance ticket :\t" + str(self.price_of_entrance_ticket) +\
                "\n\t year foundation :\t" + str(self.year_foundation) +\
                "\n\t area :\t" + str(self.area) +\
                "\n\t title :\t" + str(self.title) + "\n"

    @staticmethod
    def get_number_of_parks():
        return Park.number_of_parks

def main():
    first_park = Park("Stusa ", 2500.4, 30.5, 1960, 100.8, "Zalizna voda")
    second_park = Park("V. Velykoho ", 1000, 0.0, 1970, 200)
    second_park.title = "Horihovii hai"
    #third_park = Park("Zelena",15.5,10,1964,150,"Snopkivskii")
    third_park = Park()

    print("Number of parks : " + str(Park.get_number_of_parks()))
    print(first_park)
    print(second_park)
    print(third_park)

main()





