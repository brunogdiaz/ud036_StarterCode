import media 
import fresh_tomatoes as FT 

title = "Toy Story"
storyline = "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to"\
            "a young boy named Andy (John Morris), sees his position as"\
            " Andy's favorite toy jeopardized when his parents buy him a"\
            " Buzz Lightyear (Tim Allen) action figure. Even worse, the"\
            " arrogant Buzz thinks he's a real spaceman on a mission to"\
            " return to his home planet. When Andy's family moves to a"\
            " new house, Woody and Buzz must escape the clutches of"\
            " maladjusted neighbor Sid Phillips (Erik von Detten) and"\
            " reunite with their boy."

trailer = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
image = "images/Toy_Story.jpg"

toy_story = media.Movie(title, storyline, image, trailer)

title = "Ratatouille"
storyline = "Remy (Patton Oswalt), a resident of Paris, appreciates good food"\
            " and has quite a sophisticated palate. He would love to become a"\
            " chef so he can create and enjoy culinary masterpieces to his"\
            " heart's delight. The only problem is, Remy is a rat. When he"\
            " winds up in the sewer beneath one of Paris' finest restaurants,"\
            " the rodent gourmet finds himself ideally placed to realize his"\
            " dream."

trailer = "https://www.youtube.com/watch?v=1yKqLNnxGZw"
image = "images/Ratatouille.jpg"

ratatouille = media.Movie(title, storyline, image, trailer)

title = "Space Jam"
storyline = "Swackhammer (Danny DeVito), an evil alien theme park owner, "\
            "needs a new attraction at Moron Mountain. When his gang, the "\
            "Nerdlucks, heads to Earth to kidnap Bugs Bunny (Billy West)"\
            " and the Looney Tunes, Bugs challenges them to a basketball"\
            " game to determine their fate. The aliens agree, but they steal"\
            " the powers of NBA basketball players, including Larry Bird "\
            "(Larry Bird) and Charles Barkley (Charles Barkley) -- so Bugs"\
            " gets some help from superstar Michael Jordan (Michael Jordan)."

trailer = "https://www.youtube.com/watch?v=oKNy-MWjkcU"
image = "images/Space_Jam.jpg"

space_jam = media.Movie(title, storyline, image, trailer)

title = "The Hunger Games"
storyline = "In what was once North America, the Capitol of Panem maintains"\
            " its hold on its 12 districts by forcing them each to select a"\
            " boy and a girl, called Tributes, to compete in a nationally"\
            " televised event called the Hunger Games. Every citizen must"\
            " watch as the youths fight to the death until only one remains."\
            " District 12 Tribute Katniss Everdeen (Jennifer Lawrence) has"\
            " little to rely on, other than her hunting skills and sharp "\
            "instincts, in an arena where she must weigh survival against "\
            "love."

trailer = "https://www.youtube.com/watch?v=mfmrPu43DF8"
image = "images/Hunger_Games.jpg"

the_hunger_games = media.Movie(title, storyline, image, trailer)

movies = [toy_story, ratatouille, space_jam, the_hunger_games]

FT.open_movies_page(movies)


