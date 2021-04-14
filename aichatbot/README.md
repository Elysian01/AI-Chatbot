<!---
## List of Functions and Class In Auto EDA.
-->

### An Automated Exploratory Data Analysis Library For Machine Learning and Deep Learning in Python.

## Steps in Auto EDA

- [x] 1. **Shape** of dataset
- [x] 2. **Sample** of dataset
- [x] 3. **Number of categorical and numerical** attributes
- [x] 4. **Null values** in the dataset (number & %) => recommend to drop higher %
- [x] 5. **Value count** of attribute (unique) in the dataset
- [ ] 6. **Describe** the data (5 point summary) => inference (min, max, dist) => recommend columns to watch out for => outliers.
- [ ] 7. **Distribution** of dataset
        a. Skewed or Normal
- [ ] 8. Perform **grouping/aggregation** wherever necessary 
- [ ] 9. **Recommend Columns** or attribute to remove
        a. Column with all value as unique (e.g: ID)
- [ ] 10. Give **insight from the data** and suggest ml algorithms, techniques, cleaning, etc hints, tips and tricks
- [x] 11. **Correlation** matrix (Heatmap)
- [ ] 12. **Distribution Plot**
- [x] 13. Joint Plot 
- [x] 14. Pair plot
- [x] 15. Pie Chart
- [ ] 16. Box or Violen plot

## Steps in NLP EDA

- [ ] EDA for NLP (https://towardsdatascience.com/exploratory-data-analysis-for-natural-language-processing-ff0046ab3571)
- [ ] Model For Sentiment Analysis
- [ ] Model For finding absuive words
- [ ] Word Frequency Analysis
        

## Points to Remember & Small Tasks

- [ ] Always write and keep track of inferences from all the steps.
- [ ] Divide into functions and classes
- [ ] Plots should be interactive (plotly)
- [ ] Params to Functions
  - [ ] Can choose to show outputs/data while performing EDA 
  - [ ] Display all columns (True or False)


## TODO

- [ ] Summary of EDA (Append all the inference of each step) => autoeda.summary()
- [ ] Test on atleast 50 dataset before publishing.
- [ ] Display the outputs using `termcolor`
- [ ] Release the beta version to 15 testers
- [ ] Test the library for jupyter and spyder IDE
- [ ] Performing all operations/steps column-wise
- [ ] Instead of performing all EDA, option to perform `basic` EDA (given as parameter to constructor)
- [ ] user can access special class variables which are set after analysis (like mleda.cat_columns)
