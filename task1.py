with open("materials_b_import.csv", 'r', encoding="utf-8") as file:
    arr = file.readlines()
    # print(arr)   # список строк из данных каждой строки

    for i in range(1, len(arr)):
        result = []

        data = arr[i].strip()
        # print(data)         #строка из файла
        data_arr = (data.split(";"))
        # print(data_arr)  список из данных одной строки

        last_name = data_arr[0].strip()  # фамилия - первый столбец
        # print(last_name)

        fio = last_name.split()
        if len(fio) > 1:
            data_arr[0] = fio[0]  # фамилия
            data_arr[1] = fio[1]  # имя
            data_arr[2] = fio[2]  # отчество
        last_name = data_arr[0].strip()  # фамилия
        first_name = data_arr[1].strip()  # имя
        sur_name = data_arr[2].strip()  # отчество
        gender = data_arr[3].strip()
        if gender == "женский" or gender == "ж":
            gender = 2
        if gender == "мужской" or gender == "м":
            gender = 1
        phone = data_arr[4].strip().replace("(", "").replace(")", "").replace("-", "")

        #avatar = data_arr[5].strip().split("\\")[1]
        birthday = data_arr[6].strip()
        email = data_arr[7].strip()
        #date_reg = data_arr[8].strip()

        result.append(i)  # result[0]
        result.append(last_name)  # result[1]
        result.append(first_name)  # result[2]
        result.append(sur_name)  # result[3]
        result.append(gender)  # result[4]
        result.append(phone)
        #result.append(avatar)
        result.append(birthday)
        result.append(email)
        #result.append(date_reg)

        print(result)

#with open("materials_b_import.csv", 'r', encoding="utf-8") as f:
    rhh = f.readlines()
    for i in range(1, len(rhh)):
        result1 = []

        data1 = rhh[i].strip()

        data_rhh = (data1.split(";"))

        str = data_rhh[1].split()

        last_name1 = data_rhh[0].strip()

        num_fif = [f"{str + 1}. {first_name}" for str, first_name in enumerate(first_name)]
        result1.append(str[0])
        result1.append(str[1])
        result1.append(data_rhh[2])
        result.append(first_name)
        full_title
        print(result1)
