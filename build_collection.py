import json
import html
from pathlib import Path
from additional_recipes import recipes as additional_recipes

OUT = Path(__file__).parent
sources = {s['id']: s for s in json.loads((OUT/'source-details.json').read_text())}
photos = json.loads((OUT/'photos.json').read_text()) if (OUT/'photos.json').exists() else {}

# All quantities, yields, timings, component assignments and from-scratch steps
# below are original, untested home reconstructions, not CookUnity recipes.
recipes = [
dict(id='11577', short='Chipotle black bean & tofu tacos', yield_='4 servings · 8 small tacos', time='About 45 minutes, plus 20 minutes to soak cashews',
     basis='The page describes a tomato-chipotle tinga with crumbled tofu and black beans, cabbage slaw, and cashew crema. Its ingredient list also includes cumin, nutritional yeast, lemon, and red onion.',
     groups={
       'Tinga filling':['8 small flour tortillas','14 oz (400 g) extra-firm tofu, drained and pressed for 15 minutes','1 can (15 oz) black beans, drained and rinsed','1 can (14–15 oz) crushed or finely chopped tomatoes','1 medium onion, finely diced','3 garlic cloves, minced','1 tbsp olive oil','1 tbsp tomato paste','1–2 chipotle peppers in adobo, minced, plus 1 tsp adobo sauce','1 tsp ground cumin','1 tsp paprika','½ tsp dried oregano','1 bay leaf','½ tsp fine salt to start'],
       'Slaw':['3 cups thinly sliced green cabbage','¼ red onion, thinly sliced','¼ cup chopped cilantro','2 tbsp lime juice','¼ tsp fine salt'],
       'Cashew crema':['½ cup raw cashews, soaked in hot water 20 minutes and drained','⅓ cup fresh water, plus more to thin','1 tbsp lemon juice','1 tbsp lime juice','1 tbsp nutritional yeast','¼ tsp garlic powder','¼ tsp fine salt','Lime wedges, for serving']},
     steps=[
       'Blend the drained cashews with fresh water, citrus juices, nutritional yeast, garlic powder, and salt until completely smooth. Add water a tablespoon at a time until it drizzles easily.',
       'Toss cabbage, red onion, cilantro, lime juice, and salt. Let stand while cooking the filling; drain excess liquid before assembling.',
       'Heat olive oil in a wide skillet over medium heat. Cook the onion for 5–7 minutes until softened. Add minced garlic, tomato paste, chipotle, cumin, paprika, and oregano; stir for 1 minute.',
       'Crumble the tofu into roughly pea-size pieces. Add it with tomatoes, beans, bay leaf, and ½ tsp salt. Simmer uncovered for 15–20 minutes, stirring occasionally, until thick enough to sit in a tortilla without dripping. Add a splash of water if it dries before the flavors come together. Remove the bay leaf and adjust salt and heat.',
       'Warm tortillas in a dry skillet for 20–30 seconds per side. Divide filling among 8 tortillas, add drained slaw, and drizzle with crema. Serve with lime wedges.'
     ],
     notes='The page gives no component quantities. Start with one chipotle for moderate heat; the second makes the filling hotter. These servings are not matched to the delivered meal’s portion or nutrition.',
     reheat='For the delivered meal: separate sauce, slaw, lime, and tortillas. Heat filling at 350°F for 10–15 minutes, or microwave about 2 minutes until hot. Microwave tortillas about 20 seconds, then assemble with the cold toppings.'),
dict(id='3355', short='Quinoa & veggie enchiladas with rice and beans', yield_='4 servings · 8 enchiladas, plus rice and beans', time='About 75 minutes',
     basis='The description names quinoa, kale, Oaxaca/Monterey Jack cheese, chipotle cream, and rice with black beans. The label additionally lists poblano, jalapeño, corn, cream cheese, pepper jack, cheddar, cotija, tomatoes, and other seasonings.',
     groups={
       'Enchiladas':['8 small corn tortillas','½ cup dry quinoa, rinsed','1 cup water for quinoa','1 tbsp olive oil, plus a little for the baking dish','½ medium onion, diced','1 poblano pepper, diced','½ jalapeño, minced; remove seeds for less heat','2 garlic cloves, minced','2 cups finely chopped kale, tough stems removed','½ cup corn','2 oz cream cheese','½ cup shredded Oaxaca cheese','½ cup shredded pepper jack','¼ tsp fine salt, then more to taste'],
       'Chipotle cream and topping':['1 cup heavy cream','¾ cup canned diced tomatoes with juice','1 chipotle pepper in adobo, plus 1 tsp adobo sauce','¼ tsp ground cumin','¼ tsp fine salt','¼ cup shredded white cheddar','2 tbsp crumbled cotija','2 tbsp chopped cilantro'],
       'Rice and beans':['½ cup dry basmati rice, rinsed','1 cup prepared vegetable broth','1 can (15 oz) black beans, drained and rinsed','1 tbsp olive oil','½ medium onion, diced','½ red bell pepper, diced','1 plum tomato, diced','1 garlic clove, minced','½ tsp ground cumin','¼ tsp dried oregano','1 bay leaf','1 tsp lemon juice','Salt to taste']},
     steps=[
       'Heat oven to 375°F and lightly oil a baking dish. Simmer quinoa with 1 cup water, covered, for about 15 minutes until absorbed. Take off heat and rest covered 5 minutes.',
       'For the rice, heat 1 tbsp oil in a saucepan. Soften onion and red pepper for 5–7 minutes. Add garlic, cumin, and oregano; stir 30 seconds. Add plum tomato and cook 2 minutes. Stir in rice, broth, and bay leaf. Cover and simmer on low for 12–15 minutes, or according to the rice package. Fold in drained beans, cover, and warm on low 3–5 minutes; add a splash of water if needed. Rest off heat 5 minutes. Remove bay leaf; add lemon and salt to taste.',
       'For the filling, heat 1 tbsp oil in a skillet. Cook onion, poblano, and jalapeño for 6–8 minutes. Add garlic for 30 seconds, then kale and corn. Cook 3–4 minutes until kale softens and excess moisture evaporates. Off heat, stir in quinoa, cream cheese, Oaxaca, pepper jack, and ¼ tsp salt.',
       'Blend cream, canned tomatoes, chipotle, adobo, cumin, and salt. Pour into a small saucepan and gently simmer for 5 minutes, stirring. Avoid a vigorous boil.',
       'Warm corn tortillas in a covered damp towel in the microwave for 30–45 seconds, until pliable. Spread a little sauce in the baking dish. Divide filling among tortillas, roll, and set seam-side down. Spoon remaining sauce over them and scatter cheddar on top.',
       'Cover and bake for 15 minutes, then uncover for 5–10 minutes until bubbling at the edges. Finish with cotija and cilantro. Serve two enchiladas per person with rice and beans.'
     ],
     notes='The page refers to multiple sauce cups without identifying their separate formulas. This reconstruction uses one chipotle cream. Pepper jack follows the ingredient label; Monterey Jack is named in the description. The home version simplifies commercial oil blends and seasoning additives.',
     reheat='For the delivered meal: remove sauce cups and packaging film. Oven: 350°F for 12–15 minutes. Microwave: vent film and heat 2–3 minutes. Add sauces afterward.'),
dict(id='11104', short='Vegan vodka rigatoni with eggplant meatballs', yield_='4 servings · about 16 small meatballs', time='About 85 minutes; use cooked lentils',
     basis='The page describes rigatoni, tomato and roasted-red-pepper vodka sauce with cashew cream, and eggplant meatballs containing pumpkin and lentils. Spinach, panko, and nutritional yeast appear in the label.',
     groups={
       'Eggplant meatballs':['1 medium-large eggplant, about 1 lb (450 g), cut into ¾-inch cubes','2 tbsp olive oil','½ small onion, finely diced','2 garlic cloves, minced','¾ cup cooked green lentils, well drained','⅓ cup plain pumpkin purée','¾ cup panko, plus up to ¼ cup more if needed','2 tbsp nutritional yeast','2 tbsp chopped parsley','½ tsp dried oregano','¼ tsp each garlic powder and onion powder','½ tsp fine salt','¼ tsp black pepper'],
       'Vodka sauce':['½ cup raw cashews, soaked in hot water 20 minutes and drained','¾ cup fresh water','1 tbsp olive oil','½ small onion, finely diced','2 garlic cloves, minced','2 tbsp tomato paste','¼ cup vodka','1 can (28 oz) crushed tomatoes','½ cup drained roasted red peppers','1 bay leaf','2 tbsp nutritional yeast','¼ tsp crushed red pepper, or to taste','½ tsp fine salt, then more to taste','1 tsp coconut sugar, optional if tomatoes taste sharp'],
       'Pasta and finishing':['12 oz (340 g) dry rigatoni','3 cups baby spinach, chopped','¼ cup torn basil','1 tbsp chopped chives','Salt for pasta water']},
     steps=[
       'Heat oven to 425°F. Toss eggplant with 1½ tbsp oil, spread on a baking sheet, and roast 25–30 minutes, turning once, until very soft and browned. Let cool enough to handle. Reduce oven to 400°F.',
       'Heat remaining ½ tbsp meatball oil in a skillet. Soften the half onion for 5 minutes, then cook garlic 30 seconds. Pulse this mixture with roasted eggplant and lentils in a food processor until coarsely chopped, not smooth.',
       'Fold in pumpkin, panko, nutritional yeast, parsley, oregano, powders, salt, and pepper. Rest 10 minutes so crumbs hydrate. The mixture should hold a ball when gently squeezed; add extra panko a tablespoon at a time if too wet. Form about 16 balls on a parchment-lined sheet. Bake 25–30 minutes at 400°F until firm and browned; turn carefully after 18 minutes. Let set on the tray for 5 minutes.',
       'Meanwhile, blend drained cashews with ¾ cup fresh water until silky. In a wide saucepan, heat 1 tbsp oil and cook sauce onion for 5 minutes. Add garlic and tomato paste; cook 1–2 minutes. Take pan off the burner before adding measured vodka, then return to medium heat and simmer for 2–3 minutes.',
       'Add tomatoes, roasted peppers, bay leaf, crushed red pepper, and salt. Simmer uncovered 20 minutes, stirring. Remove bay leaf, blend until smooth with an immersion blender, and stir in cashew cream and nutritional yeast. Gently simmer 3–5 minutes. Taste before adding optional sugar.',
       'Boil rigatoni in salted water according to the package until al dente, reserving 1 cup pasta water. Toss pasta and spinach into the sauce over low heat until spinach wilts, adding pasta water as needed. Plate with meatballs on top, then basil and chives. Avoid simmering the soft meatballs in the sauce.'
     ],
     notes='Pumpkin and lentils help bind the eggplant, but moisture varies; the panko adjustment is an estimated home technique. This recipe has not been kitchen-tested. The listed vodka can be omitted and replaced with water for a different, alcohol-free sauce.',
     reheat='For the delivered meal: chop the spinach and stir it into the pasta. Heat without film at 350°F for 8–10 minutes, or microwave with vented film for about 2 minutes, until hot.'),
dict(id='6641', short='Plant-based chorizo chili quesadillas', yield_='4 servings · 4 folded quesadillas', time='About 45 minutes',
     basis='The page names vegan chorizo-and-bean chili, vegan cheddar, gluten-free tortillas, pico de gallo, and chile-lime crema. The ingredient list includes both Impossible meat and vegan chorizo, as well as vegan Parmesan.',
     groups={
       'Chili and quesadillas':['4 large brown-rice or other gluten-free tortillas','4 oz (115 g) plant-based ground meat','4 oz (115 g) vegan chorizo','¾ cup cooked black beans, drained','½ medium onion, diced','2 garlic cloves, minced','1 tbsp tomato paste','¾ cup crushed canned tomatoes','1 tsp minced chipotle in adobo','½ tsp ground cumin','½ tsp Mexican oregano','1 tbsp neutral oil, divided','1 cup shredded vegan cheddar','¼ cup grated vegan Parmesan','Salt and black pepper to taste'],
       'Pico de gallo':['2 plum tomatoes, finely diced','¼ red onion, finely diced','½ jalapeño, minced','¼ serrano pepper, minced, optional for more heat','2 tbsp chopped cilantro','1 tbsp lime juice','¼ tsp fine salt'],
       'Chile-lime crema':['½ cup vegan sour cream','1 tbsp lime juice','½ tsp Tajín','1–2 tsp water if needed']},
     steps=[
       'Combine pico ingredients and set aside. Stir together crema ingredients, thinning with water if needed. Keep both cool while cooking.',
       'Heat 2 tsp oil in a skillet over medium heat. Soften onion for 5 minutes. Add plant-based ground meat and chorizo; crumble and cook according to their package directions until cooked through and browned. Add garlic, tomato paste, chipotle, cumin, and oregano; stir 1 minute.',
       'Add beans and crushed tomatoes. Simmer uncovered for 8–12 minutes until very thick. Mash a few beans to help bind the filling. Taste before adding salt, since the meat substitutes and cheese are seasoned. Let cool 5 minutes.',
       'Warm tortillas briefly so they bend without splitting. Divide cheddar, chili, and Parmesan over one half of each tortilla, leaving a ½-inch border; fold closed.',
       'Wipe the skillet and lightly brush with remaining oil. Cook quesadillas in batches over medium-low heat for about 3–4 minutes per side until crisp and the cheese melts. A lid for the first 1–2 minutes helps melt vegan cheese; uncover to finish crisping.',
       'Rest 2 minutes before cutting. Serve with drained pico and chile-lime crema on the side.'
     ],
     notes='Choose gluten-free tortillas and check the meat substitutes if you want the home version to follow the page’s “No Gluten Added” specification. Component proportions are estimated; the source does not state the ratio of its two meat substitutes.',
     reheat='For the delivered meal: set both sauces aside. Put quesadilla on a baking sheet at 350°F for 13–15 minutes. Alternatively microwave in its vented container for 3–4 minutes, adding 30-second intervals as needed. Serve with the reserved cold sauces.'),
dict(id='9721', short='Penne with spicy pink sauce', yield_='4 servings', time='About 35 minutes',
     basis='The description explicitly says the sauce combines equal parts marinara and Alfredo, with crushed red pepper, grana cheese, and basil. The ingredient label lists American Grana, although the meal title says Grana Padano.',
     groups={
       'Pasta':['12 oz (340 g) dry penne','Salt for pasta water','¼ cup grated Grana Padano or American Grana, for serving','¼ cup torn basil'],
       'Marinara':['1 tbsp olive oil','½ small onion, finely diced','2 garlic cloves, minced','1 can (14–15 oz) crushed tomatoes','½ tsp crushed red pepper, or to taste','¼ tsp fine salt','½ tsp sugar, optional','1 tbsp chopped basil'],
       'Alfredo-style sauce':['2 tbsp butter','1 small shallot, finely minced','1 garlic clove, minced','1 cup heavy cream','½ cup finely grated Grana Padano or American Grana','¼ tsp black pepper']},
     steps=[
       'Put a large pot of salted water on to boil. For marinara, heat oil in a saucepan over medium heat. Soften onion for 5–6 minutes; add garlic and red pepper and stir 30 seconds. Add tomatoes and salt, then simmer uncovered 15–20 minutes. Stir in basil. Add sugar only if the sauce tastes too acidic.',
       'For the white sauce, melt butter over medium-low heat in a second saucepan. Cook shallot 3–4 minutes without browning. Add garlic for 30 seconds, then cream. Simmer gently for 3–5 minutes until slightly thickened. Remove from heat and gradually stir in ½ cup grated cheese and black pepper.',
       'Measure equal volumes of red and white sauce into a wide skillet, starting with 1¼ cups of each. If one sauce yields less, use that amount of each; reserve any excess separately. This preserves the page’s stated equal-parts approach despite variation in evaporation.',
       'Cook penne until al dente according to its package. Reserve 1 cup pasta water before draining. Toss pasta with the combined sauce over low heat for 1–2 minutes, adding pasta water a little at a time until glossy and loose enough to coat each piece. Avoid boiling hard after the cheese goes in.',
       'Taste and adjust salt and chili. Divide among bowls, then finish with the reserved ¼ cup cheese and fresh basil.'
     ],
     notes='Equal red/white sauce proportions are stated by CookUnity; ingredient amounts and sauce preparation here are estimated. If vegetarian rennet matters to you, select a grana-style cheese explicitly labeled accordingly.',
     reheat='For the delivered meal: keep the cheese cup aside. Cover with foil and heat at 350°F for 12–15 minutes, stirring halfway. Or microwave with vented film for 2–3 minutes, stirring halfway. Add cheese after heating.'),
dict(id='12797', short='Hearts of palm quinoa salad with cucumber dressing', yield_='4 servings', time='About 50 minutes, plus cooling',
     basis='The page describes ponzu-marinated quinoa, hearts of palm, tomatoes, cucumber, crisp fried quinoa, and cucumber-tofu dressing. The label also includes edamame, black beans, vegan feta, lettuce, mint, yuzu, kombu, and shiitake.',
     groups={
       'Salad':['¾ cup dry tri-color quinoa, rinsed','1½ cups water','1 can (14 oz) hearts of palm, drained and sliced','1 cup shelled edamame, cooked according to package and cooled','1 cup canned black beans, drained and rinsed','1 cup halved cherry tomatoes','1 cup diced cucumber','2 cups shredded iceberg lettuce','½ cup crumbled vegan feta','2 tbsp chopped mint'],
       'Estimated vegan ponzu':['¼ cup water','1 small dried shiitake mushroom','1 small piece kombu, about 2 inches square','2 tbsp light soy sauce','2 tbsp yuzu juice; lemon juice is a home substitution','1 tbsp mirin','1 tbsp seasoned rice vinegar'],
       'Cucumber-tofu dressing':['½ cup silken tofu, drained','½ cup chopped cucumber','3 tbsp vegan mayonnaise','1 tbsp white vinegar','1 tsp yellow mustard','1 small garlic clove','1 tbsp mint leaves','⅛ tsp ground cumin','Salt and black pepper to taste'],
       'Crisp quinoa topping':['½ cup of the cooked quinoa above','2 tsp neutral oil (home addition; the page does not identify a frying oil)']},
     steps=[
       'Cook quinoa with 1½ cups water: bring to a boil, cover, and simmer gently about 15 minutes until absorbed. Rest off heat, covered, for 5 minutes. Fluff, reserve ½ cup for the topping, and spread the rest on a tray to cool.',
       'For ponzu, soak shiitake and kombu in ¼ cup hot water for 15 minutes. Remove solids. Combine infused water and mirin in a small saucepan; simmer 2 minutes. Cool, then add soy sauce, yuzu, and rice vinegar. This is an estimated shortcut, not the chef’s published formula.',
       'Pat the reserved ½ cup cooked quinoa very dry on paper towels. Warm 2 tsp oil in a nonstick skillet over medium heat. Spread quinoa in a thin layer and cook, stirring periodically, for 8–12 minutes until dry and crisp. Lower heat if it browns too quickly. Cool on a plate.',
       'Blend tofu, dressing cucumber, vegan mayonnaise, white vinegar, mustard, garlic, mint, and cumin until smooth. Taste and add salt and pepper. If thin from a watery cucumber, chill before using; if too thick, add water a teaspoon at a time.',
       'Toss the cooled salad quinoa with 3 tbsp ponzu to start. Add more to taste, a tablespoon at a time, stopping before it becomes wet or overly salty; reserve any remaining ponzu.',
       'Arrange lettuce in four bowls. Divide quinoa, hearts of palm, edamame, black beans, tomatoes, and diced cucumber among them. Add feta and mint, drizzle with cucumber dressing, and add crisp quinoa just before eating.'
     ],
     notes='The source does not assign every seasoning to a component. Ponzu, dressing ratios, and the skillet method for crisp quinoa are reconstructions. The listed soy sauce contains wheat. Lemon in place of yuzu and oil for the topping are explicitly identified home choices.',
     reheat='The delivered salad is intended to be served chilled: remove packaging and the sauce cup, then add dressing. The page gives no heating step.'),
dict(id='10053', short='Mexican tofu burrito bowl with avocado sauce', yield_='4 servings', time='About 50 minutes, plus 15 minutes to press tofu',
     basis='The description names baked seasoned tofu, roasted peppers and corn, rice, black beans, and creamy avocado sauce. The label includes lemon juice, brown sugar, sriracha, cornstarch, chili powder, garlic powder, and onion powder.',
     groups={
       'Tofu':['14 oz (400 g) extra-firm tofu, drained and pressed 15 minutes','1 tbsp olive oil','1 tbsp cornstarch','1 tsp chili powder','½ tsp garlic powder','½ tsp onion powder','½ tsp fine salt','1 tbsp sriracha','2 tsp light brown sugar','1 tbsp lemon juice'],
       'Rice, beans, and vegetables':['¾ cup dry basmati rice, rinsed','1½ cups water, or amount specified by the rice package','1 can (15 oz) black beans, drained and rinsed','1 red bell pepper, sliced','1 yellow bell pepper, sliced','1 cup drained canned corn','1 tbsp olive oil','¼ tsp fine salt','¼ cup chopped cilantro'],
       'Avocado sauce':['1 large ripe avocado','2 tbsp lemon juice','¼ cup water, plus more to thin','2 tbsp cilantro','¼ tsp garlic powder','¼ tsp fine salt']},
     steps=[
       'Heat oven to 425°F. Cut pressed tofu into ¾-inch cubes and pat dry. Toss with 1 tbsp oil, cornstarch, chili powder, garlic powder, onion powder, and ½ tsp salt. Spread on a parchment-lined sheet with space between pieces.',
       'Toss peppers and corn with their oil and ¼ tsp salt on a separate sheet. Roast tofu for 25–30 minutes, turning halfway; roast vegetables for 20–25 minutes, stirring once, until tender with browned edges.',
       'Meanwhile, cook rice with its water according to package directions. Rest covered 5 minutes, then fluff. Warm beans in a small saucepan with 2 tbsp water for 4–5 minutes and drain excess liquid.',
       'Mix sriracha, brown sugar, and 1 tbsp lemon juice. Toss the browned tofu with this glaze and return to the oven for 3–5 minutes, just until it clings. Watch closely so the sugar does not burn.',
       'Blend avocado with 2 tbsp lemon juice, ¼ cup water, cilantro, garlic powder, and salt until creamy. Add water a tablespoon at a time until spoonable.',
       'Divide rice and beans among four bowls; add roasted vegetables and tofu. Finish with cilantro and avocado sauce.'
     ],
     notes='The glaze is inferred from the listed sriracha, sugar, and lemon; the page does not say how they are used. Lemon follows the ingredient label. Quantities are estimated and do not reproduce the published packaged-meal nutrition.',
     reheat='For the delivered meal: reserve the sauce. Heat at 350°F for 12–15 minutes with film removed, or microwave with vented film for 2–3 minutes. Add avocado sauce after heating.'),
dict(id='12845', short='Fettuccine with lentil bolognese', yield_='4 servings', time='About 65 minutes using dry lentils; about 40 with cooked lentils',
     basis='The page describes lentils simmered in a tomato-pepper sauce, fettuccine, feta, and parsley. The ingredient label includes brown lentils, red pepper, white wine, paprika, oregano, and bay leaf.',
     groups={
       'Lentil sauce':['¾ cup dry brown lentils, rinsed and checked, or about 2 cups cooked lentils','3 cups water for cooking dry lentils, plus more if needed','2 tbsp olive oil','1 medium onion, finely diced','1 red bell pepper, finely diced','3 garlic cloves, minced','2 tbsp tomato paste','⅓ cup dry white wine','1 can (28 oz) crushed tomatoes','1 tsp sweet paprika','½ tsp dried oregano','¼ tsp chili powder','1 bay leaf','½ tsp fine salt, then more to taste','¼ tsp black pepper','½–1 cup water as needed for the sauce'],
       'Pasta and finishing':['12 oz (340 g) dry fettuccine','½ cup crumbled feta','¼ cup chopped parsley','Salt for pasta water']},
     steps=[
       'If using dry lentils, place them in a saucepan with 3 cups water. Bring to a boil, then simmer gently for 20–30 minutes until tender but intact, adding water to keep them submerged. Drain. If using cooked lentils, drain and proceed.',
       'Heat oil in a wide, deep skillet over medium heat. Cook onion and red pepper for 8–10 minutes until softened. Add garlic, tomato paste, paprika, oregano, and chili powder; stir for 1–2 minutes.',
       'Pour in wine and simmer 2–3 minutes, scraping the bottom. Add tomatoes, cooked lentils, bay leaf, salt, pepper, and ½ cup water. Simmer uncovered for 20–25 minutes, stirring occasionally, until thick and spoon-coating. Add more water if needed to prevent sticking.',
       'Mash roughly one quarter of the lentils against the pan with a spoon for a thicker texture, leaving most intact. Remove bay leaf and taste for salt.',
       'Cook fettuccine in salted water according to package directions. Reserve 1 cup pasta water, then drain. Toss pasta with the sauce over low heat, adding pasta water in small splashes until it coats the noodles evenly.',
       'Divide among bowls and finish with feta and parsley.'
     ],
     notes='The page’s description calls this vegan, but its label explicitly lists dairy feta and milk as an allergen, and its specification says vegetarian. This reconstruction uses dairy feta to follow the label. To make a vegan adaptation, use vegan feta and confirm the pasta and wine suit that preference.',
     reheat='For the delivered meal: reserve the cheese. Cover the tray with foil and heat at 350°F for 12–15 minutes, stirring halfway. Or microwave with vented film for 2–3 minutes, stirring halfway. Add cheese at the end.'),
dict(id='1450', short='Superfood bowl with sweet potato, quinoa & black beans', yield_='4 servings', time='About 45 minutes, plus cooling if serving chilled',
     basis='The page describes sweet potato, quinoa, black beans, herbs, and a zesty sauce. The label specifies tomato, spinach, pumpkin seeds, white balsamic vinegar, onions, jalapeño, cilantro, chili powder, and cumin.',
     groups={
       'Bowl':['2 medium sweet potatoes, about 1 lb (450 g), peeled and cut into ¾-inch cubes','¾ cup dry tri-color quinoa, rinsed','1½ cups water','1 can (15 oz) black beans, drained and rinsed','3 plum tomatoes, diced','3 cups baby spinach','½ small yellow onion, finely diced','¼ red onion, finely diced','¼ cup pumpkin seeds','2 tbsp olive oil, divided','1 tsp chili powder','½ tsp ground cumin','½ tsp fine salt','¼ tsp black pepper'],
       'Estimated cilantro–white balsamic dressing':['3 tbsp olive oil','2 tbsp white balsamic vinegar','¼ cup cilantro leaves','½ jalapeño, seeded for less heat','2 tbsp water','¼ tsp ground cumin','¼ tsp fine salt']},
     steps=[
       'Heat oven to 425°F. Toss sweet potato with 1 tbsp oil, chili powder, ½ tsp cumin, ½ tsp salt, and pepper. Spread on a baking sheet and roast 25–30 minutes, turning halfway, until browned and tender in the center.',
       'Bring quinoa and 1½ cups water to a boil. Cover, reduce heat, and simmer about 15 minutes until water is absorbed. Rest off heat 5 minutes, then fluff.',
       'Heat remaining 1 tbsp bowl oil in a small skillet. Soften yellow onion for 4–5 minutes. Add beans and 2 tbsp water and cook 3–4 minutes until warm and most liquid has evaporated.',
       'Toast pumpkin seeds in a dry skillet over medium-low heat for 2–4 minutes, stirring until fragrant. Remove from the pan immediately.',
       'Blend dressing ingredients until cilantro and jalapeño are finely chopped. Taste and adjust vinegar, salt, or water for a bright, pourable sauce. Its identity and proportions are inferred from the label.',
       'For a chilled bowl like the delivered meal, spread cooked components in shallow containers and refrigerate promptly until cool. Divide spinach among four bowls, then add quinoa, sweet potato, beans, tomatoes, and red onion. Spoon on dressing and finish with pumpkin seeds. You may also assemble with freshly cooked warm components for a home variation.'
     ],
     notes='The page does not identify the zesty sauce by name or supply a formula. The cilantro–white balsamic dressing is a proposed reconstruction based on the listed ingredients.',
     reheat='The delivered bowl’s instructions call for removing packaging and adding sauce, with no heating step.')
]

recipes.extend(additional_recipes)
for recipe in recipes:
    recipe['source'] = sources[recipe['id']]
    if recipe['id'] in photos:
        recipe['photo'] = photos[recipe['id']]

intro = (f'{len(recipes)} meals collected from your open CookUnity tabs on September 8 and 10, 2026. '
         'The pages provide ingredient labels, meal descriptions, nutrition, and directions for reheating prepared meals. '
         'They do not provide ingredient quantities or recipes for cooking from scratch. '
         'Every home recipe below is an original, untested reconstruction: its quantities, yields, cooking times, '
         'component assignments, and methods are estimates unless explicitly identified as a page detail. '
         'Published nutrition describes the delivered meal only, not these home recipes. '
         'US cups and spoons are used; oven temperatures are Fahrenheit. Salt amounts refer to fine salt.')

md = ['# CookUnity meal collection', '', intro, '', '## Contents', '']
for i, r in enumerate(recipes, 1):
    md.append(f'{i}. [{r["short"]}](#meal-{r["id"]})')
for r in recipes:
    s = r['source']; n = s['nutrition']
    md.extend(['', f'<a id="meal-{r["id"]}"></a>', f'## {s["title"]}', '',
               f'Chef: **{s["chef"]}** · [CookUnity source]({s["url"]})', '',
               *([f'![{s["title"]}]({r["photo"]["path"]})', '', 'Photo from the CookUnity meal listing; the home recipe below is a reconstruction.', ''] if r.get('photo') else []),
               '**What the page establishes:** ' + r['basis'], '',
               '**Published ingredient names** (commercial subingredients omitted; duplicates removed): ' + '; '.join(s['ingredients']) + '.', '',
               f'**Delivered-meal nutrition:** {n["portion_g"]} g portion; {n["calories"]} kcal; {n["protein_g"]} g protein; {n["carbs_g"]} g carbohydrate; {n["fat_g"]} g fat; {n["sugar_g"]} g sugar.', '',
               '**Page allergen statement:** ' + s['allergens'], '',
               '### Estimated home recipe — not a published chef recipe', '',
               f'**Yield:** {r["yield_"]} · **Time:** {r["time"]}', ''])
    for name, items in r['groups'].items():
        md.extend([f'**{name}**', ''] + ['- ' + x for x in items] + [''])
    md.extend(['**Method**', ''] + [f'{i}. {x}' for i,x in enumerate(r['steps'],1)])
    md.extend(['', '**Recipe notes:** ' + r['notes'], '', '**Published reheating directions, paraphrased:** ' + r['reheat'], ''])

md.extend(['## Source and preparation notes', '',
           'The complete ingredient-label text, including commercial subingredients, is preserved in `source-details.json`. '
           'Cooking directions above are independently written. Reheating directions apply to the original delivered meals; '
           'their short heating times should not be used as from-scratch cooking times. '
           'CookUnity gives a shared-facility notice for milk, eggs, fish, shellfish, tree nuts, peanuts, wheat/gluten, soy, and sesame. '
           'Ingredient labels on the products you buy govern your home version.'])
(OUT/'recipes.md').write_text('\n'.join(md))
(OUT/'source-details.json').write_text(json.dumps(list(sources.values()), ensure_ascii=False, indent=2))
(OUT/'recipes.json').write_text(json.dumps(recipes, ensure_ascii=False, indent=2))

e = html.escape
cards=[]
for index,r in enumerate(recipes,1):
    s=r['source']; n=s['nutrition']
    photo = (f'<figure class="meal-photo"><img src="{e(r["photo"]["path"])}" alt="{e(s["title"])}" decoding="async"><figcaption>CookUnity meal photo · home recipe below is a reconstruction</figcaption></figure>' if r.get('photo') else '')
    groups=''.join(f'<div class="ingredient-group"><h4>{e(name)}</h4><ul>'+''.join(f'<li>{e(x)}</li>' for x in items)+'</ul></div>' for name,items in r['groups'].items())
    steps=''.join(f'<li>{e(x)}</li>' for x in r['steps'])
    cards.append(f'''<article id="meal-{r['id']}"><div class="eyebrow">MEAL {index:02d} · {e(s['chef'])}</div>
    <h2>{e(s['title'])}</h2><a href="{e(s['url'])}" target="_blank" rel="noopener">Open CookUnity source ↗</a>
    {photo}
    <p>{e(r['basis'])}</p>
    <details><summary>Published ingredients, nutrition &amp; allergens</summary>
    <p>{e('; '.join(s['ingredients']))}</p><p class="muted">Commercial subingredients omitted here; the full ingredient label is in source-details.json.</p>
    <p><b>Delivered meal:</b> {n['portion_g']} g · {n['calories']} kcal · {n['protein_g']} g protein · {n['carbs_g']} g carbs · {n['fat_g']} g fat · {n['sugar_g']} g sugar</p>
    <p>{e(s['allergens'])}</p></details>
    <h3>Estimated home recipe</h3><p class="muted">Original, untested reconstruction; quantities and methods are estimates.</p>
    <div class="meta"><span>{e(r['yield_'])}</span><span>{e(r['time'])}</span></div>
    <div class="ingredients">{groups}</div><h3>Method</h3><ol>{steps}</ol>
    <p class="note"><b>Recipe notes:</b> {e(r['notes'])}</p>
    <details><summary>CookUnity reheating directions, paraphrased</summary><p>{e(r['reheat'])}</p></details>
    <a class="back" href="#top">Back to contents ↑</a></article>''')
toc=''.join(f'<a href="#meal-{r["id"]}"><span>{i:02d}</span>{e(r["short"])}</a>' for i,r in enumerate(recipes,1))
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CookUnity · Nine home recipe reconstructions</title>
<style>
:root{--ink:#23352d;--muted:#627066;--paper:#faf8f2;--line:#d9dfd6;--green:#315d47}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,sans-serif}main{max-width:1000px;margin:auto;padding:56px 26px}h1,h2{font-family:Georgia,serif;line-height:1.15;letter-spacing:-.025em}h1{font-size:clamp(38px,6vw,64px);max-width:750px;margin:12px 0 24px}h2{font-size:34px;margin:12px 0}h3{margin:30px 0 4px;font-size:22px}h4{margin:18px 0 8px;font-size:16px}.eyebrow{font-size:12px;font-weight:700;letter-spacing:.12em;color:var(--green)}a{color:var(--green);text-underline-offset:3px}header>p{max-width:850px}.muted{color:var(--muted);font-size:14px}.toolbar{display:flex;gap:20px;align-items:center;margin:24px 0}button{background:var(--green);color:white;border:0;border-radius:8px;padding:11px 18px;font:inherit;cursor:pointer}nav{display:grid;grid-template-columns:1fr 1fr;gap:0 28px;margin:26px 0 54px}nav a{display:flex;gap:14px;text-decoration:none;border-bottom:1px solid var(--line);padding:13px 0}nav span{color:var(--muted);font-size:13px;padding-top:3px}article{background:#fff;border:1px solid var(--line);border-radius:14px;padding:32px;margin:28px 0;scroll-margin-top:18px}.meta{display:flex;flex-wrap:wrap;gap:10px 22px;border-block:1px solid var(--line);padding:12px 0;margin:18px 0;font-weight:600;font-size:14px}.ingredients{display:grid;grid-template-columns:1fr 1fr;gap:0 32px}ul,ol{padding-left:23px}li{padding-left:3px;margin:7px 0}ol li{margin:14px 0}details{background:#f4f6f1;border-radius:8px;padding:12px 16px;margin:18px 0}summary{cursor:pointer;font-weight:600}.note{border-left:3px solid #afbd9b;padding:10px 18px;background:#fafbf7}.back{font-size:13px}footer{font-size:14px;color:var(--muted)}@media(max-width:650px){main{padding:30px 16px}article{padding:23px 19px}.ingredients,nav{grid-template-columns:1fr}h2{font-size:29px}}@media print{body{background:#fff;font-size:11pt}main{max-width:none;padding:0}.toolbar,.back{display:none}article{border:0;border-radius:0;padding:0;margin:0;break-before:page}h2{font-size:25pt}h3,h4{break-after:avoid}li,.ingredient-group,.note{break-inside:avoid}nav{margin:20px 0}a{color:inherit}details{background:none;padding:0}.meta{font-size:10pt}.ingredients{gap:0 22px}}
</style></head><body><main id="top"><header><div class="eyebrow">YOUR CHROME TABS · SEPTEMBER 8, 2026</div><h1>Nine meals.<br>A home cooking collection.</h1><p>'''+e(intro)+'''</p><div class="toolbar"><button onclick="window.print()">Print / Save PDF</button><a href="recipes.md">Markdown recipes</a><a href="source-details.json">Source details</a></div></header><nav aria-label="Recipe contents">'''+toc+'</nav>'+''.join(cards)+'''<footer><p>CookUnity provides a shared-facility notice covering milk, eggs, fish, shellfish, tree nuts, peanuts, wheat/gluten, soy, and sesame. Check the ingredient labels of the products you use at home.</p><p>Source nutrition is for the delivered meals. These home recipes have not been kitchen-tested or nutritionally analyzed.</p></footer></main><script>let wasOpen=[];addEventListener('beforeprint',()=>{wasOpen=[...document.querySelectorAll('details')].map(d=>d.open);document.querySelectorAll('details').forEach(d=>d.open=true)});addEventListener('afterprint',()=>document.querySelectorAll('details').forEach((d,i)=>d.open=wasOpen[i]));</script></body></html>'''
page = page.replace('Nine home recipe reconstructions', f'{len(recipes)} home recipe reconstructions')
page = page.replace('Nine meals.', f'{len(recipes)} meals.')
page = page.replace('YOUR CHROME TABS · SEPTEMBER 8, 2026', 'YOUR CHROME TABS · UPDATED SEPTEMBER 10, 2026')
page = page.replace('</style>', '''
.meal-photo{margin:24px 0}.meal-photo img{display:block;width:100%;max-height:430px;object-fit:contain;background:#fafaf8;border-radius:10px}.meal-photo figcaption{font-size:12px;color:var(--muted);margin-top:7px}.toolbar{flex-wrap:wrap}
@media print{.meal-photo{break-inside:avoid;margin:12px 0}.meal-photo img{max-height:230px}.meal-photo figcaption{font-size:9pt}}
</style>''')
(OUT/'index.html').write_text(page)
assert len(recipes)==len(sources)
assert len({r['id'] for r in recipes})==len(recipes)
for r in recipes:
    assert r['steps'] and r['groups'] and r['source']['ingredients']
print(f'Created {len(recipes)} recipes in {OUT}')
print(f'Markdown: {len((OUT/"recipes.md").read_text().split())} words')
