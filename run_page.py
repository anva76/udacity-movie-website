""" This module creates a list of movie instances and displays an html page """
import media
import fresh_tomatoes

# A list of Movie class instances
movies = []

# Interstellar movie - title, storyline, poster, trailer
movies.append(media.Movie(
        "Interstellar",
        "A team of explorers travel through a wormhole in space in "
        "an attempt to ensure humanity's survival.",
        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=zSWdZVtXT7E"))

# Avatar movie - title, storyline, poster, trailer
movies.append(media.Movie(
        "Avatar",
        "A paraplegic marine dispatched to the moon Pandora on a unique "
        "mission becomes torn between following his orders and protecting "
        "the world he feels is his home.",
        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=5PSNL1qE6VY"))

# I am Legend movie - title, storyline, poster, trailer
movies.append(media.Movie(
        "I Am Legend",
        "Years after a plague kills most of humanity and transforms "
        "the rest into monsters, the sole survivor in New York City "
        "struggles valiantly to find a cure.",
        "https://upload.wikimedia.org/wikipedia/en/d/df/I_am_legend_teaser.jpg",  # NOQA
        "https://www.youtube.com/watch?v=ewpYq9rgg3w"))

# Guardians of the Galaxy movie - title, storyline, poster, trailer
movies.append(media.Movie(
        "Guardians of the Galaxy Vol. 2",
        "The Guardians must fight to keep their newfound family together "
        "as they unravel the mystery of Peter Quill's true parentage.",
        "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=duGqrYw4usE"))

# Pirates of the Caribbean movie - title, storyline, poster, trailer
movies.append(media.Movie(
        "Pirates of the Caribbean: Dead Men Tell No Tales",
        "Captain Jack Sparrow searches for the trident of Poseidon while "
        "being pursued by an undead sea captain and his crew.",
        "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",  # NOQA
        "https://www.youtube.com/watch?v=Hgeu5rhoxxY"))

# The Good, the Bad and the Ugly movie - title, storyline, poster, trailer
movies.append(media.Movie(
        "The Good, the Bad and the Ugly",
        "A bounty hunting scam joins two men in an uneasy alliance against "
        "a third in a race to find a fortune in gold buried in "
        "a remote cemetery.",
        "https://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=JdkSuurdbDA"))

# Generate an html page
fresh_tomatoes.open_movies_page(movies)
