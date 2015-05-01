from Classes.ingredients import Ingredient
from Classes.recipe import Recipe

def main():
	i = Ingredient(title="egg")

	r = Recipe(title="Scrambled eggs", ingredients=[i],
		directions=['Break egg', 'Beat egg', 'Cook egg'])

	r.print_recipes()

if __name__ == "__main__":
	main() 