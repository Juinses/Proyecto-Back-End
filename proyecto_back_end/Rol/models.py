from django.db import models

juegos_rol = {
    "RPG tradicional": [
        {"nombre": "Baldur's Gate", "imagen": "baldurs_gate.jpg", "descripcion": "Baldur's Gate 3 es un RPG de fantasía épica de Larian Studios donde los jugadores son infectados con parásitos azotamentes, lo que los lleva a una aventura para buscar la curación mientras navegan un mundo repleto de corrupción, redención y la amenaza de la posesión. El juego se basa en las reglas de la quinta edición de Dungeons & Dragons y ofrece una gran libertad de acción, decisiones que impactan el mundo y la posibilidad de jugar en modo cooperativo. "},
        {"nombre": "Dungeons & Dragons", "imagen": "Dungeons_dragons.jpeg", "descripcion": "Dungeons & Dragons es el juego de rol de mesa más popular del mundo. Es un juego cooperativo de narrativa donde tú y otros jugadores toman el papel de diferentes personajes dentro de una historia. A medida que juegas, tu personaje hará amigos y enemigos, luchará contra monstruos, descubrirá botín y completará misiones."},
        {"nombre": "Wizardry", "imagen": "wizardry.png", "descripcion": "Wizardry es una serie de videojuegos de rol (RPG) clásicos conocidos por su exploración de mazmorras, combate por turnos, creación de personajes y alta dificultad. Los jugadores forman un grupo de aventureros para descender a mazmorras peligrosas, derrotar monstruos y completar misiones, regresando a la ciudad para curarse, comerciar y recibir nuevas misiones. La serie, originada en la era de Apple II, se distingue por su jugabilidad desafiante y la necesidad de optimizar un grupo de personajes de diferentes clases para sobrevivir a las pruebas y a menudo la muerte permanente de los personajes. "},
        {"nombre": "Fallout", "imagen": "fallout.jpg", "descripcion": "En Fallout 1, un habitante del Refugio 13 debe aventurarse al páramo postapocalíptico para encontrar un chip de repuesto para el sistema de agua de su refugio, solo para descubrir una amenaza mayor: un supermutante llamado El Maestro que busca crear una nueva raza dominante. El jugador puede elegir entre la diplomacia o el combate para detener sus planes"},
        {"nombre": "Icewind Dale", "imagen": "icewind_dale.jpg", "descripcion": "Icewind Dale, un videojuego de rol ambientado en la tundra de los Reinos Olvidados, es que un grupo de aventureros es contratado para escoltar una caravana y se ve envuelto en un antiguo complot que amenaza con destruir las Diez Ciudades de Icewind Dale, un conjunto de asentamientos aislados en una región helada. La historia principal gira en torno a un misterioso mal que causa que la noche eterna de la diosa Auril caiga sobre la tierra y provoca que extraños eventos, como el sacrificio humano y la aparición de bestias, afecten a los habitantes. "}
    ],
    "Action RPG": [
        {"nombre": "Dark Souls", "imagen": "dark_souls.jpg", "descripcion": ""},
        {"nombre": "The Witcher 3", "imagen": "action_rpg.jpeg", "descripcion": ""},
        {"nombre": "Bloodborne", "imagen": "bloodborne.jpg", "descripcion": ""},
        {"nombre": "Monster Hunter: World", "imagen": "monster_hunter.jpg", "descripcion": ""},
        {"nombre": "Diablo", "imagen": "diablo.jpg", "descripcion": ""}
    ],
    "Metroidvania": [
        {"nombre": "Metroid", "imagen": "metroid.jpg", "descripcion": ""},
        {"nombre": "Hollow Knight", "imagen": "metroidvania.jpeg", "descripcion": ""},
        {"nombre": "Castlevania: Symphony of the Night", "imagen": "castlevania.jpg", "descripcion": ""},
        {"nombre": "Death's Gambit", "imagen": "deaths_gambit.jpg", "descripcion": ""},
        {"nombre": "Blasphemous", "imagen": "blasphemous.jpg", "descripcion": ""}
    ],
    "JRPG": [
        {"nombre": "Persona 5", "imagen": "persona_5.jpg", "descripcion": ""},
        {"nombre": "Final Fantasy VII", "imagen": "JRPG.jpeg", "descripcion": ""},
        {"nombre": "Dragon Quest XI", "imagen": "dragon_quest_xi.jpg", "descripcion": ""},
        {"nombre": "Xenoblade Chronicles", "imagen": "xenoblade.jpg", "descripcion": ""},
        {"nombre": "Pokemon Negro 2", "imagen": "pokemon_negro_2.jpg", "descripcion": ""}
    ],
    "Roguelike": [
        {"nombre": "The Binding of Isaac", "imagen": "binding_of_isaac.jpg", "descripcion": ""},
        {"nombre": "Hades", "imagen": "rogue_like.jpeg", "descripcion": ""},
        {"nombre": "Dead Cells", "imagen": "dead_cells.jpg", "descripcion": ""},
        {"nombre": "Spelunky", "imagen": "spelunky.jpg", "descripcion": ""},
        {"nombre": "Enter the Gungeon", "imagen": "enter_the_gungeon.jpg", "descripcion": ""}
    ]
}