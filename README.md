# MSDS460
# MSDS460
# Northwestern University MSDS
MSDS 460 Class Assignment 1
# Abstract
“The diet problem is a classic problem used as an introduction to linear programming” (Miller, 2023). The diet problem was personalized by asking students to choose foods they would normally consume. Five packaged foods were chosen, price per serving and nutrition information was documented. The objective was to satisfy a minimum cost per serving while comprising a diet containing the recommended dietary allowances.
# Methodology
The current recommended daily dietary allowances from the U.S. Food and Drug Administration were applied as constraints to the diet chosen from 5 packaged foods (Food and Drug Administration, Department of Health and Human Services. 2016). The following five packaged foods were chosen: Kind blueberry almond break- fast bars, 2 percent milk, 365 turkey lunch meat, Bertolli’s Traditional Marinara Sauce, Trader Joe’s whole wheat pasta noodles. Price per serving was then calculated.1 Variables were set as follows: r = Kind breakfast bars, m = milk, t = turkey lunch meat, s = pastas sauce, p = pasta noodles. Using the calculated cost per serv- ing.2 The objective function, z = 1.08r + .42m + 1.83t + .66s + .25p, describes the servings per unit cost of each food item. The constraints of recommended daily values were applied to the variables as follow:
0r + 120m + 470t + 490s + 0p<= 5000 (sodium in each food)
210r + 120m + 60t + 80s + 200p >= 2000 (calories)
0r + 2.1m + 0t +0s + 0p >= 20 (vitamin D)
3r + 8m + 12t + 2s + 7p >= 50 (protein)
26r + 300m + 0t + 20s + 0p >= 1300 (calcium)
2.16r + 0m + .7t + .5s +.9p >= 18 (iron)
94r + 350m + 0t + 440s + 140*p >= 4700 (potassium)

Results revealed that one would need to eat 9.5238095 milk servings (about 10 cups of milk) and 20 servings of pasta (2.5 cups of pasta) with a minimal cost of 5 dollars each day. This result did not change with the additional constraints of vitamin B6 and vitamin A. The calculations were run using Python PuLP, a .py text file can be found in a Github repository, https://github.com/hheid-huc/MSDS460/tree/main.

The repository has two files, one without the additional nutrition constraints, one with the additional nutrition constraints.

1.	See Appendix A for label details.
2.	See Appendix B for cost per serving.
# Research
Due to the maximization or minimization nature of this objective this problem is a single objective solution (Williams, 2013). Marginal costs, which represent the price per serving, were calculated based on the additional costs incurred to adjust serving sizes to meet the minimum or maximum nutrition constraints (Williams, 2013). A case study, A Blending Problem, provides an in depth look at setting up the Python coding using LPproblem function in the PuLP package (https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html, 2009). 
Though no longer required to be included on nutrition labels, vitamin A and vitamin B6 provide health benefits for primary body function, vitamin A is assists in healthy eye function and vitamin B6 is responsible for healthy nervous system function.  (https://my.clevelandclinic.org/health/diseases/23107-vitamin-a-deficiency, 2022) (https://www.hsph.harvard.edu/nutritionsource/vitamin-b6/, 2023).
Information for the additional nutrients were not located on the food packages, nutrition references were found online. Kind breakfast bars contain 0 mg of vitamin B6 and 0 mcg of vitamin A (https://www.nutritionix.com/i/kind-breakfast/bars-blueberry-almond/55e3518fa2630bff23a571a8, 2023). Milk contains .1 mg of vitamin B6, 150 mcg vitamin A (http://milkfacts.info/Nutrition%20Facts/Nutrient%20Content.htm, 2023). Turkey contains .4mg of per serving of vitamin B6, 0 of vitamin A (O’Brien, 2023). Marina pasta sauce contains 0 mg of vitamin B6, 34 mg of vitamin A (https://mobile.fatsecret.com/calories-nutrition/food/pasta-sauce/vitamins, 2023). Whole wheat pasta contains .28 mg of vitamin B6, 1.14 mg vitamin A (https://vegnt.com/foods/pasta_whole-wheat_dry.html, 2023). 
# Bibliography
Miller, W. Thomas. “Homework Assignment:1 Liner Programming Example—The Diet Problem.” 2023. https://canvas.northwestern.edu/courses/200718/assignments/1276264

Food and Drug Administration, Department of Health and Human Services.“Food  Labeling: Revision of the Nutrition and Supplemental Facts Labels”.2016. https://s3.amazonaws.com/public-inspection.federalregister.gov/2016-11867.pdf

Williams, H. Paul. 2013. “Model Building in Mathematical Programming” (fifth ed.). New York:	Wiley.

Github.com, A case study. “A Blending Problem.”2009. Last modified 2009. https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html

Cleveland Clinic. 2002. “Vitamin A Deficiency.”2023. https://my.clevelandclinic.org/health/diseases/23107-vitamin-a-deficiency

Harvard School of Public Health. “The Nutrition Source, Vitamin B6.”2023
	https://www.hsph.harvard.edu/nutritionsource/vitamin-b6/

Nutritionix, A Syndigo Company. “Bars, Blueberry Almond” 2022. https://www.nutritionix.com/i/kind-breakfast/bars-blueberry-almond/55e3518fa2630bff23a571a8

Milkfacts.info. “Nutrient Content of Milk Varieties.” 2023. http://milkfacts.info/Nutrition%20Facts/Nutrient%20Content.htm

Healthline.com. “All You Need to Know About Turkey Meat.” 2023.
	https://www.healthline.com/nutrition/turkey

Fatsecrets.com. “Vitamins in Pasta Sauce.” 2023.
	https://www.fatsecret.com/calories-nutrition/food/pasta-sauce/vitamins

Vegnt.com. “Food Info, Whole Wheat Pasta.” 2023.
	https://vegnt.com/foods/pasta_whole-wheat_dry.html
# Appendix A
![Alt text](https://i5.walmartimages.com/seo/KIND-Breakfast-Healthy-Snack-Bar-Blueberry-Almond-Gluten-Free-Breakfast-Bars-100-Whole-Grains-1-76-OZ-Packs-6-Count_dddaabcd-a083-4d02-a316-3aa94d215c83.12c0dfd314aae3db784ac57e7f2d24f0.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF)
Nutrition information: Kind Bluberry Almond Breakfast Bars

![Alt text](https://target.scene7.com/is/image/Target/GUEST_68940f13-7d78-4563-b983-a948e9085749)
Nutrition Information: 
2% Good Gather Milk

![Alt text](https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/634887fb58d7ce0458bc86d0_0099482482022-glamor-front-2022-09-02t17-01-26-iphone-7-quality-90-1-31-0-user-5d7652c1db2c4b51d4c666ca-zps0-652901._FMwebp__SR300,300__TTD_.jpg)
Nutrition Information:
365 Turkey Lunch Meat

![Alt text](https://target.scene7.com/is/image/Target/GUEST_38bf8b9b-ac93-4d20-8144-2a6052f221b1?wid=400&hei=400&qlt=80&fmt=webp)
Nutrition Information:
Bertolli's Traditional Marinara Sauce

![Alt text](https://m.media-amazon.com/images/I/816QueXXD2L._SX679_.jpg)
Nutrition Information:
Trader Joe's Whole Wheat Pasta

# Appendix B
Nutrition Information and Price per Serving

| Packaged Food| Sodium < = 5000mg| Cal >= 2000 | Protein >= 50g | Vitamin D >= 20mcg | Calcium >= 1300mg| Iron >= 18mg | Potassium >= 4700 mg| Vitamin B6 >= 1.7mg | Vitamin  A >= 900mcg |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|
| Kind Breakfast Bars (2 bars per serving) $1.08 | 20 | 210 | 3| 0 | 26 | 2.16| 94|0 | 0|
|2% Milk (1c serving) $.42 | 120|120 |8| 2.1 | 300| 0 | 350| .1| 150|
| Turkey (5 slices serving) $1.83  |470| 60| 12| 0 | 0 | .7 | 0 | .4| 0 |
|Pasta Sauce (1/2c serving) $.66  | 490| 80| 2 | 0 |20| .5| 440 | 0| 34|
|Whole Wheat Pasta (1/8c  servings) $.25| 0| 200 |7| 0 |0 |.9| 140 | .28| 1.41|
