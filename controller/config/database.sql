SELECT r.name, r.city, r.cuisine_type, r.price_range, COUNT(uc.choice_id) as total_picks
FROM Restaurants r
LEFT JOIN UserChoices uc ON r.restaurant_id = uc.restaurant_id
GROUP BY r.restaurant_id
ORDER BY total_picks DESC;