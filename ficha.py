from colorama import Fore,Style

yo={
    "nombres":{"nombre1":"Angel","nombre2":"De Assis"},
    "apellidos":{"apellido1":"Vega","apellido2":"Vega"},
    "fe_naci":{"dia":9,"mes":12,"año":2006},
    "rut":222293995,
    "nacionalidad":"Chilena",
    "signo":"Sagitario ♐",
    "sexo":"Maculino",
    "animal_fav":"Perros",
    "comida_fav":{"comida1":"lasagna","comida2":"sushi"},
    "mis_mascotas":{"jack":"Perro","bils":"Gato"},
    "deportr_fav":"Futbol",
    "equipo_naci_fav":"U de chile",
    "juego_compu_fav":"Pokemon",
    "pokemon_fav":"Incineroar",
    "color_fav":{"color1":"Azul","color2":"Verde"},
    "juego_pley":"Rocket League",
    "rango_rocket":"Platino 1",
    "Juego_cel":{"juego1":"Efootball","juego2":"Clash of clans"},
    "th_en_clash":"Ayuntamiento 12",
    "valor_en_pes":{"fuerza":3134,"rango_mas_alto":"Division 2"},
    "para_probar":"hola como estas"
}
print(f"""{Fore.BLUE}{Style.BRIGHT}
======================================
    {yo['nombres']['nombre1']} {yo['apellidos']['apellido1']} rut : {yo['rut']}
======================================

Fecha nacimiento : {yo['fe_naci']['dia']} {yo['fe_naci']['mes']} {yo['fe_naci']['año']}
Sexo : {yo['sexo']}
Nacionalidad : {yo['nacionalidad']}
Signo : {yo['signo']}
Animal favorito : {yo['animal_fav']}
Mis mascotas : {yo['mis_mascotas']['jack']} y {yo['mis_mascotas']['bils']}
Comida favorita : {yo['comida_fav']['comida1']} y {yo['comida_fav']['comida2']}
Deporte favorito : {yo['deportr_fav']}
Equipo de futbol favorito : {yo['equipo_naci_fav']}
Juego de computadora favorito : {yo['juego_compu_fav']}
Pokemon favorito : {yo['pokemon_fav']}
Juego de pley favorito : {yo['juego_pley']}
Rango en Rocket League : {yo['rango_rocket']}
Juego de telefono favorito : {yo['Juego_cel']['juego1']} y {yo['Juego_cel']['juego2']}
Ayuntamiento en Clash of clans : {yo['th_en_clash']}
Division en Efootball : {yo['valor_en_pes']['rango_mas_alto']}, Fuerza : {yo['valor_en_pes']['fuerza']}
pa probar : {yo['para_probar']}


{Style.RESET_ALL}""")