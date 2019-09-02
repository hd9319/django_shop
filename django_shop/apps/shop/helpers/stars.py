from statistics import mean

star_filled = '&#9733; '
star_empty = '&#9734; '
total_stars = 5

def get_stars(rating):
	stars = ''
	stars_filled = int(rating)
	stars_empty = 5 - stars_filled

	stars += ''.join([star_filled for _ in range(stars_filled)])
	stars += ''.join([star_empty for _ in range(stars_empty)])

	return stars

def get_ratings_context(ratings):
	num_ratings = ratings.count()

	if num_ratings == 0:
		rating = 0.0
	else:
		rating = round(mean([rating[0] for rating in ratings]), 1)

	stars = get_stars(rating)

	ratings_context = {
		'rating': rating,
		'num_ratings': num_ratings,
		'stars': stars
	}

	return ratings_context