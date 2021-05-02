
---

## 🧐 About <a name = "about"></a>

Project was created for "SKNS Warsztaty z Pythona". <br>
Consists crawler for scraping real estate data from gumtree and jupyter notebook with ML.

## 🏁 Getting Started <a name = "getting_started"></a>

To clone repository type:
```
git clone https://github.com/Santhin/real-estate
```
To run crawler locally:
```
pip install -r requirements
python app.py
```

### Project structure
```
.
├── crawler
│   ├── app.py
│   ├── aps_asyncio.py
│   ├── gumtree
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │       ├── gumtree_crawler.py
│   │       ├── __init__.py
│   │       └── stack.py
│   ├── install_asyncio.py
│   ├── Procfile
│   ├── requirements.txt
│   └── scrapy.cfg
├── LICENSE
├── ml
│   ├── features
│   │   ├── rankingcen.xlsx
│   │   ├── Ranking\ Dzielnic\ 2020\ Warszawa.pdf
│   │   ├── ranking_dzielnic_warszawy_pod_wzgledem_atrakcyjnosci_warunkow_zycia_2017.pdf
│   │   ├── ranking_otodom.csv
│   │   ├── ranking.txt
│   │   └── ranking.xlsx
│   ├── notebooks
│   │   ├── ML\ endgame\ floydhub.ipynb
│   │   ├── ML\ endgame.ipynb
│   │   ├── NLP\ eda\ etc.ipynb
│   │   ├── Pipeline\ mongoRaw\ to\ clean\ before\ EDA.ipynb
│   │   └── real\ EDA.ipynb
│   └── pictures
│       ├── images.png
│       ├── ml_map.png
│       ├── simple-house-exterior-white-background_1308-50195.jpg
│       ├── unnamed.jpg
│       └── white-house-background-check-democratic-party-republican-party-house-png.jpg
└── README.md

6 directories, 32 files
```


## 🚀 Deployment <a name = "deployment"></a>
The crawler was deployed on Heroku and in 15min intervals was activated with advanced python scheduler.

## ⛏️ Built Using <a name = "built_using"></a>

- [Scrapy](https://scrapy.org/) - Crawler
- [MongoDB](https://www.mongodb.com/) - Database
- [Heroku](https://www.heroku.com/) - Deployment
- [Floydhub](https://www.floydhub.com/) - Traning model


## 🛠️ Todo
- add requirements.txt to ML folder