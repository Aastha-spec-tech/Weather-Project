# 🌦️ Weather Alert CLI Tool  
A powerful, multi-feature command-line weather monitoring system built in Python.  
This tool fetches real-time weather, displays it beautifully in the terminal, shows GUI maps, sends desktop notifications, handles alerts, exports data, and caches city weather intelligently.

------------------------------------------------
Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

------------------------------------------------
## 🚀 Features

### ✅ **1. Multi-City Weather Fetching (Threaded)**
Fetch weather data for multiple cities simultaneously using `ThreadPoolExecutor` for ultra-fast performance.
commands used :
1) python main.py -c name_of_city
2) python main.py -c name_city --alert-temp 4
3) python main.py -c name_city --map
4) python main.py --export-csv
5) python main.py -c delhi -c ranchi -c pune
┌──────────────────────┐
                 │     main.py          │
                 │  (App Controller)    │
                 └─────────┬────────────┘
                           │
   ┌───────────────────────┼────────────────────────┐
   │                       │                        │
   ▼                       ▼                        ▼
┌──────────┐        ┌──────────┐             ┌──────────┐
│  cli.py  │        │config.py │             │logging_   │
│ Parses   │        │ Loads     │            │ system.py │
│ arguments│        │ config.ini│            │ Sets logs │
└────┬─────┘        └─────┬────┘            └─────┬─────┘
     │                    │                      │
     ▼                    ▼                      ▼
┌──────────┐      ┌────────────┐        ┌─────────────────┐
│ fetcher  │      │ cache.py   │        │ alerts.py        │
│ Fetches  │◄────►│ load/save  │        │ temp threshold   │
│ API data │      │ TTL logic  │        │ color + sound    │
└────┬─────┘      └─────┬──────┘        └───────┬─────────┘
     │                    │                      │
     └──────────────┬─────▼──────────────┬──────┘
                    ▼                    ▼
             ┌────────────┐     ┌──────────────────┐
             │ data/       │     │ tests/           │
             │ cache files │     │ unittest modules │
             └────────────┘     └──────────────────┘

