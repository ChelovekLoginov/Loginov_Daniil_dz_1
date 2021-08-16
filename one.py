duration = int(input("Введите время в секундах"))
if duration < 60:
    print(str(duration) + "секунд")
elif duration < 3600:
    print(str(duration // 60) + "минут" + str(duration % 60) + "секунд")
elif duration < 24 * 60 * 60:
    print(str(duration // 3600) + "часов" + str(duration % 3600 // 60) + "минут" + str(duration % 60) + "секунд")
else:
    print(str(duration // (24 * 3600)) + "дней" + str(duration % (24 * 3600) // 3600) + "часов" +
          str(duration % (24 * 3600) % 3600 // 60) + "минут" + str(duration % 60) + "секунд")
