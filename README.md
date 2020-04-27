# SARS-CoV-2 Positive Cases Map/News Tracker
General Assembly Final Project

## Getting Started

This status of this project is a proof of concept at the moment. There are still alot of fixes to be made regarding bugs/CSS positioning. 


### Prerequisites

What things you need to install the software and how to install them

If you do try to run the app, please note that you will need an API key from "News API". The app in this repository has the key abstracted. You will need to input your key at the end of the ```news_url``` link located in the ```update_news()``` function.

```python
def update_news():
    news_url = "http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=[KEY]"
    ...
```

## Deployment

This app will be deployed and hosted on Heroku once finished.

## Built With

* [The COVID Tracking Project](https://covidtracking.com/) - COVID-19 Country Data API
* [COVID 19 API](https://covid19api.com/) - COVID-19 Data API for U.S States
* [News API](https://newsapi.org/) - Provides the news feed on COVID-19

## Authors

* **Ernie Enriquez** - *Initial work* - [Ernie Enriquez](https://github.com/ernenr1)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Big thank you to:
* [Martin Skarzynski](https://marskar.github.io/) for teaching this Python class and help developing this app.
* General Assembly Python classmates
* General Assembly
