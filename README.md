# Spotify Crawler

## Objetivo
O objetivo da parte 1 do projeto da disciplina ![EXA844](https://sites.google.com/a/ecomp.uefs.br/joao/home/courses/exa844) é selecionar um ou mais usuários e ver todos os artistas/bandas que ele(s) escutam cotidianamente.
É inserido o UID do usuário que se deseja obter artistas ouvidos através de suas playlists públicas. As playlists são processadas, seleciona-se as 100 primeiras músicas, 
filtra-se os artistas para que exista apenas 1 ocorrência de cada. Com os UIDs dos artistas, a página dele no Spotify é acessada, raspada e tem os dados estruturados.
Com os dados dos artistas já estruturados, é criado um JSON respectivo contendo nome, id único, url, álbuns e singles. Posterioremente será disponibilizado uma API REST
para acesso desses dados.

## Links
Os links a serem buscados são a página principal de um usuário qualquer do Spotify ou somente seu UID respectivo.
Exemplos:
- ![Ian Zaque](https://open.spotify.com/user/2124wohtd26bam7kcuvhvwgii)
- ![2124wohtd26bam7kcuvhvwgii](https://open.spotify.com/user/2124wohtd26bam7kcuvhvwgii)

## Esquema
Os dados serão estruturados em JSONs da seguinte ![forma](https://github.com/ian-zaque/exa844-projeto/blob/main/esquema.json):

```json
{
    "name": "",
    "albums": [
        {
            "name": "",
            "img": "",
            "year": 2021,
            "type": ""
        },
        {
            "name": "",
            "img": "",
            "year": 2017,
            "type": ""
        }
    ],
    "singles": [
        {
            "name": "",
            "img": "",
            "year": 2020,
            "type": "Single"
        }
    ],
    "similarArtists": [
        {
            "name": ""
        }
    ],
    "URL": "",
    "UID": ""
}
```


## Exemplo Real
O aquivo ![Avenged Sevenfold.json]() é um exemplo real de um artista que foi buscado e estruturado.

```json
{
    "name": "Avenged Sevenfold",
    "albums": [
        {
            "name": "Live in the LBC",
            "img": "https://i.scdn.co/image/ab67616d00001e0214e46988b8b3ed36de9b7f92",
            "year": "2020",
            "type": "Album"
        },
        {
            "name": "Diamonds in the Rough",
            "img": "https://i.scdn.co/image/ab67616d00001e0251a4c25f865262b2a03c7b90",
            "year": "2020",
            "type": "Album"
        },
        {
            "name": "The Stage (Deluxe Edition)",
            "img": "https://i.scdn.co/image/ab67616d00001e024843e0f824a00334e811279c",
            "year": "2017",
            "type": "Album"
        },
        {
            "name": "The Stage",
            "img": "https://i.scdn.co/image/ab67616d00001e02cbe3f1cd68d2ed2fec96b740",
            "year": "2016",
            "type": "Album"
        },
        {
            "name": "Hail to the King: Deathbat (Original Video Game Soundtrack)",
            "img": "https://i.scdn.co/image/ab67616d00001e02bb3b10ab9c78f1614a207298",
            "year": "2015",
            "type": "Album"
        },
        {
            "name": "Waking The Fallen: Resurrected",
            "img": "https://i.scdn.co/image/ab67616d00001e0227a248cf7b07baa9f643cafa",
            "year": "2014",
            "type": "Album"
        },
        {
            "name": "Hail to the King",
            "img": "https://i.scdn.co/image/ab67616d00001e020ea1ecb2d5271c2db402b0c2",
            "year": "2013",
            "type": "Album"
        },
        {
            "name": "Nightmare",
            "img": "https://i.scdn.co/image/ab67616d00001e02c34064a3c5e4a25892a091f3",
            "year": "2010",
            "type": "Album"
        }
    ],
    "singles": [
        {
            "name": "Nobody",
            "img": "https://i.scdn.co/image/ab67616d00001e022054ff11f6205e072c9b2ded",
            "year": "2023",
            "type": "Single"
        },
        {
            "name": "Set Me Free",
            "img": "https://i.scdn.co/image/ab67616d00001e02f8ff4fc228b1925ea53d8b85",
            "year": "2020",
            "type": "Single"
        },
        {
            "name": "Black Reign",
            "img": "https://i.scdn.co/image/ab67616d00001e027d1513d5e7f6bb88de6cdcd9",
            "year": "2018",
            "type": "EP"
        },
        {
            "name": "Mad Hatter",
            "img": "https://i.scdn.co/image/ab67616d00001e02c13e88f01a72ca6080656847",
            "year": "2018",
            "type": "Single"
        },
        {
            "name": "Live At The GRAMMY Museum\u00ae",
            "img": "https://i.scdn.co/image/ab67616d00001e0235a175c1a44ede1f48d390db",
            "year": "2017",
            "type": "Single"
        },
        {
            "name": "Eternal Rest (Live From Ventura Theater - January 2004)",
            "img": "https://i.scdn.co/image/ab67616d00001e02582a30ef12716bba22968904",
            "year": "2012",
            "type": "Single"
        },
        {
            "name": "Carry On",
            "img": "https://i.scdn.co/image/ab67616d00001e024799eecf1843c6d9742bc023",
            "year": "2012",
            "type": "Single"
        },
        {
            "name": "Not Ready to Die (From \"Call of the Dead\")",
            "img": "https://i.scdn.co/image/ab67616d00001e0294695e0e42ce2be29d783573",
            "year": "2011",
            "type": "Single"
        }
    ],
    "similarArtists": [
        {
            "name": "Bullet For My Valentine"
        },
        {
            "name": "Atreyu"
        },
        {
            "name": "Trivium"
        },
        {
            "name": "All That Remains"
        },
        {
            "name": "Stone Sour"
        },
        {
            "name": "Black Tide"
        },
        {
            "name": "Killswitch Engage"
        },
        {
            "name": "Escape the Fate"
        }
    ],
    "URL": "https://open.spotify.com/artist/0nmQIMXWTXfhgOBdNzhGOs",
    "UID": "0nmQIMXWTXfhgOBdNzhGOs"
}





