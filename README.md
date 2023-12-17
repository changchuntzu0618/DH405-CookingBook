# Digitalizing a Chinese Cooking Book: YingShanZhengYao
## Introduction
This project is part of the DH405 Digital Humanities course and aims to digitize an Ancient Chinese Cookbook and medical text known as [**YinShanZhengYao**](https://en.wikipedia.org/wiki/Yinshan_zhengyao). Published in 1330, this text holds significant cultural importance in the field of Chinese medical technology. The project involves tasks such as data collection, data processing, data analysis, and the construction of a web platform.

## Data collection
## Data Processing
### Categorize

### Ancient to Modern Chinese Translation
ChatGPT3.5 was employed for translation to achieve more fluent translated text. The helper function responsible for constructing the data frame after obtaining translations from ChatGPT is presented in the "Ancient_Chinese_Translation.ipynb" notebook.
### English Translation
## Data Analysis - Data_Analysis.ipynb
The code for conducting data analysis is stored in the file named "Data_Analysis.ipynb." Within this code, we have illustrated the step-by-step process of performing various analyses related to recipes. These analyses encompass aspects such as recipe category, ingredient frequency, ingredient pairing, ingredient category, ingredient category pairing, cooking methods, effects, and correlations between effects and ingredients. Through these analyses, a more in-depth understanding of the cookbook can be gained, revealing intriguing correlations and properties of the recipes. The analysis primarily relies on the use of the **Pandas** and **Scikit-learn** libraries for data manipulation. Additionally, the **Matplotlib**, **Seaborn**, and **WordCloud** libraries are employed for data visualization purposes.

One notable finding involves the examination of ingredient frequency, where "Mutton" emerged as the most frequently occurring ingredient. This observation aligns with the historical context of the book, which was written and published during the Yuan dynasty, known for its Mongol leadership and renowned for mutton dishes. Additionally, the analysis of ingredient pairing highlighted that the combination of "Mutton" and "Tsaoko cardamom" occurs most frequently. This pairing is logical, considering that Tsaoko cardamom can help mitigate the smell of mutton. Furthermore, the analysis of ingredient categories revealed that "meat" is the most frequently occurring category, closely followed by Chinese medicinal materials. This aligns with the dual nature of the book as both a culinary and medical text.

For further captivating insights, please refer to the details provided in the "Data_Analysis.ipynb" file.
## Web Construction - Web_Construction.ipynb
The code for building the website is contained in the file named "Web_Construction.ipynb." The code primarily consists of two main parts: the first part involves generating the HTML for the website, resulting in the creation of the file "index.html." The second part focuses on generating a JSON file that stores all the recipes (recipes.json), facilitating the research function on the website.

To enable the recipe research function, we have incorporated [**fuse.js**](https://www.fusejs.io/), a library that offers fuzzy searching capabilities, allowing for approximate string matching. Detailed information about the search function can be found in the "main.js" file.

All the files related to the website are available in the "webpage" folder.
