import redis
from rich.console import Console
from rich.table import Table


# Create console object for rich print
console = Console()

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

try:
    # Get server stats
    stats = r.info()

    # Create a table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="dim", width=20)
    table.add_column("Value")

    # Add rows to the table with key metrics and additional info
    table.add_row("Redis Version", stats['redis_version'])
    table.add_row("Redis Mode", stats['redis_mode'])
    table.add_row("OS", stats['os'])
    table.add_row("Architecture Bits", str(stats['arch_bits']))
    table.add_row("TCP Port", str(stats['tcp_port']))
    table.add_row("Max Clients", str(stats['maxclients']))
    table.add_row("Connected Clients", str(stats['connected_clients']))
    table.add_row("Used Memory", str(stats['used_memory_human']))
    table.add_row("Commands per second", str(
        stats['instantaneous_ops_per_sec']))
    # Avoid division by zero
    hit_rate = stats['keyspace_hits'] / \
        (stats['keyspace_hits'] + stats['keyspace_misses'] + 1)
    table.add_row("Hit rate", f"{hit_rate:.2f}")

    # Print the table to the console
    console.print(table)

except redis.exceptions.ConnectionError:
    console.print("[bold red]Failed to connect to Redis[/bold red]")
