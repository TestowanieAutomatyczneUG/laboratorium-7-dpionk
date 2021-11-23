import json
import requests
import unittest

class Food:
	def get_all_by_first_letter(self, letter):
		if type(letter) is str and len(letter) == 1 and letter in "abcdefghijklmnopqrstuvwxyz":
			r = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
			result = json.loads(r.content.decode('utf-8'))['meals']
			resultArray = []
			for i in result:
				resultArray.append(i['strMeal'])
			return resultArray
		else:
			raise ValueError("Podano zły argument")

	def get_one_by_id(self, id):
		if type(id) is int:
			r = requests.get(f"http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
			result = json.loads(r.content.decode('utf-8'))['meals']
			if result == None:
				raise ValueError("W bazie nie ma posiłku o takim ID")
			else:
				return result[0]['strMeal']
		else:
			raise ValueError("Podano zły argument")

	def get_by_category(self, category):
		if type(category) is str:
			r = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}")
			result = json.loads(r.content.decode('utf-8'))['meals']
			if result == None:
				raise ValueError("Podano zły argument")
			else:
				resultArray = []
				for i in result:
					resultArray.append(i['strMeal'])
				return resultArray
		else:
			raise ValueError("Podano zły argument")

	def check_if_has_ingredient(self, id, ingredient):
		if type(id) is int and type(ingredient) is str:
			r = requests.get(f"http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
			result = json.loads(r.content.decode('utf-8'))['meals']
			if result == None:
				raise ValueError("W bazie nie ma posiłku o takim ID")
			else:
				for i in result:
					for j in i:
						if i[j] == ingredient:
							return True
				return False
		else:
			raise ValueError("Podano zły argument")

class Recipe:
	def get_recipe_by_id(self, id):
		if type(id) is int:
			r = requests.get(f"http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
			result = json.loads(r.content.decode('utf-8'))['meals']
			if result == None:
				raise ValueError("W bazie nie ma posiłku o takim ID")
			else:
				return result[0]['strInstructions']

		else:
			raise ValueError("Podano zły argument")

	def get_easiest_recipe_first_letter(self, letter):
		if type(letter) is str and len(letter) == 1 and letter in "abcdefghijklmnopqrstuvwxyz":
			r = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
			result = json.loads(r.content.decode('utf-8'))['meals']
			easiest_recipe = result[0]['strInstructions']
			if easiest_recipe != None:
				for i in result:
					if len(i['strInstructions']) < len(easiest_recipe):
						easiest_recipe = i['strInstructions']
				return easiest_recipe
			else:
				raise ValueError("Podano zły argument")
		else:
			raise ValueError("Podano zły argument")


class Categories:
	def get_food_categories(self):
		r = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
		result = json.loads(r.content.decode('utf-8'))['categories']
		resultArray = []
		for i in result:
			resultArray.append(i['strCategory'])
		return resultArray

class Ingredient:
	def get_all_ingredients_starting_with_letter(self, letter):
		if type(letter) is str and len(letter) == 1 and letter in "abcdefghijklmnopqrstuvwxyz":
			r = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?i=list")
			result = json.loads(r.content.decode('utf-8'))['meals']
			resultArray = []
			for i in result:
				if i['strIngredient'].lower()[0] == letter:
					resultArray.append(i['strIngredient'])
			return resultArray
		else:
			raise ValueError("Podano zły argument")


get_all_fl = Food().get_all_by_first_letter
get_one_id = Food().get_one_by_id
get_recipe = Recipe().get_recipe_by_id
get_category = Food().get_by_category
easiest_recipe = Recipe().get_easiest_recipe_first_letter
has_ingredient = Food().check_if_has_ingredient

class Food_test(unittest.TestCase):

	def test_first_letter_ok(self):
		self.assertEqual(['Apple Frangipan Tart', 'Apple & Blackberry Crumble', 'Apam balik', 'Ayam Percik'], get_all_fl("a"))

	def test_first_letter_ok_2(self):
		self.assertEqual(['Dal fry', 'Dundee cake', 'Duck Confit'], get_all_fl("d"))

	def test_first_letter_wrong_argument(self):
		self.assertRaises(ValueError, get_all_fl, 2342343)

	def test_first_letter_wrong_argument_2(self):
		self.assertRaises(ValueError, get_all_fl, None)

	def test_first_letter_wrong_argument_3(self):
		self.assertRaises(ValueError, get_all_fl, "")

	def test_first_letter_wrong_argument_4(self):
		self.assertRaises(ValueError, get_all_fl, "1")

	def test_one_id_ok(self):
		self.assertEqual("Teriyaki Chicken Casserole", get_one_id(52772))

	def test_one_id_ok_2(self):
		self.assertEqual("Fennel Dauphinoise", get_one_id(52919))

	def test_one_id_wrong_argument(self):
		self.assertRaises(ValueError, get_one_id,"gdfg")

	def test_one_id_wrong_argument_2(self):
		self.assertRaises(ValueError, get_one_id, 6)

	def test_one_id_wrong_argument_3(self):
		self.assertRaises(ValueError, get_one_id, None)

	def test_food_categories(self):
		self.assertEqual(['Beef', 'Chicken', 'Dessert', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side', 'Starter', 'Vegan', 'Vegetarian', 'Breakfast', 'Goat'], Categories().get_food_categories())

	def test_get_recipe_ok(self):
		self.assertEqual("Preheat oven to 350\u00b0 F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, \u00bd cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!", get_recipe(52772))

	def test_get_recipe_ok_2(self):
		self.assertEqual("Twist the heads from the prawns, then peel away the legs and shells, but leave the tails intact. Devein each prawn. Fry the shells in 1 tbsp oil for 5 mins, until dark pink and golden in patches. Add the wine, boil down by two thirds, then pour in the stock. Strain into a jug, discarding the shells.\r\nHeat the rest of the oil in a deep frying pan or casserole. Add the fennel, onion and garlic, season, then cover and gently cook for 10 mins until softened. Meanwhile, peel the potato and cut into 2cm-ish chunks. Put into a pan of cold water, bring to the boil and cook for 5 mins until almost tender. Drain in a colander.\r\nPeel a strip of zest from the orange. Put the zest, star anise, bay and \u00bd tsp harissa into the pan. Fry gently, uncovered, for 5-10 mins, until the vegetables are soft, sweet and golden.\r\nStir in the tomato pur\u00e9e, cook for 2 mins, then add the tomatoes and stock. Simmer for 10 mins until the sauce thickens slightly. Season to taste. The sauce can be made ahead, then reheated later in the day. Meantime, scrub the mussels or clams and pull away any stringy beards. Any that are open should be tapped sharply on the worktop \u2013 if they don\u2019t close after a few seconds, discard them.\r\nReheat the sauce if necessary, then stir the potato, chunks of fish and prawns very gently into the stew. Bring back to the boil, then cover and gently simmer for 3 mins. Scatter the mussels or clams over the stew, then cover and cook for 2 mins more or until the shells have opened wide. Discard any that remain closed. The chunks of fish should flake easily and the prawns should be pink through. Scatter with the thyme leaves.\r\nTo make the quick rouille, stir the rest of the harissa through the mayonnaise. Serve the stew in bowls, topped with spoonfuls of rouille, which will melt into the sauce and enrich it. Have some good bread ready, as you\u2019ll definitely want to mop up the juices.", get_recipe(52918))

	def test_get_recipe_wrong_argument(self):
		self.assertRaises(ValueError, get_recipe, 667)

	def test_get_recipe_wrong_argument_2(self):
		self.assertRaises(ValueError, get_recipe, "34543543")

	def test_get_recipe_wrong_argument_3(self):
		self.assertRaises(ValueError, get_recipe, True)

	def test_get_category_ok(self):
		self.assertEqual(['Baked salmon with fennel & tomatoes', 'Cajun spiced fish tacos', 'Escovitch Fish', 'Fish fofos', 'Fish pie', 'Fish Stew with Rouille', 'Garides Saganaki', 'Grilled Portuguese sardines', 'Honey Teriyaki Salmon', 'Kedgeree', 'Kung Po Prawns', 'Laksa King Prawn Noodles', 'Mediterranean Pasta Salad', 'Mee goreng mamak', 'Nasi lemak', 'Portuguese fish stew (Caldeirada de peixe)', 'Recheado Masala Fish', 'Salmon Avocado Salad', 'Salmon Prawn Risotto', 'Saltfish and Ackee', 'Seafood fideuà', 'Shrimp Chow Fun', 'Sledz w Oleju (Polish Herrings)', 'Spring onion and prawn empanadas', 'Three Fish Pie', 'Tuna and Egg Briks', 'Tuna Nicoise'], get_category("seaFood"))

	def test_get_category_ok_2(self):
		self.assertEqual(['Ayam Percik', 'Brown Stew Chicken', 'Chick-Fil-A Sandwich', 'Chicken & mushroom Hotpot', 'Chicken Alfredo Primavera', 'Chicken Basquaise', 'Chicken Congee', 'Chicken Couscous', 'Chicken Enchilada Casserole', 'Chicken Fajita Mac and Cheese', 'Chicken Ham and Leek Pie', 'Chicken Handi', 'Chicken Karaage', 'Chicken Marengo', 'Chicken Parmentier', 'Chicken Quinoa Greek Salad', 'Coq au vin', 'Crock Pot Chicken Baked Tacos', 'French Onion Chicken with Roasted Carrots & Mashed Potatoes', "General Tso's Chicken", 'Honey Balsamic Chicken with Crispy Broccoli & Potatoes', 'Jerk chicken with rice & peas', 'Katsu Chicken curry', 'Kentucky Fried Chicken', 'Kung Pao Chicken', 'Nutty Chicken Curry', 'Pad See Ew', 'Piri-piri chicken and slaw', 'Potato Gratin with Chicken', 'Rappie Pie', 'Rosół (Polish Chicken Soup)', 'Shawarma', 'Tandoori chicken', 'Teriyaki Chicken Casserole', 'Thai Green Curry'], get_category("chicken"))

	def test_get_category_wrong_argument(self):
		self.assertRaises(ValueError, get_category, "dfdsf")

	def test_get_category_wrong_argument_2(self):
		self.assertRaises(ValueError, get_category, True)

	def test_get_category_wrong_argument_3(self):
		self.assertRaises(ValueError, get_category, 3)

	def test_easiest_recipe_ok(self):
		self.assertEqual("Mix milk, oil and egg together. Sift flour, baking powder and salt into the mixture. Stir well until all ingredients are combined evenly.\r\n\r\nSpread some batter onto the pan. Spread a thin layer of batter to the side of the pan. Cover the pan for 30-60 seconds until small air bubbles appear.\r\n\r\nAdd butter, cream corn, crushed peanuts and sugar onto the pancake. Fold the pancake into half once the bottom surface is browned.\r\n\r\nCut into wedges and best eaten when it is warm.", easiest_recipe("a"))

	def test_easiest_recipe_ok_2(self):
		self.assertEqual("Crush the meat so that it is finite and we put it on a griddle to brown. Put the eggs, bacon and ham to fry.\r\nCut the bread in half, put the beef brisket, the fried eggs, the bacon, the ham, the mozzarella, the tomato and the lettuce. Cover with the other half of the bread and serve.", easiest_recipe("c"))
	def test_easiest_recipe_wrong(self):
		self.assertRaises(ValueError, get_recipe, "z")

	def test_easiest_recipe_wrong_2(self):
		self.assertRaises(ValueError, get_recipe, "sfsdfdsfdsfs")

	def test_easiest_recipe_wrong_3(self):
		self.assertRaises(ValueError, get_recipe, 4565)

	def test_get_all_ingredients_first_letter_ok(self):
		self.assertEqual(['Avocado','Apple Cider Vinegar','Asparagus','Aubergine','Apricot','Apricot Jam','Almonds','Apples','Ackee','Ancho Chillies','Almond Milk','Allspice','Almond Extract','Anchovy Fillet'], Ingredient().get_all_ingredients_starting_with_letter("a"))

	def test_get_all_ingredients_first_letter_ok(self):
		self.assertEqual(['Zucchini'], Ingredient().get_all_ingredients_starting_with_letter("z"))

	def test_get_all_ingredients_first_letter_wrong(self):
		self.assertRaises(ValueError, Ingredient().get_all_ingredients_starting_with_letter, "sdgdsg")

	def test_get_all_ingredients_first_letter_wrong_2(self):
		self.assertRaises(ValueError, Ingredient().get_all_ingredients_starting_with_letter, {})

	def test_check_if_has_ingredient_ok(self):
		self.assertEqual(True, has_ingredient(52772, "chicken breasts"))

	def test_check_if_has_ingredient_ok_2(self):
		self.assertEqual(False, has_ingredient(52774, "chicken breasts"))

	def test_check_if_has_ingredient_wrong_id(self):
		self.assertRaises(ValueError, has_ingredient, 52344, "chicken breasts")

	def test_check_if_has_ingredient_wrong_ingredient(self):
		self.assertRaises(ValueError, has_ingredient, 52344, 6456545)

	def test_check_if_has_ingredient_wrong_arguments(self):
		self.assertRaises(ValueError, has_ingredient, "sdff", {})

	def test_check_if_has_ingredient_wrong_arguments(self):
		self.assertRaises(ValueError, has_ingredient, 52344, True)
