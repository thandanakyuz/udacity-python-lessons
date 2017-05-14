import media, fresh_tomatoes

scott_pilgrim = media.Movie("Scott Pilgrim",
                            "Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcT4LTAKx5v-BsXPTSlwmnN35T-cl-3GWeeYt0eVkoN92x0cRVJ0",
                            "https://www.youtube.com/watch?v=8NUBVcit5VM")

vanilla_sky = media.Movie("Vanilla Sky",
                          "A self-indulgent and vain publishing magnate finds his privileged life upended after a vehicular accident with a resentful lover.",
                          "http://www.gstatic.com/tv/thumb/movieposters/28886/p28886_p_v8_aa.jpg",
                          "https://www.youtube.com/watch?v=k09OX40NLUw")

zootopia = media.Movie("Zootopia",
                       "In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcQj1fU0-Idujcrs_MB2xEWbVEygeCkcjYUp4Z-hSIPqgu0vFbQi",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

v_for_vendetta = media.Movie("V for Vendetta",
                             "In a future British tyranny, a shadowy freedom fighter, known only by the alias of \"V\", plots to overthrow it with the help of a young woman.",
                             "http://www.impawards.com/2006/posters/v_for_vendetta_ver3.jpg",
                             "https://www.youtube.com/watch?v=k_13fFIrhPk")

boss_baby = media.Movie("The Boss Baby",
                        "A suit-wearing briefcase-carrying baby pairs up with his seven-year old brother to stop the dastardly plot of the CEO of Puppy Co.",
                        "http://www.impawards.com/2017/posters/boss_baby.jpg",
                        "https://www.youtube.com/watch?v=tquIfapGVqs")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

movies = [scott_pilgrim, vanilla_sky, zootopia, v_for_vendetta, boss_baby, inception]
fresh_tomatoes.open_movies_page(movies)
