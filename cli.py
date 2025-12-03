# cli.py
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Weather Harvester CLI")

    # Multiple cities: -c Delhi -c Pune
    parser.add_argument(
        "-c", "--city",
        action="append",
        help="City name (can be given multiple times: -c Delhi -c Pune)"
    )

    # Alternative: comma-separated cities
    parser.add_argument(
        "-C", "--cities",
        type=str,
        help="Comma-separated list of cities: --cities Delhi,Mumbai"
    )

    # Coordinate override (used as fallback if city not in known list)
    parser.add_argument(
        "--lat",
        type=float,
        help="Latitude value (used if city has no predefined coordinates)"
    )

    parser.add_argument(
        "--lon",
        type=float,
        help="Longitude value (used if city has no predefined coordinates)"
    )

    # Cache toggle
    parser.add_argument(
        "--use-cache",
        action="store_true",
        help="Use cached data if available"
    )

    # Logging level
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level"
    )

    # Alert threshold
    parser.add_argument(
        "--alert-temp",
        type=float,
        help="Temperature threshold to trigger alert (°C)"
    )

    # Config path
    parser.add_argument(
        "--config",
        type=str,
        default="config/config.ini",
        help="Path to configuration file"
    )
    parser.add_argument(
        "--alert-low",
        type=float,
        help="Trigger alert if temperature drops below this value (°C)"
    )
    parser.add_argument(
        "--map",
        action="store_true",
        help="Open location on Google Maps"
    )
    parser.add_argument(
    "--show-cache",
    action="store_true",
    help="Display cached weather data as a table"
     )
    parser.add_argument(
    "--export-csv",
    action="store_true",
    help="Export cached weather data to a CSV file."
)


    return parser.parse_args()
