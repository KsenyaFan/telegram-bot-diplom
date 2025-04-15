## Телеграмм-бот Кинопоиск @MyNewFan_bot

1. #### Описание проекта
Телеграмм-бот создан для поиска фильмов. Он позволяет
пользователям находить информацию о фильмах
и сериалах по названию, рейтингу,
а также имеет возможность предоставлять информацию о 
любимых актерах, режисерах.

2. #### Как пользоваться

Откройте телеграмм. В поиске введите название
бота **@MyNewFan_bot**.

3. #### custom command:

   **`/movie_search`** — поиск фильма/сериала по названию.
При вызове данной команды бот отправляет
сообщение пользователю:
*Введите название фильма для поиска:*

После чего пользователь вводит название интересующего
его фильма с клавиатуры.
*(Например, Матрица)*

С помощью функции *search_movie*
отправляется запрос API:

https://api.kinopoisk.dev/v1.3/movie?name=Матрица&limit=5

Ответ API:
```json
{
    "docs": [
        {
            "externalId": {
                "imdb": "tt0133093",
                "tmdb": 603,
                "kpHD": "4824a95e60a7db7e86f14137516ba590"
            },
            "rating": {
                "kp": 8.498,
                "imdb": 8.7,
                "filmCritics": 7.7,
                "russianFilmCritics": 60,
                "await": null
            },
            "votes": {
                "kp": 755888,
                "imdb": 2131790,
                "filmCritics": 210,
                "russianFilmCritics": 5,
                "await": 0
            },
            "movieLength": 136,
            "id": 301,
            "type": "movie",
            "name": "Матрица",
            "description": "Жизнь Томаса Андерсона разделена на две части: днём он — самый обычный офисный работник, получающий нагоняи от начальства, а ночью превращается в хакера по имени Нео, и нет места в сети, куда он бы не смог проникнуть. Но однажды всё меняется. Томас узнаёт ужасающую правду о реальности.",
            "year": 1999,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/4774061/cf1970bc-3f08-4e0e-a095-2fb57c3aa7c6/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/4774061/cf1970bc-3f08-4e0e-a095-2fb57c3aa7c6/x1000"
            },
            "genres": [
                {
                    "name": "фантастика"
                },
                {
                    "name": "боевик"
                }
            ],
            "countries": [
                {
                    "name": "США"
                },
                {
                    "name": "Австралия"
                }
            ],
            "alternativeName": "The Matrix",
            "enName": null,
            "names": [
                {
                    "name": "Матрица"
                },
                {
                    "name": "The Matrix"
                },
                {
                    "name": "เพาะพันธุ์มนุษย์เหนือโลก",
                    "language": "TH",
                    "type": null
                },
                {
                    "name": "黑客帝国1",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "Μάτριξ",
                    "language": "GR",
                    "type": null
                },
                {
                    "name": "黑客帝国1：骇客任务",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "매트릭스",
                    "language": "KR",
                    "type": null
                },
                {
                    "name": "Matrix 1",
                    "language": "DE",
                    "type": null
                },
                {
                    "name": "マトリックス：1999",
                    "language": "JP",
                    "type": null
                },
                {
                    "name": "廿二世紀殺人網絡",
                    "language": "HK",
                    "type": null
                },
                {
                    "name": "廿二世紀殺人網絡",
                    "language": "TW",
                    "type": null
                },
                {
                    "name": "Matrix",
                    "language": "ES",
                    "type": "Castilian Spanish"
                }
            ],
            "shortDescription": "Хакер Нео узнает, что его мир — виртуальный. Выдающийся экшен, доказавший, что зрелищное кино может быть умным",
            "logo": {
                "url": "https://imagetmdb.com/t/p/original/a9ATitiXhAZU5FQeF63Nb19hYfQ.png"
            },
            "watchability": {
                "items": []
            }
        },
        {
            "externalId": {
                "imdb": "tt0234215",
                "tmdb": 604,
                "kpHD": "4fb1b6ac7e089865a4f80f5aace6bc27"
            },
            "rating": {
                "kp": 7.74,
                "imdb": 7.2,
                "filmCritics": 6.8,
                "russianFilmCritics": 77.7778,
                "await": null
            },
            "votes": {
                "kp": 279355,
                "imdb": 647425,
                "filmCritics": 239,
                "russianFilmCritics": 9,
                "await": 0
            },
            "movieLength": 138,
            "id": 299,
            "type": "movie",
            "name": "Матрица: Перезагрузка",
            "description": "Борцы за свободу Нео, Тринити и Морфеус продолжают руководить восстанием людей против армии машин. Они вынуждены использовать не только арсенал превосходного оружия, но и свои выдающиеся навыки. Участие в миссии по спасению человеческой расы от истребления приносит им более глубокое понимание Матрицы и осознание центральной роли Нео в судьбе человечества.",
            "year": 2003,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/4774061/a53d1c75-4d1a-4c86-a936-65b2a724345c/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/4774061/a53d1c75-4d1a-4c86-a936-65b2a724345c/x1000"
            },
            "genres": [
                {
                    "name": "фантастика"
                },
                {
                    "name": "боевик"
                }
            ],
            "countries": [
                {
                    "name": "США"
                }
            ],
            "alternativeName": "The Matrix Reloaded",
            "enName": null,
            "names": [
                {
                    "name": "Матрица: Перезагрузка"
                },
                {
                    "name": "The Matrix Reloaded"
                },
                {
                    "name": "The Matrix 2",
                    "language": "US",
                    "type": "working title"
                },
                {
                    "name": "The Matrix Reloaded: The IMAX Experience",
                    "language": "US",
                    "type": "MAX version promotional title"
                },
                {
                    "name": "Matrix II Reloaded",
                    "language": "ES",
                    "type": null
                },
                {
                    "name": "Matrix 2 - Reloaded",
                    "language": "FR",
                    "type": null
                },
                {
                    "name": "Matrix Recargado",
                    "language": "MX",
                    "type": null
                },
                {
                    "name": "The Matrix 2：Reloaded",
                    "language": "US",
                    "type": null
                },
                {
                    "name": "黑客帝国2",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "Matrix 2",
                    "language": "US",
                    "type": null
                },
                {
                    "name": "Matrix 2 - Reloaded",
                    "language": "IT",
                    "type": null
                },
                {
                    "name": "Matrix II - Reloaded",
                    "language": "IT",
                    "type": null
                },
                {
                    "name": "Μάτριξ 2",
                    "language": "GR",
                    "type": null
                },
                {
                    "name": "Matrix Reloaded",
                    "language": "BR",
                    "type": null
                },
                {
                    "name": "매트릭스 2: 리로디드",
                    "language": "KR",
                    "type": null
                },
                {
                    "name": "Matrix 2",
                    "language": "CA",
                    "type": null
                },
                {
                    "name": "Matrix 2 - Reloaded",
                    "language": "CA",
                    "type": null
                },
                {
                    "name": "The Matrix II: Reloaded",
                    "language": "US",
                    "type": null
                },
                {
                    "name": "Matrix 2 - Reloaded",
                    "language": "DE",
                    "type": null
                }
            ],
            "shortDescription": "Нео против бесчисленных копий агента Смита. Вторая часть знаковой трилогии с Киану Ривзом",
            "logo": {
                "url": "https://avatars.mds.yandex.net/get-ott/1652588/2a00000170ed41c7e28d1dcfcb8f8cb7e8a3/orig"
            },
            "watchability": {
                "items": []
            }
        },
        {
            "externalId": {
                "imdb": "tt0242653",
                "tmdb": 605,
                "kpHD": "447facd44e4281f2bb27e87bf573de0e"
            },
            "rating": {
                "kp": 7.63,
                "imdb": 6.7,
                "filmCritics": 5.3,
                "russianFilmCritics": 20,
                "await": null
            },
            "votes": {
                "kp": 241795,
                "imdb": 557517,
                "filmCritics": 215,
                "russianFilmCritics": 5,
                "await": 0
            },
            "movieLength": 129,
            "id": 316,
            "type": "movie",
            "name": "Матрица: Революция",
            "description": "Пока армия машин пытается уничтожить Зион, его жители из последних сил держат оборону.",
            "year": 2003,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/1900788/37fc55e7-dfc7-406f-a187-17ef49f65b6f/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1900788/37fc55e7-dfc7-406f-a187-17ef49f65b6f/x1000"
            },
            "genres": [
                {
                    "name": "фантастика"
                },
                {
                    "name": "боевик"
                }
            ],
            "countries": [
                {
                    "name": "США"
                },
                {
                    "name": "Австралия"
                }
            ],
            "alternativeName": "The Matrix Revolutions",
            "enName": null,
            "names": [
                {
                    "name": "Матрица: Революция"
                },
                {
                    "name": "The Matrix Revolutions"
                },
                {
                    "name": "The Matrix 3",
                    "language": "US",
                    "type": "working title"
                },
                {
                    "name": "The Matrix Revolutions: The IMAX Experience",
                    "language": "US",
                    "type": "IMAX version promotional title"
                },
                {
                    "name": "Matrix 3 - Revolutions",
                    "language": "FR",
                    "type": null
                },
                {
                    "name": "Matrix III Revolutions",
                    "language": "ES",
                    "type": null
                },
                {
                    "name": "The Matrix 3 - Revolutions",
                    "language": "US",
                    "type": null
                },
                {
                    "name": "黑客帝国3",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "Matrix 3",
                    "language": "US",
                    "type": null
                },
                {
                    "name": "Matrix 3 - Revolutions",
                    "language": "IT",
                    "type": null
                },
                {
                    "name": "Matrix III - Revolutions",
                    "language": "IT",
                    "type": null
                },
                {
                    "name": "Μάτριξ 3",
                    "language": "GR",
                    "type": null
                },
                {
                    "name": "매트릭스 3: 레볼루션",
                    "language": "KR",
                    "type": null
                },
                {
                    "name": "Matrix Revolutions",
                    "language": "DE",
                    "type": null
                },
                {
                    "name": "Matrix 3",
                    "language": "CA",
                    "type": null
                },
                {
                    "name": "Matrix 3 - Revolutions",
                    "language": "CA",
                    "type": null
                },
                {
                    "name": "The Matrix III: Revolutions",
                    "language": "US",
                    "type": null
                },
                {
                    "name": "Matrix 3 - Revolutions",
                    "language": "DE",
                    "type": null
                }
            ],
            "shortDescription": "Для Нео пришло время исполнить пророчество и дать бой Матрице. Финал трилогии с эпической битвой людей и машин",
            "logo": {
                "url": "https://avatars.mds.yandex.net/get-ott/236744/2a00000170ed42c2c265608715044eff6b26/orig"
            },
            "watchability": {
                "items": []
            }
        },
        {
            "id": 1294123,
            "type": "movie",
            "externalId": {
                "kpHD": "451328a462e0e301ac1c040ab63b43ed",
                "imdb": "tt10838180",
                "tmdb": 624860
            },
            "name": "Матрица: Воскрешение",
            "rating": {
                "kp": 5.716,
                "imdb": 5.6,
                "filmCritics": 6.2,
                "russianFilmCritics": 76.9231,
                "await": null
            },
            "description": "Геймдизайнер Томас Андерсон сделал себе имя работой над трилогией игр «Матрица». Хотя окружающий мир периодически даёт сбои и обнажает свою истинную сущность, бывший Нео исправно посещает психотерапевта, принимает пилюли и практически убедил себя, что всё это — игра его воображения. Но однажды на него выходит хакерша Багз и предлагает снова следовать за белым кроликом.",
            "votes": {
                "kp": 187390,
                "imdb": 291308,
                "filmCritics": 359,
                "russianFilmCritics": 13,
                "await": 0
            },
            "year": 2021,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/1898899/f71f55b2-0a74-4a9e-b9a2-7369eccbb3a3/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1898899/f71f55b2-0a74-4a9e-b9a2-7369eccbb3a3/x1000"
            },
            "genres": [
                {
                    "name": "фантастика"
                },
                {
                    "name": "боевик"
                }
            ],
            "countries": [
                {
                    "name": "США"
                },
                {
                    "name": "Австралия"
                }
            ],
            "alternativeName": "The Matrix Resurrections",
            "enName": null,
            "movieLength": 148,
            "names": [
                {
                    "name": "Матрица: Воскрешение"
                },
                {
                    "name": "The Matrix Resurrections"
                },
                {
                    "name": "骇客任务4",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "骇客帝国4",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "The Matrix 4",
                    "language": "US",
                    "type": "working title"
                },
                {
                    "name": "Матриця 4",
                    "language": "UA",
                    "type": null
                },
                {
                    "name": "매트릭스: 리저렉션",
                    "language": "KR",
                    "type": null
                },
                {
                    "name": "Matrix 4",
                    "language": "BR",
                    "type": null
                },
                {
                    "name": "Матрицата: Възкресения",
                    "language": "BG",
                    "type": null
                },
                {
                    "name": "駭客任務：復活",
                    "language": "TW",
                    "type": null
                },
                {
                    "name": "The Matrix 4 Resurrections",
                    "language": "US",
                    "type": "alternative title"
                },
                {
                    "name": "黑客帝国4：矩阵重启",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "Mátrix - Feltámadások",
                    "language": "HU",
                    "type": null
                },
                {
                    "name": "22 世紀殺人網絡 復活次元",
                    "language": "HK",
                    "type": null
                },
                {
                    "name": "Matrix: Ανάσταση",
                    "language": "GR",
                    "type": null
                },
                {
                    "name": "Matrix 4 - Resurrections",
                    "language": "FR",
                    "type": null
                },
                {
                    "name": "Matrix 4 - Resurrections",
                    "language": "DE",
                    "type": null
                },
                {
                    "name": "Matrikss: Atdzimšana",
                    "language": "LV",
                    "type": null
                },
                {
                    "name": "The Matrix IV: Resurrections",
                    "language": "US",
                    "type": "Alternative Title"
                },
                {
                    "name": "Project Ice Cream",
                    "language": "US",
                    "type": "Working Title"
                },
                {
                    "name": "マトリックス レザレクションズ：2021",
                    "language": "JP",
                    "type": null
                },
                {
                    "name": "Matrix: ülestõusmine",
                    "language": "EE",
                    "type": null
                },
                {
                    "name": "Matrix Resurrections",
                    "language": "ES",
                    "type": null
                },
                {
                    "name": "22世紀殺人網絡 復活次元",
                    "language": "HK",
                    "type": null
                },
                {
                    "name": "22世紀殺人網絡4 復活次元",
                    "language": "HK",
                    "type": null
                },
                {
                    "name": "La Matrice Résurrections",
                    "language": "CA",
                    "type": "Québec"
                },
                {
                    "name": "黑客帝国4",
                    "language": "CN",
                    "type": null
                }
            ],
            "shortDescription": "Нео должен вернуться в Матрицу, чтобы спасти Тринити. Любимые герои и меташутки в продолжении революционного боевика",
            "logo": {
                "url": "https://image.openmoviedb.com/tmdb-images/original/gtqZvzLLGZX3yGoEbEpm9DUdo9U.png",
                "previewUrl": "https://image.openmoviedb.com/tmdb-images/w500/gtqZvzLLGZX3yGoEbEpm9DUdo9U.png"
            },
            "watchability": {
                "items": []
            }
        },
        {
            "id": 556944,
            "externalId": {
                "kpHD": "443e1241a458e34da8a66df77e8fc44b"
            },
            "name": "Матрица времени",
            "alternativeName": "Before I Fall",
            "enName": null,
            "names": [
                {
                    "name": "Матрица времени",
                    "language": "RU",
                    "type": "Russian title on kinopoisk"
                },
                {
                    "name": "Before I Fall",
                    "language": null,
                    "type": "Original title on kinopoisk"
                }
            ],
            "type": "movie",
            "year": 2016,
            "description": "Саманта - крутая девчонка, которой всегда и во всем везло. Но в тот день, в пятницу, 12 февраля, что-то пошло не так, а потом та авария на трассе… Саманта оказалась в заколдованном круге проклятого дня, и теперь она вынуждена проживать ужас той пятницы снова и снова. Чтобы распутать петлю времени, она должна вычислить ошибку и исправить неверный шаг. Но каждый раз что-то не срабатывает…",
            "shortDescription": "Саманта погибает и попадает в петлю времени, которую нужно прервать. Молодежная версия «Дня сурка» с Зои Дойч",
            "rating": {
                "kp": 6.462,
                "imdb": 6.4,
                "filmCritics": 5.8,
                "russianFilmCritics": 50,
                "await": null
            },
            "votes": {
                "kp": 113813,
                "imdb": 58301,
                "filmCritics": 122,
                "russianFilmCritics": 4,
                "await": 0
            },
            "movieLength": 99,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/1600647/3961248c-8fcc-4d10-ac97-a9b14b6e7a50/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1600647/3961248c-8fcc-4d10-ac97-a9b14b6e7a50/x1000"
            },
            "genres": [
                {
                    "name": "триллер"
                },
                {
                    "name": "драма"
                },
                {
                    "name": "детектив"
                }
            ],
            "countries": [
                {
                    "name": "США"
                }
            ],
            "watchability": {
                "items": [
                    {
                        "name": "Okko",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/239697/7713e586-17d1-42d1-ac62-53e9ef1e70c3/orig"
                        },
                        "url": "https://okko.tv/movie/before-i-fall?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed"
                    },
                    {
                        "name": "PREMIER",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/239697/0f86e907-9531-47e9-87bd-5101a08d4e30/orig"
                        },
                        "url": "https://premier.one/show/9461?utm_source=yandex&utm_medium=yandex_feed_search&utm_campaign=yandex_feed"
                    },
                    {
                        "name": "Триколор Кино и ТВ",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/239697/947e777c-2f73-4cbc-b09d-6bfa3966ba13/orig"
                        },
                        "url": "https://kino.tricolor.tv/watch/matritsa-vremeni-2017/"
                    },
                    {
                        "name": "Wink",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/1672343/54096cbe-cc3b-41c9-8e44-990ebbca8d61/orig"
                        },
                        "url": "https://wink.ru/media_items/54870173?utm_source=yandex&utm_medium=koldunschick&utm_content=name"
                    },
                    {
                        "name": "viju",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/224348/8b10c84b-e1bb-4493-9bc4-6ee56554403a/orig"
                        },
                        "url": "https://viju.ru/filmy/matritsa-vremeni?utm_campaign=yandex_content_integration&utm_medium=affiliate&utm_source=yandex"
                    },
                    {
                        "name": "24ТВ",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/2439731/85e83b8d-1159-4781-bad5-ce0a809b3843/orig"
                        },
                        "url": "https://24h.tv/contents/2017-before-i-fall-546386729444049137"
                    },
                    {
                        "name": "Смотрёшка",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/236744/c88e652e-2eb1-472d-b636-a266364dbf58/orig"
                        },
                        "url": "https://smotreshka.tv/archive/5b679fefb2de77e74824e63d?utm_source=yandex_search&utm_campaign=yandex_feed&utm_term=archive&utm_content=archive"
                    }
                ]
            }
        }
    ],
    "total": 32,
    "limit": 5,
    "page": 1,
    "pages": 7
}
```
Далее, приходит в ответ несколько вариантов фильмов,
в виде инлайн-кнопок, где указано
название фильма и год выпуска. В данном запросе установлен
лимит - 5 фильмов с похожим названием.

Ответ бота:

Выбери фильм:
Кнопка 1 - Матрица (1999)
Кнопка 2 - Матрица: Перезагрузка (2003)
Кнопка 3 - Матрица: Революция (2003)
Кнопка 4 - Матрица: Воскрешение (2021)
Кнопка 5 - Матрица времени(2016)


Пользователю предоставляется выбор
интересующего фильма. Пользователь выбирает
фильм *(например, Матрица (1999))*

С помощью функции *get_movies_by_id*, в которую
передается id нужного фильма, отправляется повторный
запрос API уже по id:

https://api.kinopoisk.dev/v1.3/movie?id=301&limit=1

Ответ API:
```json
{
    "docs": [
        {
            "externalId": {
                "imdb": "tt0133093",
                "tmdb": 603,
                "kpHD": "4824a95e60a7db7e86f14137516ba590"
            },
            "rating": {
                "kp": 8.498,
                "imdb": 8.7,
                "filmCritics": 7.7,
                "russianFilmCritics": 60,
                "await": null
            },
            "votes": {
                "kp": 755888,
                "imdb": 2131790,
                "filmCritics": 210,
                "russianFilmCritics": 5,
                "await": 0
            },
            "movieLength": 136,
            "id": 301,
            "type": "movie",
            "name": "Матрица",
            "description": "Жизнь Томаса Андерсона разделена на две части: днём он — самый обычный офисный работник, получающий нагоняи от начальства, а ночью превращается в хакера по имени Нео, и нет места в сети, куда он бы не смог проникнуть. Но однажды всё меняется. Томас узнаёт ужасающую правду о реальности.",
            "year": 1999,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/4774061/cf1970bc-3f08-4e0e-a095-2fb57c3aa7c6/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/4774061/cf1970bc-3f08-4e0e-a095-2fb57c3aa7c6/x1000"
            },
            "genres": [
                {
                    "name": "фантастика"
                },
                {
                    "name": "боевик"
                }
            ],
            "countries": [
                {
                    "name": "США"
                },
                {
                    "name": "Австралия"
                }
            ],
            "alternativeName": "The Matrix",
            "enName": null,
            "names": [
                {
                    "name": "Матрица"
                },
                {
                    "name": "The Matrix"
                },
                {
                    "name": "เพาะพันธุ์มนุษย์เหนือโลก",
                    "language": "TH",
                    "type": null
                },
                {
                    "name": "黑客帝国1",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "Μάτριξ",
                    "language": "GR",
                    "type": null
                },
                {
                    "name": "黑客帝国1：骇客任务",
                    "language": "CN",
                    "type": null
                },
                {
                    "name": "매트릭스",
                    "language": "KR",
                    "type": null
                },
                {
                    "name": "Matrix 1",
                    "language": "DE",
                    "type": null
                },
                {
                    "name": "マトリックス：1999",
                    "language": "JP",
                    "type": null
                },
                {
                    "name": "廿二世紀殺人網絡",
                    "language": "HK",
                    "type": null
                },
                {
                    "name": "廿二世紀殺人網絡",
                    "language": "TW",
                    "type": null
                },
                {
                    "name": "Matrix",
                    "language": "ES",
                    "type": "Castilian Spanish"
                }
            ],
            "shortDescription": "Хакер Нео узнает, что его мир — виртуальный. Выдающийся экшен, доказавший, что зрелищное кино может быть умным",
            "logo": {
                "url": "https://imagetmdb.com/t/p/original/a9ATitiXhAZU5FQeF63Nb19hYfQ.png"
            },
            "watchability": {
                "items": []
            }
        }
    ],
    "total": 1,
    "limit": 1,
    "page": 1,
    "pages": 1
}
```

В ответ ему приходит сообщение, где 
изображен постер фильма, наименование, год,
рейтинг, страна производитель, жанр и описание.

Ответ бота:

**Фото**
*Матрица (1999)*
*Рейтинг: 8.498*
*Страна: США, Австралия*
*Жанр: фантастика, боевик*

*Описание:Жизнь Томаса Андерсона разделена на две 
части: днём он — самый обычный офисный работник,
получающий нагоняи от начальства, а ночью
превращается в хакера по имени Нео, и нет места в
сети, куда он бы не смог проникнуть. Но однажды всё
меняется. Томас узнаёт ужасающую правду о реальности.*

После чего фильм автоматически добавлен в историю поиска.

   **`/movies_rating`** — поиск фильмов/сериалов по рейтингу.

При вызове данной команды бот отправляет
сообщение пользователю:
*Введите рейтинг для поиска фильмов:*

После чего пользователь вводит рейтинг с клавиатуры.
*(Например, 8)*

С помощью функции *get_movies_by_rating*
отправляется запрос API:

https://api.kinopoisk.dev/v1.3/movie?rating.kp=8&limit=5

Ответ API:
```json
{
    "docs": [
        {
            "externalId": {
                "imdb": "tt0088847",
                "tmdb": 2108,
                "kpHD": "415303c6e7488ce7b802872fffad0552"
            },
            "rating": {
                "kp": 8,
                "imdb": 7.8,
                "filmCritics": 7.7,
                "russianFilmCritics": 100,
                "await": null
            },
            "votes": {
                "kp": 93437,
                "imdb": 452195,
                "filmCritics": 62,
                "russianFilmCritics": 3,
                "await": 0
            },
            "movieLength": 97,
            "id": 21844,
            "type": "movie",
            "name": "Клуб «Завтрак»",
            "description": "Пятеро школьников в наказание за проступки вынуждены приехать в школу в выходной день и написать сочинение на тему «Кем вы себя представляете?» Молодым людям с большим трудом удается разобраться в своих проблемах.",
            "year": 1985,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/1946459/8cfbe2f6-7e1b-4e2d-a408-5c9eb7354466/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1946459/8cfbe2f6-7e1b-4e2d-a408-5c9eb7354466/x1000"
            },
            "genres": [
                {
                    "name": "драма"
                },
                {
                    "name": "комедия"
                }
            ],
            "countries": [
                {
                    "name": "США"
                }
            ],
            "alternativeName": "The Breakfast Club",
            "enName": null,
            "names": [
                {
                    "name": "Клуб «Завтрак»"
                },
                {
                    "name": "The Breakfast Club"
                },
                {
                    "name": "Клуб Завтрак",
                    "language": "RU",
                    "type": null
                },
                {
                    "name": "Der Frühstücksclub",
                    "language": "DE",
                    "type": null
                },
                {
                    "name": "O Clube",
                    "language": "PT",
                    "type": null
                },
                {
                    "name": "Breakfast Club - Der Frühstücksclub",
                    "language": "DE",
                    "type": null
                },
                {
                    "name": "બ્રેકફાસ્ટ ક્લબ",
                    "language": "IN",
                    "type": "Gujarati"
                },
                {
                    "name": "പ്രഭാതഭക്ഷണ ക്ലബ്",
                    "language": "IN",
                    "type": "Malayalam"
                },
                {
                    "name": "ब्रेकफास्ट क्लब",
                    "language": "IN",
                    "type": "Marathi"
                },
                {
                    "name": "బ్రేక్ ఫాస్ట్ క్లబ్",
                    "language": "IN",
                    "type": "Telugu"
                },
                {
                    "name": "ਨਾਸ਼ਤੇ ਦਾ ਕਲੱਬ",
                    "language": "IN",
                    "type": "Punjabi"
                },
                {
                    "name": "조찬클럽",
                    "language": "KR",
                    "type": null
                },
                {
                    "name": "El club de los cinco",
                    "language": "ES",
                    "type": null
                },
                {
                    "name": "ブレックファスト・クラブ",
                    "language": "JP",
                    "type": null
                },
                {
                    "name": "ブレックファスト・クラブ：1985",
                    "language": "JP",
                    "type": null
                },
                {
                    "name": "Le club des petits déjeuners",
                    "language": "CA",
                    "type": "french"
                },
                {
                    "name": "Le club des petits déjeuners",
                    "language": "FR",
                    "type": "french"
                },
                {
                    "name": "Breakfast Club",
                    "language": "FR",
                    "type": "fr-FR title"
                }
            ],
            "shortDescription": "Спортсмен, принцесса, ботан, хулиган и чудачка пишут сочинение о самих себе. Подростковая комедия Джона Хьюза",
            "logo": {
                "url": "https://imagetmdb.com/t/p/original/iyFNHG7CwqWHMPQI1FsDjczZx7I.png"
            },
            "watchability": {
                "items": [
                    {
                        "name": "Иви",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/2419418/0dfd1724-848f-4725-9160-abc571f41c11/orig"
                        },
                        "url": "https://www.ivi.ru/watch/90307?utm_source=yandex&utm_medium=wizard"
                    }
                ]
            }
        },
        {
            "id": 1162236,
            "externalId": {
                "kpHD": "4f3fa88ec913aaea98948e1447157f66"
            },
            "name": "Мамы чемпионов",
            "alternativeName": null,
            "names": [
                {
                    "name": "Мамы чемпионов",
                    "language": "RU",
                    "type": "Russian title on kinopoisk"
                }
            ],
            "type": "tv-series",
            "year": 2018,
            "description": "У 17-летней Веры было всё: золото на соревнованиях, любимый человек, обожаемый папа, мама–тренер по плаванию. Но после предательства мамы в один момент от Веры «уплыла» вся её успешная жизнь: девушка неожиданно покидает большой спорт и остаётся одна с ребёнком на руках. Спустя 15 лет, она успешный тренер, среди подопечных которой — её сын Кирилл. Только прошлое не отпускает Веру и преподносит заманчивое предложение. И теперь бывшей чемпионке придётся вновь столкнуться не только с коварством собственной матери, готовой пойти на всё ради больших побед, но и экс-парнем, возглавившим сборную страны по плаванию.",
            "shortDescription": "Вера одна воспитывает сына-спортсмена и противостоит жестокой матери. Драма о семейных трагедиях и амбициях",
            "rating": {
                "kp": 8,
                "imdb": 0,
                "filmCritics": 0,
                "russianFilmCritics": 0,
                "await": null
            },
            "votes": {
                "kp": 72862,
                "imdb": 0,
                "filmCritics": 0,
                "russianFilmCritics": 1,
                "await": 0
            },
            "movieLength": null,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/4774061/7ba75d7c-48c4-4067-94be-a1fc237eaa04/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/4774061/7ba75d7c-48c4-4067-94be-a1fc237eaa04/x1000"
            },
            "genres": [
                {
                    "name": "драма"
                },
                {
                    "name": "спорт"
                }
            ],
            "countries": [
                {
                    "name": "Россия"
                }
            ],
            "watchability": {
                "items": [
                    {
                        "name": "Wink",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/1672343/54096cbe-cc3b-41c9-8e44-990ebbca8d61/orig"
                        },
                        "url": "https://wink.ru/media_items/82957130?utm_source=yandex&utm_medium=koldunschick&utm_content=name"
                    },
                    {
                        "name": "ctc.ru",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/224348/9c4fb43c-11f0-4245-9848-7c76c7917d37/orig"
                        },
                        "url": "https://ctc.ru/projects/serials/mamy_chempionov/?utm_source=yandex&utm_medium=feed"
                    }
                ]
            },
            "releaseYears": [
                {
                    "start": 2018,
                    "end": 2018
                }
            ]
        },
        {
            "id": 957773,
            "externalId": {
                "kpHD": null
            },
            "name": "Мажор 2",
            "alternativeName": null,
            "names": [
                {
                    "name": "Мажор 2",
                    "language": "RU",
                    "type": "Russian title on kinopoisk"
                }
            ],
            "type": "tv-series",
            "year": 2016,
            "description": "Неожиданно для всех Игоря Соколовского выпускают из СИЗО, сняв все обвинения в покушении на жизнь бизнесмена Игнатьева. Но Мажор выходит с одним-единственным желанием – отомстить, так как он считает Игнатьева виновным в смерти отца и матери. Соколовский возвращается на службу в полицию, возглавляет бизнес отца, который перешел ему по наследству, заводит красивый и яркий роман с Катей. Мучается из-за отношений с Викой – они так и не смогли забыть друг друга. И день за днем торопит развязку – уничтожение Игнатьева. Но что будет после того, как цель достигнута? После того, как придется посмотреть на победу с другой стороны…",
            "shortDescription": null,
            "rating": {
                "kp": 8,
                "imdb": 0,
                "filmCritics": 0,
                "russianFilmCritics": 0,
                "await": null
            },
            "votes": {
                "kp": 45764,
                "imdb": 0,
                "filmCritics": 0,
                "russianFilmCritics": 1,
                "await": 0
            },
            "movieLength": null,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/1946459/aa61f2a0-5f70-4bcc-abef-38c0af3946bc/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1946459/aa61f2a0-5f70-4bcc-abef-38c0af3946bc/x1000"
            },
            "genres": [
                {
                    "name": "драма"
                },
                {
                    "name": "криминал"
                }
            ],
            "countries": [
                {
                    "name": "Россия"
                }
            ],
            "watchability": {
                "items": [
                    {
                        "name": "24ТВ",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/2439731/85e83b8d-1159-4781-bad5-ce0a809b3843/orig"
                        },
                        "url": "https://24h.tv/contents/2014-mazhor-813517345270657381"
                    },
                    {
                        "name": "Смотрёшка",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/236744/c88e652e-2eb1-472d-b636-a266364dbf58/orig"
                        },
                        "url": "https://smotreshka.tv/archive/5bd65b99b2de77478b1f99ee?utm_source=yandex_search&utm_campaign=yandex_feed&utm_term=archive&utm_content=archive"
                    },
                    {
                        "name": "Иви",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/2419418/0dfd1724-848f-4725-9160-abc571f41c11/orig"
                        },
                        "url": "https://www.ivi.ru/watch/mazhor?utm_source=yandex&utm_medium=wizard"
                    },
                    {
                        "name": "PREMIER",
                        "logo": {
                            "url": "https://avatars.mds.yandex.net/get-ott/239697/0f86e907-9531-47e9-87bd-5101a08d4e30/orig"
                        },
                        "url": "https://premier.one/show/242357?utm_source=yandex&utm_medium=yandex_feed_search&utm_campaign=yandex_feed"
                    }
                ]
            },
            "releaseYears": [
                {
                    "start": 2016,
                    "end": 2016
                }
            ]
        },
        {
            "id": 80754,
            "type": "movie",
            "externalId": {
                "kpHD": "52e556bc5bc040aab1199fe5bfbd63fe",
                "imdb": "tt0052893",
                "tmdb": 5544
            },
            "name": "Хиросима, моя любовь",
            "rating": {
                "kp": 8,
                "imdb": 7.8,
                "filmCritics": 8.8,
                "russianFilmCritics": 0,
                "await": null
            },
            "description": "История короткой любви французской киноактрисы и японского архитектора в послевоенной Хиросиме. На каждого из них давит груз прошлого, с которым приходится жить каждый час.",
            "votes": {
                "kp": 13358,
                "imdb": 37281,
                "filmCritics": 46,
                "russianFilmCritics": 1,
                "await": 0
            },
            "year": 1959,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/6201401/30193f9c-a8bb-465e-97bf-8f3388f34687/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/6201401/30193f9c-a8bb-465e-97bf-8f3388f34687/x1000"
            },
            "genres": [
                {
                    "name": "драма"
                },
                {
                    "name": "мелодрама"
                }
            ],
            "countries": [
                {
                    "name": "Франция"
                },
                {
                    "name": "Япония"
                }
            ],
            "alternativeName": "Hiroshima mon amour",
            "enName": null,
            "movieLength": 91,
            "names": [],
            "shortDescription": null,
            "logo": {
                "url": null
            },
            "watchability": {
                "items": []
            }
        },
        {
            "id": 257371,
            "type": "anime",
            "externalId": {
                "kpHD": null,
                "tmdb": 34801
            },
            "name": "Волчий дождь",
            "rating": {
                "kp": 8,
                "imdb": 7.9,
                "filmCritics": 0,
                "russianFilmCritics": 0,
                "await": null
            },
            "description": "Еле уловимый аромат Лунного цветка — это все, чему можно здесь верить. Согласно пророчеству, этот запах приведет в рай, что откроется на исходе времен. Одержимый Киба, невозмутимый Цумэ, юный Тобоэ и беззаботный Хигэ — волки, способные принимать человеческое обличье. Возможно, именно им предстоит открыть ворота туда, где теряет значение слово «судьба». В погибающем мире, не помнящем света, эти четверо отправляются в путь.",
            "votes": {
                "kp": 13123,
                "imdb": 8508,
                "filmCritics": 0,
                "russianFilmCritics": 0,
                "await": 0
            },
            "year": 2003,
            "poster": {
                "url": "https://image.openmoviedb.com/kinopoisk-images/1704946/f3cf9b1b-e747-4cb6-99ae-36e452538d45/orig",
                "previewUrl": "https://image.openmoviedb.com/kinopoisk-images/1704946/f3cf9b1b-e747-4cb6-99ae-36e452538d45/x1000"
            },
            "genres": [
                {
                    "name": "аниме"
                },
                {
                    "name": "мультфильм"
                },
                {
                    "name": "фэнтези"
                },
                {
                    "name": "драма"
                },
                {
                    "name": "приключения"
                }
            ],
            "countries": [
                {
                    "name": "Япония"
                }
            ],
            "alternativeName": "Wolf's Rain",
            "enName": null,
            "names": [
                {
                    "name": "Волчий дождь"
                },
                {
                    "name": "Wolf's Rain"
                }
            ],
            "movieLength": null,
            "shortDescription": null,
            "logo": {
                "url": null
            },
            "watchability": {
                "items": []
            },
            "releaseYears": [
                {
                    "start": 2003,
                    "end": 2004
                }
            ]
        }
    ],
    "total": 46,
    "limit": 5,
    "page": 1,
    "pages": 10
}
```

Далее, приходит в ответ несколько вариантов фильмов,
в виде инлайн-кнопок, где указано
название фильма и год выпуска. В данном запросе также
установлен лимит - 5 фильмов с запрашиваемым рейтингом.

Ответ бота:

Выбери фильм:
Кнопка 1 - Клуб "Завтрак" (1999)
Кнопка 2 - Мамы чемпионов (2003)
Кнопка 3 - Мажор 2 (2003)
Кнопка 4 - Хиросима, моя любовь (1959)
Кнопка 5 - Волчий дождь (2016)


Пользователю предоставляется выбор
интересующего фильма. Пользователь выбирает
фильм *(например, Хиросима, моя любовь (1959))*.

Аналогично поиску по имени, обрабатывается
информация с помощью функции *get_movies_by_id*, в которую
передается id нужного фильма, отправляется повторный
запрос API уже по id:

https://api.kinopoisk.dev/v1.3/movie?id=301&limit=1

в ответ ему приходит сообщение, где также 
изображен постер фильма, наименование, год,
рейтинг, страны производители, жанр и описание.

Ответ бота:

**Фото**
*Хиросима, моя любовь (1959)*
*Рейтинг: 8*
*Страны: Франция, Япония*
*Жанр: драма, мелодрама*

*Описание:История короткой любви французской
киноактрисы и японского архитектора в послевоенной
Хиросиме. На каждого из них давит груз прошлого,
с которым приходится жить каждый час.*

После чего фильм автоматически добавлен в историю поиска.

   **`/person_name`** — поиск актёра/режисера по имени.

При вызове данной команды бот отправляет
сообщение пользователю:
*Введите имя актера:*

После чего пользователь вводит название интересующего
его фильма с клавиатуры.
*(Например, Киану Ривз)*

С помощью функции *get_person_by_name*
отправляется запрос API:

https://api.kinopoisk.dev//v1.4/person/search?query=Киану_Ривз&page=1&limit=1

Ответ API:

```json
{
    "docs": [
        {
            "id": 7836,
            "name": "Киану Ривз",
            "enName": "Keanu Reeves",
            "photo": "https://avatars.mds.yandex.net/get-kinopoisk-image/10671298/ab4697b5-dc63-4168-84fc-9d6481408219/orig",
            "sex": "Мужской",
            "growth": 186,
            "birthday": "1964-09-02T00:00:00.000Z",
            "death": "",
            "age": 60
        }
    ],
    "total": 1000,
    "limit": 1,
    "page": 1,
    "pages": 1000
}
```

В ответ ему приходит сообщение, где 
изображен постер фильма, имя, дата рождения,
возраст и пол.

Ответ бота:

**Фото**
*Киану Ривз*
*Дата рождения: 02.09.1964*
*возраст: 60, пол: Мужской*

После чего запрос автоматически добавлен в историю поиска.


  Команда **`/history`** - позволяет просматривать историю поисковых запросов.

✔ Хранит последние 10 запросов (фильмы/актеры)

✔ Автоматически удаляет самые старые записи при превышении лимита

✔ Отображает постер (если доступен) и краткую информацию по каждому запросу

Реализована постраничная навигация - каждый запрос отображается на отдельной странице

4. #### default command:

**/start** - команда старт, используется для начала работы с ботом.

При запуске бота отправляет приветственное сообщение и рассказывает
о своем назначении и предлагает перейти в меню
для дальнейшей работы.

Пример ответа бота при первом обращении:
*Привет, name!*
*Этот бот предназначен для поиска фильмов по названию,
рейтингу, или для получения информации
по имени актера/режиссера.*

*Чтобы посмотреть список доступных команд
набери команду /help, либо перейди в меню 👇*

Пример ответа бота при последующих обращениях:
*С возвращением, name! 👋*

*Чтобы посмотреть список доступных команд
набери команду /help, либо перейди в меню 👇*

**/help** - помощь по работе бота, здесь описаны
все возможные функции бота.

Пример ответа бота:

*Доступные команды:*

*/start - Запустить бота
/help - Cправка по работе бота
/helloworld - Приветствие
/history - Вывести историю запросов
/movie_search - Поиск фильма по названию
/movies_rating - Поиск фильмов по рейтингу
/person_name - Поиск актера по имени*

**`/helloworld`** — команда приветствия.

При выборе команды оправляет приветственное сообщение.
Ответ бота на команду */helloworld*:

*Hello World!*

### Как запустить

1. Открыть терминал
2. Выбрать папку для копирования
   *cd путь к папке*

3. Cкопировать ссылку на репозиторий HTTPS:
   *https://gitlab.skillbox.ru/oksana_kravchenko/python_basic_diploma.git*

4. В терминале установить репозиторий
   *git clone https://gitlab.skillbox.ru/oksana_kravchenko/python_basic_diploma.git*

5. Установить зависимости
   *pip install -r requirements.txt*