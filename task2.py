with open("materials_b_import.csv", 'r', encoding="utf-8") as f:
    rhh = f.readlines()
    main = []
    for i in range(1, len(rhh)):
        result1 = []
        data1 = rhh[i].strip()
        data_rhh = (data1.split(";"))
        title = data_rhh[0].strip()
        result1.append(title)
        last_title = data_rhh[1].strip()
        result1.append(last_title)

        if "\\" in data_rhh[2]:
            img = data_rhh[2].strip().split('\\')[2]
        else:
            img = "NULL"
        result1.append(img)
        money = data_rhh[3].replace("рублей", "").replace("₽", "").replace("руб", "").replace(".00", "")
        result1.append(money)
        hub= data_rhh[4].replace("в наличии", "").replace("На складе", "")
        result1.append(hub)
        hub1= data_rhh[5].strip()
        result1.append(hub1)
        hub2=data_rhh[6].strip()
        result1.append(hub2)
        hub3 = data_rhh[7].strip()
        result1.append(hub3)
        main.append(result1)
    print(main)

