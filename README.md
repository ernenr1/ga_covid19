# SARS-CoV-2 Positive Cases Map/News Tracker
##### Current Version/Update Log
v1.1.0
<br>
..* Commented out code
<br>
..* Created time/date stamp
<br>
..* Reduce/optimize code

## Getting Started

We are in a now live! Please note that this Github repository is not serving the Heroku app.

[LIVE LINK](https://ga-covid19.herokuapp.com/)


### Prerequisites

What things you need to install the software and how to install them

If you do try to run the app, please note that you will need an API key from "News API". The app in this repository has the key abstracted. You will need to input your key at the end of the ```news_url``` link located in the ```update_news()``` function.

```python
def update_news():
    news_url = "http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=[KEY]"
    ...
```

## Deployment

Currently this app is hosted on Heroku. Please note that the app is hosted using Heroku's free tier. Therefore, the app may take time to load and wake up because Heroku puts the app to sleep.

## Built With

* [The COVID Tracking Project](https://covidtracking.com/) - COVID-19 Data API for U.S States
* [COVID 19 API](https://covid19api.com/) - COVID-19 World Data API
* [News API](https://newsapi.org/) - Provides the news feed on COVID-19

## Authors

* **Ernie Enriquez** - [My Personal GitHub Repo](https://github.com/ernenr1)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Big thank you to:
* [Martin Skarzynski](https://marskar.github.io/) for teaching this Python class and help developing this app.
* General Assembly Python classmates
* General Assembly
