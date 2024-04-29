# GW2 Data collection - Heavy Loot Bag 

This is the repository for the CSV files for the data on Heavy Loot Bags (AKA WvW bags). 

Original post from Reddit: https://redd.it/1ce1uld

## The spreadsheet

**Link to spreadsheet:** https://docs.google.com/spreadsheets/d/1sNC-4Bs3MWOUsGC4tn1moyBh3Zy-yK5LwzDBFLqSMTM/edit?usp=sharing

The spreadsheet is divided into 3 tabs:

* **Summary:** If you just want to see the conclusions, this is the page you're looking for. It lists the profit per bag from directly selling the contents in the TP, and the savings per bag from using the materials instead of buying them from the TP. It also breaks down the value further into material types and specific materials.
* **Raw Data:** This is where the results from individual openings are. I'll be making the CSV files available soon, as well as a Python script to compile them into a single file. 
* **Data Statistics:** Some measures for the statistics nerds, like confidence intervals and such. It should show how ~~overkill~~ good the samples are.

I will make it available in a .xlsx file as well in the future (as soon as I'm able to upgrade from Excel 2016 to a newer version).

## Compiling the data

In oder to make the data importing less painful, I've also made the `CompileData.py` script. It will read the individual CSV files and output a single CSV file with the raw data. You can paste the data in your local copy of the spreadsheet in the "Raw Data" tab (be sure to divide the data in columns). 

Please note that you need to have [Python](https://www.python.org/) installed with the `numpy`, `pandas` and `os` modules. This script was also developed for Windows; I haven't tested it for Linux yet. 

## Data collection

Well, data collection was pretty simple: I bought a bunch of bags, cleared the inventory of one character and opened them. Then I used https://datawars2.ie/ to fetch the item list via CSV. 

**Important disclaimer:** Unfortunately, I was already finishing the drop rate collection when I realized that those CSVs didn't have the coins that the bags drop. However, since the coppers make for only ~1% of the bag value at most, values shouldn't change much. If anything, TP price fluctuations should matter more than these coppers. 

"You should have used https://drf.rs/ to record the data, it should be more accurate!!" Yeah, it's generally better. But it leads to bigger files and more work to process them. Moreover I didn't have it when I collected most of the data :P

## So what about it?

**Disclaimer:** Those are the conclusions taken at 26/04/2024. They may change in the future as prices fluctuate.

1. **It's almost always worth opening the bags instead of selling, even at sell price.** Generally if you're selling everything, you'll break even. But if you're using even some of the basic materials, you'll be profiting. Moreover, you can always upgrade some of the T5 trophies to T6 (but check profits first).

2. **T6 trophies are by far the most valuable drops.** At current prices, T6 trophies make for almost 70% of the bag value. So if you need T6 trophies for things like legendaries, open the bags instead of selling!

3. **Cores and lodestones have negligible impact.** I was genuinely surprised how little they drop. So yeah, get them from other sources.

4. **500k+ bags were way overkill of a sample.** From my calculations, I managed to have a very narrow 99% confidence interval in the bag value. Even for items with low drop rate, their overall impact is quite small. I think I could have been happy with like 60% of the data or so. ~~I totally didn't lose the CSV files at some point and found them again after gathering more data~~

## Conclusion

So this is the first dataset I've released, and I plan to make it as a kind of a template for any future datasets. So please let me know if you have any suggestion about what to add, change or remove in the future. 

Shoutout to the veterans of Overflow Discord where I learned quite a bit (I hope I didn't do them dirty). Also shoutout to Zanar, Shinymeta and Selici for their inspiring data projects.
