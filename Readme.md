# RedisStatusChecker

RedisStatusChecker is a Python utility that provides a quick and rich overview of your Redis server's metrics and performance. It uses the `redis` and `rich` libraries to fetch server statistics and display them in a visually appealing table format, including details like Redis version, mode, memory usage, client connections, and command statistics.

## Features

-   Fetch and display Redis server statistics.
-   Rich console table output with key metrics.
-   Error handling for connection issues.

## Prerequisites

Before you begin, ensure you have met the following requirements:

-   Python 3.x
-   Redis server running locally or accessible remotely

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/koorukuroo/RedisStatusChecker.git
```

Navigate to the cloned repository. Install the necessary packages using pip:

```bash
pip install redis rich
```

## Usage

Run the script with Python:

```bash
python redis_status_checker.py
```

```
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Metric               ┃ Value              ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Redis Version        │ 7.1.0              │
│ Redis Mode           │ standalone         │
│ OS                   │ Amazon ElastiCache │
│ Architecture Bits    │ 64                 │
│ TCP Port             │ 6379               │
│ Max Clients          │ 65000              │
│ Connected Clients    │ 8                  │
│ Used Memory          │ 10.19M             │
│ Commands per second  │ 0                  │
│ Hit rate             │ 0.85               │
└──────────────────────┴────────────────────┘
```

Upon execution, the script will attempt to connect to the Redis server at `localhost:6379`. If successful, it will display various Redis metrics in a table format.

## Contributing

Contributions to the RedisStatusChecker are welcome.

## License

Distributed under the MIT License.
