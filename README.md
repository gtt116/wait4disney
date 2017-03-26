## What is this ?

We all love Shanghai Disneyland, but the long long long waiting queue is going to kill
us. So I need a better place to find which attraction is the lightest. 

Also I want to find out which season is the best choice to travel to
Disneyland, the statistic will give me the answer.


## Installation

1. install influxdb
2. install grafana

```bash
$ git clone git://github.com/gtt116/wait4disney
$ cd wait4disney
$ pip install -r requirements.txt
$ python main.py
```
The influxdb configration was hard coded at main.py, please feel free to change
them to meet your environment.

You can setup a crontab job to update disney waiting queue every minute.
The grafana dashboard template locates at `wait4disney/doc/grafana.json`, you can
import it to give a try.

## Heatmap

To generate heatmap follow these steps:

```
python web.py > disney.json
python -mSimpleHTTPServer
```

Then open your favourite web browser to http://127.0.0.1:8000/index.html.
you can also setup a crontab to generate report every day.

## Web Snapshot

![wait](https://raw.githubusercontent.com/gtt116/wait4disney/master/doc/demo.png)
