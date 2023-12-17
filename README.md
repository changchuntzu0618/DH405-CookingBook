# Digitalizing a Chinese Cooking Book: YingShanZhengYao(飲膳正要)
## Introduction
This project is part of the DH405 Digital Humanities course and aims to digitize an Ancient Chinese Cookbook and medical text known as [**YinShanZhengYao**](https://en.wikipedia.org/wiki/Yinshan_zhengyao). Published in 1330, this text holds significant cultural importance in the field of Chinese medical technology. The project involves tasks such as data collection, data processing, data analysis, and the construction of a web platform.

## Data collection - Data_Crawling.ipynb
We obtained the recipe text from the [Chinese Text Project](https://ctext.org/) website. To collect the required recipe data, we conducted data crawling, and the corresponding code is available in the 'Data_Crawling.ipynb' notebook.

## Data Processing
### Construct dataset - Dataset_construct.py
After obtaining data from the website, it is necessary to clean and organize the data into the following structure: Food_Name, Effect, Ingredients, Steps. As the data on the website does not separate well these four elements, we had to write functions to construct our dataset. The relevant code can be found in "Dataset_construct.py".

### Categorize - Categorize.ipynb
To conduct further data analysis and implement the search function for the website, the initial step involves categorizing our data. This categorization includes recipe categories (e.g., main dishes, soup, congee), method categories (e.g., boil, pan-fry, steam), ingredient categories (e.g., meat, vegetable, plant, Chinese medicinal materials), and effect categories (e.g., General Health and Wellness, Gastrointestinal Issues, Musculoskeletal Issues). The code responsible for generating the dataframe containing information for all these categories is located in the "Categorize.ipynb" notebook. The resulting dataframe is stored in the "/categorize" folder.

### Ancient to Modern Chinese Translation - Ancient_Chinese_Translation.ipynb
ChatGPT3.5 was employed for translation to achieve more fluent translated text. The helper function responsible for constructing the data frame after obtaining translations from ChatGPT is presented in the "Ancient_Chinese_Translation.ipynb" notebook.

### English Translation - English_translation.ipynb
For the English translation, we discovered a digital document online that contains the English version of the book (YinShanZhengYao_english.pdf). Consequently, we extracted the English translated recipes from this document and built an English database for the recipes. Subsequently, we created a comprehensive recipe dataset that includes both English and Chinese versions. To categorize the data in English, given that we already had categorized data in Chinese, we devised a mapping method to establish a correspondence between Chinese and English categories. The code for constructing the full recipe and implementing the mapping function can be found in the "English_translation.ipynb" notebook.

## Data Analysis - Data_Analysis.ipynb
The code for conducting data analysis is stored in the file named "Data_Analysis.ipynb." Within this code, we have illustrated the step-by-step process of performing various analyses related to recipes. These analyses encompass aspects such as recipe category, ingredient frequency, ingredient pairing, ingredient category, ingredient category pairing, cooking methods, effects, and correlations between effects and ingredients. Through these analyses, a more in-depth understanding of the cookbook can be gained, revealing intriguing correlations and properties of the recipes. The analysis primarily relies on the use of the **Pandas** and **Scikit-learn** libraries for data manipulation. Additionally, the **Matplotlib**, **Seaborn**, and **WordCloud** libraries are employed for data visualization purposes.

One notable finding involves the examination of ingredient frequency, where "Mutton" emerged as the most frequently occurring ingredient. This observation aligns with the historical context of the book, which was written and published during the Yuan dynasty, known for its Mongol leadership and renowned for mutton dishes. Additionally, the analysis of ingredient pairing highlighted that the combination of "Mutton" and "Tsaoko cardamom" occurs most frequently. This pairing is logical, considering that Tsaoko cardamom can help mitigate the smell of mutton. Furthermore, the analysis of ingredient categories revealed that "meat" is the most frequently occurring category, closely followed by Chinese medicinal materials. This aligns with the dual nature of the book as both a culinary and medical text.

For further captivating insights, please refer to the details provided in the "Data_Analysis.ipynb" file.
## Web Construction - Web_Construction.ipynb
The code for building the website is contained in the file named "Web_Construction.ipynb." The code primarily consists of two main parts: the first part involves generating the HTML tags, including the checkboxes which user can select different search crieria, such as effect categories, ingredients and more, for the website. After HTML tags are generated, we then plug all these tags into our "index.html" file. Besides HTML tags, we also generate a JSON file containing all the recipes [recipes.json](./webpage/recipes.json) to populate the recipes entries when the webpage is loaded and to facilitate search function where we populate the recipe entries based on the search result.

To enable the recipe research function, we have incorporated [**fuse.js**](https://www.fusejs.io/), a library that offers fuzzy searching capabilities, allowing for approximate string matching. Detailed information about the search function can be found in the "main.js" file.

All the files related to the website are available in the "webpage" folder.

## Dataset
- /YinShanZhengYao_text: Original text collected from the website of the book.
- /first_clean_recipe: Ancient Chinese recipe dataframe with the structure: Food_Name, Effect, Ingredients, Steps. It also includes the English version of the recipe in the same data structure obtained from the English translation documents (YinShanZhengYao_english.pdf).
- /ingredient: Ingredient dataframe with the structure: Food_Name, Food_Name_en, Ingredient, Ingredient_en, Amount. It contains both Chinese and English versions.
- /categorize: All categorized data, including recipe category, cooking method, ingredient category, and effect, in both Chinese and English versions.
- /translation_receipe_v1: Translated recipes from ancient Chinese to modern Chinese.
- /webpage: All related codes and files for website construction.
- full_recipe.csv: Full recipes with both english and chinese.
